![logo](./image/logo_django.png)

<a name="0"></a>

# [MỤC LỤC](#0)

> Version Django = 2.1.5

---
- ### [I. LẬP TRÌNH WEB VỚI DJANGO 2019 - BASIC](#I)

	- #### [1.1 Django web Develepment with Python](#I_01)

	- #### [1.2 Model - Django Web Development with Python](#I_02)

	- #### [1.3 Admin and Apps - Django Web Development with Python](#I_03)

	- #### [1.4 Views and Templates - Django Web Development with Python](#I_04)

	- #### [1.5 Styling w/ CSS - Django Web Development with Python](#I_05)

	- #### [1.6 User Registration - Django Web Development with Python](#I_06)

	- #### [1.7 Messages and Include - Django Web Development with Python](#I_07)

	- #### [1.8 User Login and Logout - Django Web Development with Python](#I_08)

	- #### [1.9 Linking models with Foreign Keys - Django Web Development with Python p.9](#I_09)

	- #### [1.10 Working with Foreign Key - Django Web Development with Python p.10](#I_10)

	- #### [1.11 Dynamic sidebar - Django Web Development with Python P.11](#I_11)

	- #### [1.12 Deploying Django to a server - Django Web Development with Python P.12](#I_12)



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
**[Link tham khảo](https://www.youtube.com/watch?v=yD0_1DPmfKM&list=PLQVvvaa0QuDe9nqlirjacLkBYdgc2inh3&index=1)**

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

		* mysite -> mysite -> settings.py

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

**[Link tham khảo](https://www.youtube.com/watch?v=aXxIjeGR6po&list=PLQVvvaa0QuDe9nqlirjacLkBYdgc2inh3&index=2)**

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
**[Link tham khảo](https://www.youtube.com/watch?v=BJfyATa9nX0&list=PLQVvvaa0QuDe9nqlirjacLkBYdgc2inh3&index=3)**

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

		22

**[Link tham khảo](https://www.youtube.com/watch?v=j9elKTmCEhY&list=PLQVvvaa0QuDe9nqlirjacLkBYdgc2inh3&index=4)**

<a name="I_05"></a>

- #### [1.5 Styling w/ CSS - Django Web Development with Python](#I_05)

	+ Vào [link Materializecss.com](https://materializecss.com/), Componects -> Cards, và Componects -> Navbar

	+ mysite -> main -> templates -> main -> home.html

	```html
	{% extends "main/header.html" %}
	{% block content%}
	  <div class="row">
	    {% for tut in tutorials %}
	    <div class="col s12 m6 14">
	      <div class="card blue-grey darken-1">
	        <div class="card-content white-text">
	          <span class="card-title">{{tut.tutorial_title}}</span>
	          <p style="font-style: 70%">{{tut.tutorial_published}}<p>
	          <p>{{tut.tutorial_content | safe}}<p>
	        </div>
	        <div class="card-action">
	          <a href="#">This is a link</a>
	          <a href="#">This is a link</a>
	        </div>
	      </div>
	    </div>
	    {%endfor%}
	  </div>
	{% endblock %}
	```

	+ mysite -> main -> templates -> main -> header.html

	```html
	<head>
	{% load static %}
	<link href="{% static 'tinymce/css/prism.css'%}" rel="stylesheet">
	<!-- Compiled and minified CSS -->
	<link rel="stylesheet" href="{% static 'main/css/materialize.css' %}">
	<!-- Compiled and minified JavaScript -->
	<script src="https://cdnjs.cloudflare.com/ajax/libs/materialize/1.0.0/js/materialize.min.js"></script>
	</head>
	<body>
	  <nav>
	    <div class="nav-wrapper">
	      <a href="#" class="brand-logo">Logo</a>
	      <ul id="nav-mobile" class="right hide-on-med-and-down">
	        <li><a href="/">Home</a></li>
	        <li><a href="/register">Register</a></li>
	        <li><a href="/login">Login</a></li>
	      </ul>
	    </div>
	  </nav>
	  {% block content%}
	  {% endblock %}
	</body>
	<script src="{% static 'tinymce/js/prism.js'%}"></script>f
	```
Search google: [htmlcolorcodes.com](https://htmlcolorcodes.com/)

	+ mysite -> main -> static -> main -> css -> materialize.css

	> File materialize.css làm theo Link dưới

**[Link tham khảo](https://www.youtube.com/watch?v=a3d_nyccpM8&list=PLQVvvaa0QuDe9nqlirjacLkBYdgc2inh3&index=5)**

<a name="I_06"></a>

- #### [1.6 User Registration - Django Web Development with Python](#I_06)

	+ mysite -> main -> templates -> main -> register.html

	```html
	{% extends "main/header.html" %}
	{% block content %}
		<from method="POST">
			{% csrf_token %}
			{{form.as_p}}
			<button class="btn" style="background-color: yellow; color: blue" type="submit">register</button>
		</from>
		If you already Have an Account, <a href="/login"><strong>Login</strong></a> instead.
	{% endblock %}
	```

	+ mysite -> main -> views.py

	```python
	from django.shortcuts import render, redirect
	from django.http import HttpResponse
	from .models import Tutorial
	from django.contrib.auth.forms import UserCreationForm
	from django.contrib.auth import login, logout, authenticate
	def homepage(request):
		return render(request=request,
			template_name="main/home.html",
			context={"tutorials": Tutorial.objects.all})
	def register(request):
		if request.method=="POST":
			form=UserCreationForm(request.POST)
			if form.is_valid():
				user = form.save()
				return redirect("main:homepage")
			else:
				for msg in form.error_message:
					print(form.error_messages[msg])
		form = UserCreationForm
		return render(request,
			"main/register.html",
			{"form":form})
	```

	+ mysite -> main -> urls.py

	```python
	from django.urls import path
	from . import views
	app_name = "main"
	urlpatterns = [
		path('', views.homepage, name="homepage"),
		path("register", views.register, name="register")
	]
	```

**[Link tham khảo](https://www.youtube.com/watch?v=riXD5lSInJ4&list=PLQVvvaa0QuDe9nqlirjacLkBYdgc2inh3&index=6)**

<a name="I_07"></a>

- #### [1.7 Messages and Include - Django Web Development with Python](#I_07)

	+ mysite -> main -> views.py

	```python3
	from django.shortcuts import render, redirect
	from django.http import HttpResponse
	from .modes import Tutorial
	from django.contrib.auth.forms import UserCreationForm
	from django.contrib.auth import login, logout, authenticate
	from django.contrib import messages
	def homepage(request):
		return render(	request=request,
						template_name="main/home.html",
						context={"tutorials": Tutorial.objects.all})
	def register(request):
		if request.method == "POST":
			form = UserCreationForm(request.POST)
			if form.is_valid():
				user = form.save()
				username = form.cleaned_data.get('username')
				messages.success(request, f"New Account Create: {username}")
				login(request, user)
				messages.info(request, f"You are now logged in as {username}")
				return redirect("main:homepage")
			else:
				for msg in form.error_messages:
					messages.error(request, f"{msg}: {form.error_messages[msg]}")
		form = UserCreationForm
		return render(	request=request,
						template_name="main/register.html",
						context={"form": form})
	```

	+ mysite -> main -> templates -> main -> header.html

	```html
	<head>
		{% load static %}
		<link href="{% static 'tinymce/css/prism.css'%}" rel="stylesheet">
		<link rel="stylesheet" href="{% static 'main/css/materialize.css'%}">
		<script src="https://cdnjs.cloudflare.com/ajax/libs/materialize/1.0.0/js/materialize.min.js">
	</head>
	<body>
		{% include "main/includes/navbar.html"%}
		{% include "main/includes/messages.html"%}
		<div class="container">
			{% block content %}
			{% endblock %}
		</div>
	</body>
	<script src="{% static 'tinymce/js/prism.js'%}"></script>
	```

	+ mysite -> main -> templates -> main -> includes -> navbar.html

	```html
	<nav>
		<div class="nav-wrapper">
			<a href="#" class="brand-logo">Logo</a>
			<ul id="nav-mobile" class="right hide-on-med-and-down">
				<li><a href="/">Home</a></li>
				{% if user.is_authenticated %}
					<li><a href="/account">{{user.username}}</a></li>
					<li><a href="/logout">Logout</a></li>
				{% else %}
					<li><a href="/register">Register</a></li>
					<li><a href="/login">Login</a></li>
				{% endif %}
			</ul>
		</div>
	</nav>
	```
	+ mysite -> main -> templates -> main -> includes -> messages.html

	```html
	{% if messages %}
		{% for message in messages %}
			{% if message.tags == 'success' %}
				<script>M.toast({html: "{{message}}", classes: "green rounded", displayLength:2000})</script>
				{% elif message.tags == 'info'%}
				<script>M.toast({html: "{{message}}", classes: "blue rounded", displayLength:2000})</script>
				{% elif message.tags == 'warning'%}
				<script>M.toast({html: "{{message}}", classes: "orange rounded", displayLength:10000})</script>
				{% elif message.tags == 'error'%}
				<script>M.toast({html: "{{message}}", classes: "red rounded", displayLength:10000})</script>
			{% endif %}
		{% endfor%}
	{% endif %}
	```
**[Link tham khảo](https://www.youtube.com/watch?v=0VGJPg0SQIY&list=PLQVvvaa0QuDe9nqlirjacLkBYdgc2inh3&index=7)**

<a name="I_08"></a>

- #### [1.8 User Login and Logout - Django Web Development with Python](#I_08)

	+ mysite -> main -> urls.py

	```python
	from django.urls import path
	from . import views
	app_name = "main"
	urlpatterns=[
		path('',views.homepage, name="homepage"),
		path("register", views.register, name="register"),
		path("logout", views.logout_request, name="logout"),
		path("login", views.login_request, name="login")
	]
	```

	+ mysite -> main -> views.py

	```python
	from django.shortcuts import render, redirect
	from django.http import HttpResponse
	from .modes import Tutorial
	from django.contrib.auth.forms import AuthenticationForm
	from django.contrib.auth import login, logout, authenticate
	from django.contrib import message
	form .forms import NewUserForm
	def homepage(request):
		return render(request=request,
			template_name="main/home.html",
			context={"tutorial": Tutorial.objects.all})
	def register(request):
		if request.method == "POST":
			form = NewUserForm(request.POST)
			if form.is_valid():
				user = form.save()
				username = form.cleaned_data.get("username")
				message.success(request, f"New Account Create: {username}")
				login(request, user)
				messages.info(request, f"You are now logged in as {username}")
				return redirect("main:homepage")
			else:
				for msg in form.error_messages:
					messages.error(request, f"{msg}: {form.error_messages[msg]}")
		form = NewUserForm
		return render(request=request,
			template_name="main/register.html",
			context={"form":form})
	def logout_request(request):
		logout(request)
		message.info(request, "Logged out successfully !")
		return redirect("main:homepage")
	def login_request(request):
		if request.method == "POST":
			form = AuthenticationForm(request, data=request.POST)
			if form.is_valid():
				username = form.cleaned_data.get('username')
				username = form.cleaned_data.get('password')
				user = authenticate(username=usernam, password=password)
				if user is not None:
					login(request, user)
					messages.info(request, f"You are now logged in as {username}")
					return redirect("main:homepage")
				else:
					message.error(request, "Invalid username or password")
		form = AuthenticationForm()
		return render(request,
			"main/login.html",
			{"form":form})
	```

	+ mysite -> main -> templates -> main -> login.html

	```html
	{% extends "main/header.html" %}
	{% block content %}
		<form method="POST">
			{% csrf_token %}
			{{form.as_p}}
			<button class="btn" style="background-color: yellow; color: blue" type="submit">login</button>
		</form>
		If you don't already Have an Accout, <a href="/login"><strong>register</strong></a> for one.
	{% endblock %}
	```

	+ mysite -> main -> forms.py

	```python
	form django import forms
	form django.contrib.auth.forms import UserCreationForm
	form django.contrib.auth.models import User
	class NewUserForm(UserCreationForm):
		email = forms.EmailField(request=True)
		class Meta:
			model = User
			fields = ("username", "email", "password1", "password2")
		def save(self, commit=True):
			user = super(NewUserForm, self).save(comm=Flase)
			user.email = self.cleaned_data['email']
			if commit:
				user.save()
			return user
	```
**[Link tham khảo](https://www.youtube.com/watch?v=79A1YoQ5ZJc&list=PLQVvvaa0QuDe9nqlirjacLkBYdgc2inh3&index=8)**

<a name="I_09"></a>

- #### [1.9 Linking models with Foreign Keys - Django Web Development with Python p.9](#I_09)

	+ mysite -> main -> models.py

	```python
	from django.db import models
	from django.utils import timezone
	class TutorialCategory(models.Model):
		tutorial_category = models.CharField(max_length=200)
		category_summary = models.CharField(max_length=200)
		category_slug = models.CharField(max_length=200)
		class Meta:
			verbose_name_plural = "Categories"
		def __str__(self):
			return self.tutorial_category
	class TutorialSeries(models.Model):
		tutorial_series = models.CharField(max_length=200)
		tutorial_category = models.ForeignKey(TutorialCategory, default=1, verbose_name="Category", on_delete=models.SET_DEFAULT)
		series_summary = models.CharField(max_length=200)
		class Meta:
			verbose_name_plural = "Series"
		def __str__(self):
			return self.tutorial_series
	class Tutorial(models.Model):
		tutorial_title = models.CharField(max_length=200)
		tutorial_content = models.TextField()
		tutorial_published = models.DateTimeField("date published", default=timezone.now())
		tutorial_series = models.ForeignKey(TutorialSeries, default=1, verbose_name="Series", on_delete=models.SET_DEFAULT)
		def __str__(self):
			return self.tutorial_title
	```

	> Chạy hai lệnh sau trong shell Django để cập nhật lại Model

	```
	python manage.py makemigrations
	python manage.py migrate
	```

	+ mysite -> main -> admin

	```python
	from django.contrib import admin
	from .models import Tutorial, TutorialSeries, TutorialCategory
	from tinymce.widgets import TinyMCE
	from django.db import models
	class TutorialAdmin(admin.ModelAdmin):
		fieldsets=[
				("Title/date",{"fields":["tutorial_title","tutorial_published"]}),
				("URL",{"fields":["tutorial_slug"]}),
				("Series",{"fields":["tutorial_series"]}),
				("Content",{"fields":["tutorial_content"]})
			]
		formfield_overrides={
			models.TextField:{"widget":TinyMCE()}
		}
	admin.site.register(TutorialSeries)
	admin.site.register(TutorialCategory)
	admin.site.register(Tutorial,TutorialAdmin)
	```

**[Link tham khảo](https://www.youtube.com/watch?v=Rju5qdU0e58&list=PLQVvvaa0QuDe9nqlirjacLkBYdgc2inh3&index=9)**

<a name="I_10"></a>

- #### [1.10 Working with Foreign Key - Django Web Development with Python p.10](#I_10)

	+ mysite -> main -> views.py

	```python
	from django.shortcuts import render, redirect
	from django.http import HttpRespone
	from .models import Tutorial, TutorialCategory, TutorialSeries
	from django.contrib.auth.forms import AuthenticationForm
	from django.contrib.auth import login, logout, authenticate
	from django.contrib import messages
	from .forms import NewUserForm
	def single_slug(request, single_slug):
		categories = [c.category_slug for c in TutorialCategory.objects.all()]
		if single_slug in categories:
			matching_series = TutorialSeries.object.filter(tutorial_category__category_slug=single_slug)
			series_urls={}
			for m in matching_series.all():
				part_one = Tutorial.objects.filter(tutorial_series__tutorial_series=m.tutorial_series).earliest("tutorial_published")
				series_urlsp[m]=part_one.tutorial_slug
			return render(	request,
							"main/category.html",
							{"part_ones": series_urls})
		tutorials = [t.tutorial_slug for t in Tutorial.objects.all()]
		if single_slug in tutorials:
			return HttpResponse(f"{single_slug} is a tutorial !!!")
		return HttpResponse(f"{single_slug} dose not correspind to anything.")
	def homepage(request):
		return render(	request=request,
						template_name="main/categories.html",
						context={"categories": TutorialCategory.objects.all()})
	def register(request):
		if request.method == "POST":
			form = NewUserForm(request.POST)
			if form.is_valid():
				user = form.save()
				username = form.cleaned_data.get("username")
				messages.success(request, f"New Account Create: {username}")
				login(request, user)
				messages.info(request, f"You are now logged in as {username}")
				return redirect("main:homepage")
			else:
				for msg in form.error_messages:
					messages.error(request, f"{msg}: {from.error_messages[msg]}")
		form = NewUserForm
		return render(	request=request,
						template_name="main/register.html",
						context={"form": form})
	def logout_request(request):
		loggout(request)
		message.info(request, "Logged out successfully !!!")
		return redirect("main:homepage")
	def login_request(request):
		if request.method == "POST":
			form = AuthenticationForm(request, data=request.POST)
			if form.is_valid():
				username = form.cleaned_data.get("username")
				password = form.cleaned_data.get("password")
				user = authenticate(username=username, password=password)
				if user is not None:
					login(request, user)
					messages.info(request, f"You are now logged in as {username}")
					return redirect("main:homepage")
				else:
					message.error(request, "Invalid username or password")
			else:
				message.error(request, "Invalid username or password")
		form = AuthenticationForm()
		return render(	request,
						"main/login.html",
						{"form": form})
	```

	+ mysite -> main -> urls.py

	```python
	from django.urls import path
	from . import views
	app_name = "main"
	urlpatterns = [
		path('', views.homepage, name="homepage"),
		path("register", views.register, name="register"),
		path("logout", views.logout_request, name="logout"),
		path("login", views.login_request, name="login"),
		path("<single_slug>", views.single_slug, name="single_slug")
		]
	```

	+ mysite -> main -> templates -> main -> categories.html

	```html
	{% extends "main/header.html"%}
	{% block content %}
		<div class="row">
			{% for cat in categories %}
				<div class="col s12 m6 14">
					<a href="{{cat.category_slug}}", style="color: #000">
						<div class="card hoverable">
							<div class="card-content">
								<div class="card-title">{{cat.tutorial_category}}</div>
								<p>{{cat.category_summary}}</p>
							</div>
						</div>
					</a>
				</div>
			{% endfor %}
		</div>
	{% endblock %}
	```

	+ mysite -> main -> templates -> main -> category.html

	```html
	{% extends 'main/header.html' %}
	{% block content %}
		<div class="row">
			{% for tut, partone in part_ones.items%}
				<div class="col s12 m6 14">
					<a href="{{partone}}", style="color:#000">
						<div class="card hoverable">
							<div class="card-content">
								<div class="card-title">{{tut.tutorial_series}}</div>
								<p>{{tut.series_summary}}</p>
							</div>
						</div>
					</a>
				</div>
			{% endfor %}
		</div>
	{% endblock %}
	```

**[Link tham khảo](https://www.youtube.com/watch?v=NqHX4eF2tw8&list=PLQVvvaa0QuDe9nqlirjacLkBYdgc2inh3&index=10)**

<a name="I_11"></a>

- #### [1.11 Dynamic sidebar - Django Web Development with Python P.11](#I_11)

	+ mysite -> main -> views.py

	```python
	from django.shortcuts import render, redirect
	form django.http import HttpResponse
	from .models import Tutorial, TutorialCategory, TutorialSeries
	from django.contrib.auth.forms import AuthenticationForm
	from django.contrib.auth import login, logout, authenticate
	from django.contrib import messages
	from .forms import NewUserForm
	def single_slug(request, single_slug):
		categories = [c.category_slug for c in TutorialCategory.objects.all()]
		if single_slug in categories:
			matching_series = TutorialSeries.object.filter(tutorial_category__category_slug=single_slug)
			series_urls={}
			for m in matching_series.all():
				part_one = Tutorial.objects.filter(tutorial_series__tutorial_series=m.tutorial_series).earliest("tutorial_published")
				series_urls[m]=part_one.tutorial_slug
			return render(	request,
							"main/category.html",
							{"part_ones": series_urls})
		tutorials = [t.tutorial_slug for t in Tutorial.objects.all()]
		if single_slug in tutorials:
			this_tutorial = Tutorial.objects.get(tutorial_slug = single_slug)
			tutorial_from_series = Tutorial.objects.filter(tutorial_series__tutorial_series=this_tutorial.tutorial_series).order_by("tutorial_published")
			this_tutorial_idx = list(tutorial_from_series).index(this_tutorial)
			return render(	request,
							"main/tutorial.html",
							{"tutorial":this_tutorial,
							"sidebar":tutorial_from_series,
							"this_tutorial_idx":this_tutorial_idx})
		return HttpResponse(f"{single_slug} does not correspond to anything.")
	def homepage(request):
		return render(	request=request,
						template_name="main/categories.html",
						context={"categories": TutorialCategory.objects.all()})
	def register(request):
		if request.method == "POST"
			form = NewUserForm(request.POST)
			if form.is_valid():
				user = form.save()
				username = form.cleaned_data.get('username')
				message.success(request, f"New Account Create: {username}")
				login(request, user)
				messages.info(request, f"You are now logged in as {username}")
				return redirect("main:homepage")
			else:
				for msg in form.error_messages:
					message.error(request, f"{msg}: {form.error_messages[msg]}")
		form = NewUserForm
		return render(	request=request,
						template_name="main/register.html",
						context={"form":form})
	def logout_request(request):
		logout(request)
		messages.info(request, "Logged out successfully !")
		return redirect("main:homepage")
	def login_request(request):
		if request.method == "POST":
			form = AuthenticationForm(request, data=request.POST)
			if form.is_valid():
				username = form.cleaned_data.get('username')
				password = form.cleaned_data.get('password')
				user = authenticate(username=username, password=password)
				if user is not None:
					login(request, user)
					messages.info(request, f"Yout are now logged in as {username}")
					return redirect("main:homepage")
				else:
					messages.error(request, "Invalid username or password")
			else:
				messages.error(request, "Invalid username or password")
		form = AuthenticationForm()
		return render(	request,
						"main/login.html",
						{"form":form})
	```

	+ mysite -> main -> templates -> main -> tutorial.html

	```html
	{% extends 'main/header.html' %}
	{% block content %}
		<div class="row">
			<div class="col s12, m8, 18">
				<h3>{{tutorial.tutorial_title}}</h3>
				<p style="font-size:70%">Published {{tutorial.tutorial_published}}</p>
				{{tutorial.tutorial_content|safe}}
			</div>
			<div class="col s12 m4 14">
				<ul class="collapsible popout">
					{% for tutorial in sidebar %}
						{% if forloop.counter0 == this_tutorial_idx %}
							<li class="active">
								<div class="collapsible-header">
								{{tutorial.tutorial_title}}<br>(currently viewing)</div>
							</li>
						{% else %}
							<li>
								<div class="collapsible-header">{{tutorial.tutorial_title}}</div>
								<div class="collpasible-body">
									<p><a href="/{{tutorial.tutorial_slug}}"><button class="btn waves-effect waves-light right-align" style="background-color:yellow;color: black>Go</button></a></p>
								</div>
							</li>
						{% endif %}
					{% endfor %}
				<ul>
			</div>
		</div>
	{% endblock %}
	```

	+ mysite -> main -> templates -> main -> header.html

	```html
	<head>
		{% load static %}
		<link href="{% static 'tinymce/css/prism.css' %}" rel="stylesheet">
		<link rel="stylesheet" href="{% static 'main/css/materialize.css' %}">
		<script src="https://cdnjs.cloudfare.com/ajax/libs/materialize/1.0.0/js/materialize.min.js"></script>
	</head
	<body>
		{% include "main/includes/navbar.html" %}
		{% include "main/includes/messages.html" %}
		<div class="container">
			{% block content %}
			{% endblock %}
		</div>
	</body>
	<script src="{% static 'tinymce/js/prism.js' %}"></script>
	<script>M.AutoInit();</script>
	```

**[Link tham khảo](https://www.youtube.com/watch?v=ZSzGIXYuE1I&list=PLQVvvaa0QuDe9nqlirjacLkBYdgc2inh3&index=11)**

<a name="I_12"></a>

- #### [1.12 Deploying Django to a server - Django Web Development with Python P.12](#I_12)

**[Link tham khảo](https://www.youtube.com/watch?v=4FLb1ulb64o&list=PLQVvvaa0QuDe9nqlirjacLkBYdgc2inh3&index=12)**