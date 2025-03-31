import os
import django
import requests
import tempfile
from pathlib import Path
from django.core.files import File

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'learning_platform.settings')
django.setup()

from courses.models import Course

# Create media/course_images directory if it doesn't exist
media_path = Path('media/course_images')
media_path.mkdir(parents=True, exist_ok=True)

# Course image URLs - using placeholder images that represent each course topic
course_images = {
    'Python Django Masterclass': 'https://raw.githubusercontent.com/github/explore/80688e429a7d4ef2fca1e82350fe8e3517d3494d/topics/django/django.png',
    'Machine Learning Fundamentals': 'https://raw.githubusercontent.com/github/explore/80688e429a7d4ef2fca1e82350fe8e3517d3494d/topics/python/python.png',
    'React Native Development': 'https://raw.githubusercontent.com/github/explore/80688e429a7d4ef2fca1e82350fe8e3517d3494d/topics/react-native/react-native.png',
    'Full Stack JavaScript': 'https://raw.githubusercontent.com/github/explore/80688e429a7d4ef2fca1e82350fe8e3517d3494d/topics/javascript/javascript.png',
    'Data Analysis with Python': 'https://raw.githubusercontent.com/github/explore/80688e429a7d4ef2fca1e82350fe8e3517d3494d/topics/numpy/numpy.png'
}

def download_and_save_image(url, course):
    try:
        # Download the image
        response = requests.get(url)
        if response.status_code == 200:
            # Create a temporary file
            temp_file = tempfile.NamedTemporaryFile()
            temp_file.write(response.content)
            temp_file.flush()

            # Create a filename based on the course title
            filename = f"{course.title.lower().replace(' ', '_')}.png"

            # Save the image to the course
            course.image.save(filename, File(temp_file), save=True)
            print(f"Successfully added image for: {course.title}")
        else:
            print(f"Failed to download image for: {course.title}")
    except Exception as e:
        print(f"Error processing image for {course.title}: {str(e)}")

# Update each course with its corresponding image
for course in Course.objects.all():
    if course.title in course_images:
        if not course.image:  # Only add image if it doesn't exist
            download_and_save_image(course_images[course.title], course)
        else:
            print(f"Image already exists for: {course.title}")

print("Finished adding images to courses!")