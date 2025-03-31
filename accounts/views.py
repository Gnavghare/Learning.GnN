from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth import login, authenticate
from django.urls import reverse
from django.db import transaction
from .forms import UserRegistrationForm, UserProfileForm
from .models import UserProfile

def register(request):
    if request.user.is_authenticated:
        messages.info(request, 'You are already registered and logged in.')
        return redirect('courses:home')
        
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid() and request.POST.get('terms'):
            try:
                with transaction.atomic():
                    user = form.save()
                    login(request, user)
                    messages.success(request, 'Welcome! Your account has been created successfully.')
                    return redirect('accounts:profile')
            except Exception as e:
                messages.error(request, 'An error occurred during registration. Please try again.')
        else:
            if not request.POST.get('terms'):
                messages.error(request, 'You must agree to the Terms and Conditions.')
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f'{error}')
    else:
        form = UserRegistrationForm()
    
    return render(request, 'accounts/register.html', {'form': form})

@login_required
def profile(request):
    if request.method == 'POST':
        profile_form = UserProfileForm(request.POST, request.FILES, instance=request.user.profile)
        if profile_form.is_valid():
            profile_form.save()
            messages.success(request, 'Your profile has been updated successfully!')
            return redirect('accounts:profile')
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        profile_form = UserProfileForm(instance=request.user.profile)
    
    enrolled_courses = request.user.profile.enrolled_courses.all()
    return render(request, 'accounts/profile.html', {
        'profile_form': profile_form,
        'enrolled_courses': enrolled_courses
    })

@login_required
def enroll_course(request, course_id):
    from courses.models import Course
    course = get_object_or_404(Course, id=course_id)
    if request.user.profile.enrolled_courses.filter(id=course_id).exists():
        messages.info(request, f'You are already enrolled in {course.title}.')
    else:
        request.user.profile.enrolled_courses.add(course)
        messages.success(request, f'You have successfully enrolled in {course.title}!')
    return redirect('courses:course_detail', slug=course.slug)

@login_required
def unenroll_course(request, course_id):
    from courses.models import Course
    course = get_object_or_404(Course, id=course_id)
    if request.user.profile.enrolled_courses.filter(id=course_id).exists():
        request.user.profile.enrolled_courses.remove(course)
        messages.success(request, f'You have unenrolled from {course.title}')
    else:
        messages.info(request, f'You were not enrolled in {course.title}.')
    return redirect('courses:course_detail', slug=course.slug)
