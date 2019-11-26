![logo](./image/logo_django.png)

<a name="0"></a>

# [MỤC LỤC](#0)
---
- ### [I. LẬP TRÌNH WEB VỚI DJANGO 2019 - BASIC](#I)

	- #### [1.1 Django web Develepment with Python](#I_01)

	- #### [1.2 Model - Django Web Development with Python](#I_02)

	- #### [1.3 Admin and Apps - Django Web Development with Python](#I_03)

	- #### [1.4 Views and Templates - Django Web Development with Python](#I_04)

<a name="00"></a>

#### [ĐIỀU KIỆN](#00)

- Install Python

- Install Virtualenv

<a name="I"></a>

# [I. LẬP TRÌNH WEB VỚI DJANGO 2019 - BASIC](#I)
---

<a name="I_01"></a>

- #### [1.1 Django web Develepment with Python](#I_01)
	
	+ 1.1.1 Create virtualenv Django

	```
	virtualenv --no-site-package virtualenv_web
	```

	+ 1.1.2 Create Project Django mysite

	```
	django-admin startproject mysite
	```

	+ 1.1.3 Create Apps main

	```
	python manage.py startapp main
	```

	+ 1.1.4 Code

		* mysite -> mysite -> urls.py

		```python
		from django.contrib import admin
		from django.urls import path, include

		urlpatterns = [
			path('', include('main.urls')),
			path('admin/', admin.site.urls),
		]
		```

		* mysite -> main -> urls.py

		```python
		from django.urls import path
		from . import views

		app_name = 'main'

		urlpatterns=[
			path('', views.homepage, name="homepage"),
		]
		```

		* mysite -> main -> views.py

		```python
		from django.shortcuts import render
		from django.http import HttpResponse

		def homepage(request):
			return HttpResponse('Wow this is an <strong>awesome</strong> BTN')
		```

<a name="I_02"></a>

- #### [1.2 Model - Django Web Development with Python](#I_02)

	+ 1.2.1 Model in app main

		* mysite -> main -> models.py

		```python
		from django.db import models

		class Tutorial(models.Model):
			tutorial_title=models.CharField(max_length=200)
			tutorial_content=models.TextField()
			tutorial_published=models.DateTimeField('date published')

			def __str__(self):
				return self.tutorial_title
		```

		* mysite -> mysite -> __pycache__ -> settings.py

		```python
		INSTALLED_APPS = [
			...,
			'main.apps.MainConfig',
		]
		```

		> ```python
		> python manage.py makemigrations
		> ```
		>
		> ```python
		> python manage.py sqlmigrate main 0001
		> ```
		>
		> ```python
		> python manage.py migrate
		> ```

<a name="I_03"></a>

- #### [1.3 Admin and Apps - Django Web Development with Python](#I_03)

	+ 1.3.1 Create user and pass admin

		> ```python manage.py createsuperuser``` tạo user admin và passworld
		>
		> Sau khi tạo xong đăng nhập bằng ```127.0.0.1:800\admin```, để vô trang admin
	
		* mysite -> main -> models.py

		```python
		from django.db import models
		from django.utils import timezone

		class Tutorial(models.Model):
			tutorial_title=models.CharField(max_length=200)
			tutorial_content=models.TextField()
			tutorial_published=models.DateTimeField("date published", default=timezone.now())

			def __str__(self):
				return self.tutorial_title
		```

	+ 1.3.2 Install TinyMCE

		> Package này dùng để thêm chức năng cho content

		```
		pip install django-tinymce4-lite
		```

		* mysite -> mysite -> settings.py

		```python
		INSTALLED_APPS = [
			'django.contrib.admin',
			'django.contrib.auth',
			'django.contrib.contenttypes',
			'django.contrib.sessions',
			'django.contrib.messages',
			'django.contrib.staticfiles',
			'main.apps.MainConfig',
			'tinymce',
		]
		```

		* mysite -> main -> admin.py

		```python
		from django.contrib import admin
		from .models import Tutorial
		from tinymce.widgets import TinyMCE
		from django.db import models

		class TutorialAdmin(admin.ModelAdmin):
			fieldsets = [
				("Title/date", {"fields":["tutorial_title","tutorial_published"]}),
				("Content",{"fields":["tutorial_content"]})
			]

			formfield_overrides = {
				models.TextField: {'widget': TinyMCE()}
			}

		admin.site.register(Tutorial, TutorialAdmin)
		```

<a name="I_04"></a>

- #### [1.4 Views and Templates - Django Web Development with Python](#I_04)

	+ mysite -> main -> views.py

		```python
		from django.shortcut import render
		from django.http import HttpResponse
		from .models import Tutorial

		def homepage(request):
			return render(request=request,
				template_name="main/home.html",
				context={"tutorials":Tutorial.objects.all})
		```

	+ mysite -> main -> templates -> main -> home.html

		```python
		<head>
			{% load static %}
			<link href="{% static 'tinymce/css/prism.css' rel="stylesheet"%}">
		</head>

		<body>
			{% for tut in tutorials %}
				<hr>
				<p>{{tut.tutorial_title}}</p>
				<p>{{tut.tutorial_published}}</p>
				<p>{{tut.tutorial_content | safe}}</p>
				<hr>
			{% endfor%}
		</body>

		<script src="{% static 'tinymce/js/prism.js'%}"></script>
		```

[link tham khảo](https://www.youtube.com/watch?v=yD0_1DPmfKM&list=PLQVvvaa0QuDe9nqlirjacLkBYdgc2inh3)