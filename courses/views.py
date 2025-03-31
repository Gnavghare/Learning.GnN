from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Course, Category, Note

def home(request):
    categories = Category.objects.all()
    featured_courses = Course.objects.filter(is_published=True)[:6]
    return render(request, 'courses/home.html', {
        'categories': categories,
        'featured_courses': featured_courses
    })

def course_list(request):
    category_id = request.GET.get('category')
    if category_id:
        courses = Course.objects.filter(category_id=category_id, is_published=True)
    else:
        courses = Course.objects.filter(is_published=True)
    categories = Category.objects.all()
    return render(request, 'courses/course_list.html', {
        'courses': courses,
        'categories': categories
    })

def course_detail(request, slug):
    course = get_object_or_404(Course, slug=slug, is_published=True)
    notes = course.notes.all()
    return render(request, 'courses/course_detail.html', {
        'course': course,
        'notes': notes
    })

@login_required
def note_detail(request, course_slug, note_id):
    course = get_object_or_404(Course, slug=course_slug, is_published=True)
    note = get_object_or_404(Note, id=note_id, course=course)
    return render(request, 'courses/note_detail.html', {
        'course': course,
        'note': note
    })
