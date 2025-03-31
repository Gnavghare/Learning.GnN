import os
import django
import json

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'learning_platform.settings')
django.setup()

from django.contrib.auth.models import User
from courses.models import Category, Course, Note

# Get or create admin user
admin_user = User.objects.get(username='admin')

# Sample courses data
categories = [
    {
        'name': 'Web Development',
        'description': 'Learn modern web development technologies',
        'icon': 'fa-code'
    },
    {
        'name': 'Data Science',
        'description': 'Master data analysis and machine learning',
        'icon': 'fa-chart-line'
    },
    {
        'name': 'Mobile Development',
        'description': 'Build mobile applications for iOS and Android',
        'icon': 'fa-mobile-alt'
    }
]

courses = [
    {
        'title': 'Python Django Masterclass',
        'category': 'Web Development',
        'description': 'Master Django web development framework',
        'overview': '''Learn Django from basics to advanced concepts. This comprehensive course covers everything you need to know to build modern web applications using Django framework. Perfect for beginners and intermediate developers looking to enhance their skills.''',
        'key_points': [
            'Understanding Django MTV architecture',
            'Building robust database models',
            'Creating dynamic templates',
            'Implementing authentication and authorization',
            'REST API development with Django REST framework'
        ],
        'duration': '8 weeks',
        'difficulty_level': 'intermediate',
        'notes': [
            {
                'title': 'Getting Started with Django',
                'content': '''Django is a high-level Python web framework that enables rapid development of secure and maintainable websites. Built by experienced developers, Django takes care of much of the hassle of web development, so you can focus on writing your app without needing to reinvent the wheel.

Example:
```python
# Create a new Django project
django-admin startproject myproject

# Create a new app
python manage.py startapp myapp

# Define a model
class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
```''',
                'content_type': 'overview'
            },
            {
                'title': 'Django Models and Database Management',
                'content': '''Learn how to create and manage database models in Django. Understanding models is crucial for building data-driven applications.

Example:
```python
from django.db import models

class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product)
    total = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
```''',
                'content_type': 'detailed'
            }
        ]
    },
    {
        'title': 'Machine Learning Fundamentals',
        'category': 'Data Science',
        'description': 'Introduction to machine learning concepts and applications',
        'overview': '''Dive into the world of machine learning with this comprehensive course. Learn about different ML algorithms, data preprocessing, model evaluation, and practical applications using Python's popular ML libraries.''',
        'key_points': [
            'Understanding ML algorithms',
            'Data preprocessing techniques',
            'Model training and evaluation',
            'Feature engineering',
            'Practical ML project implementation'
        ],
        'duration': '10 weeks',
        'difficulty_level': 'advanced',
        'notes': [
            {
                'title': 'Introduction to Machine Learning',
                'content': '''Machine Learning is a subset of artificial intelligence that focuses on building systems that learn from data. This course introduces fundamental concepts and practical applications.

Example using scikit-learn:
```python
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

# Prepare data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# Train model
model = LogisticRegression()
model.fit(X_train, y_train)
```''',
                'content_type': 'overview'
            },
            {
                'title': 'Data Preprocessing in Machine Learning',
                'content': '''Data preprocessing is a crucial step in any machine learning project. Learn how to handle missing values, encode categorical variables, and scale features.

Example:
```python
import pandas as pd
from sklearn.preprocessing import StandardScaler

# Handle missing values
df.fillna(df.mean(), inplace=True)

# Scale features
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)
```''',
                'content_type': 'detailed'
            }
        ]
    },
    {
        'title': 'React Native Development',
        'category': 'Mobile Development',
        'description': 'Build cross-platform mobile apps with React Native',
        'overview': '''Learn to develop mobile applications for both iOS and Android using React Native. This course covers everything from setup to deployment, including native modules and performance optimization.''',
        'key_points': [
            'Setting up React Native environment',
            'Building UI components',
            'State management with Redux',
            'Navigation and routing',
            'Native module integration'
        ],
        'duration': '12 weeks',
        'difficulty_level': 'intermediate',
        'notes': [
            {
                'title': 'Getting Started with React Native',
                'content': '''React Native lets you build mobile apps using only JavaScript. It uses the same design as React, letting you compose a rich mobile UI from declarative components.

Example:
```javascript
import React from 'react';
import { View, Text, StyleSheet } from 'react-native';

const App = () => {
  return (
    <View style={styles.container}>
      <Text style={styles.text}>Welcome to React Native!</Text>
    </View>
  );
};

const styles = StyleSheet.create({
  container: {
    flex: 1,
    justifyContent: 'center',
    alignItems: 'center',
  },
  text: {
    fontSize: 24,
    fontWeight: 'bold',
  },
});
```''',
                'content_type': 'overview'
            },
            {
                'title': 'State Management in React Native',
                'content': '''Learn how to manage application state effectively in React Native using Redux and Context API.

Example:
```javascript
// Redux store setup
import { createStore } from 'redux';

const initialState = {
  counter: 0,
};

function reducer(state = initialState, action) {
  switch (action.type) {
    case 'INCREMENT':
      return { counter: state.counter + 1 };
    default:
      return state;
  }
}

const store = createStore(reducer);
```''',
                'content_type': 'detailed'
            }
        ]
    },
    {
        'title': 'Full Stack JavaScript',
        'category': 'Web Development',
        'description': 'Master modern JavaScript stack development',
        'overview': '''Comprehensive course covering both frontend and backend JavaScript development. Learn Node.js, Express, React, and MongoDB to build full-stack applications.''',
        'key_points': [
            'Modern JavaScript (ES6+)',
            'Node.js and Express backend',
            'React frontend development',
            'MongoDB database integration',
            'RESTful API design'
        ],
        'duration': '14 weeks',
        'difficulty_level': 'intermediate',
        'notes': [
            {
                'title': 'Modern JavaScript Features',
                'content': '''Explore modern JavaScript features and how they improve code quality and developer productivity.

Example:
```javascript
// ES6+ Features
const fetchUser = async (id) => {
  try {
    const response = await fetch(`/api/users/${id}`);
    const data = await response.json();
    return data;
  } catch (error) {
    console.error('Error:', error);
  }
};

// Destructuring and spread operator
const { name, email, ...rest } = user;
const newUser = { ...user, age: 25 };
```''',
                'content_type': 'overview'
            },
            {
                'title': 'Building REST APIs with Express',
                'content': '''Learn how to create robust REST APIs using Express.js and MongoDB.

Example:
```javascript
const express = require('express');
const router = express.Router();

router.get('/users', async (req, res) => {
  try {
    const users = await User.find();
    res.json(users);
  } catch (error) {
    res.status(500).json({ message: error.message });
  }
});
```''',
                'content_type': 'detailed'
            }
        ]
    },
    {
        'title': 'Data Analysis with Python',
        'category': 'Data Science',
        'description': 'Learn data analysis using Python libraries',
        'overview': '''Master data analysis techniques using Python's powerful libraries including Pandas, NumPy, and Matplotlib. Learn how to clean, analyze, and visualize data effectively.''',
        'key_points': [
            'Data manipulation with Pandas',
            'Statistical analysis with NumPy',
            'Data visualization with Matplotlib',
            'Exploratory data analysis',
            'Time series analysis'
        ],
        'duration': '8 weeks',
        'difficulty_level': 'beginner',
        'notes': [
            {
                'title': 'Introduction to Pandas',
                'content': '''Learn how to use Pandas for data manipulation and analysis in Python.

Example:
```python
import pandas as pd
import numpy as np

# Create a DataFrame
df = pd.DataFrame({
    'A': np.random.randn(5),
    'B': np.random.randn(5),
    'C': np.random.randn(5)
})

# Basic operations
print(df.describe())
print(df.mean())
```''',
                'content_type': 'overview'
            },
            {
                'title': 'Data Visualization with Matplotlib',
                'content': '''Master the art of data visualization using Matplotlib and Seaborn.

Example:
```python
import matplotlib.pyplot as plt
import seaborn as sns

# Create a line plot
plt.figure(figsize=(10, 6))
plt.plot(df.index, df['A'], label='Series A')
plt.plot(df.index, df['B'], label='Series B')
plt.title('Time Series Plot')
plt.xlabel('Time')
plt.ylabel('Value')
plt.legend()
plt.show()
```''',
                'content_type': 'detailed'
            }
        ]
    }
]

# Create categories
category_objects = {}
for cat_data in categories:
    category, created = Category.objects.get_or_create(
        name=cat_data['name'],
        defaults={
            'description': cat_data['description'],
            'icon': cat_data['icon']
        }
    )
    category_objects[cat_data['name']] = category

# Create courses and their notes
for course_data in courses:
    # Get the category
    category = category_objects[course_data['category']]
    
    # Create the course
    course, created = Course.objects.get_or_create(
        title=course_data['title'],
        defaults={
            'slug': course_data['title'].lower().replace(' ', '-'),
            'description': course_data['description'],
            'overview': course_data['overview'],
            'key_points': course_data['key_points'],
            'category': category,
            'instructor': admin_user,
            'duration': course_data['duration'],
            'difficulty_level': course_data['difficulty_level'],
            'is_published': True
        }
    )
    
    # Create notes for the course
    for note_data in course_data['notes']:
        Note.objects.get_or_create(
            course=course,
            title=note_data['title'],
            defaults={
                'content': note_data['content'],
                'content_type': note_data['content_type']
            }
        )

print("Sample courses, categories, and notes have been created successfully!")