from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.views.decorators.http import require_POST
from .forms import UserForm,blogForm
from .models import userDetails,blogs_post


def login(request):
 user_list = userDetails.objects.order_by('id')
 blog_list= blogs_post.objects.order_by('id')
 form = UserForm()
 context = {'user_list' : user_list, 'form' : form, 'blog_list':blog_list}
 return render(request, 'login.html', context)
 
def displaySignup(request):
 form = UserForm()
 context = {'form' : form}
 return render(request, 'displaySignup.html', context)

@require_POST
def loginSuccess(request):
 user_list = userDetails.objects.order_by('id')
 form = UserForm(request.POST)
 context={}
 for ul in user_list:
  if ul.userName == request.POST['userName']:
   if ul.password == request.POST['password']:
    return render(request, 'blogs.html', context)
   else:
    continue
 
 return redirect('login')

@require_POST
def addTodo(request):
 form = UserForm(request.POST)
 pwd = request.POST.get('pwd')
 print (pwd)
 if pwd != request.POST['password']:
  print("This is wrong")
  return redirect('displaySignup')
 context={}
 if form.is_valid():
  new_todo = userDetails(userName=request.POST['userName'], password=request.POST['password'])
  new_todo.save()
  return render(request, 'blogs.html', context)

def addBlog(request):
 blog = blogs_post.objects.order_by('id')
 form = blogForm()
 context = {'blog' : blog, 'form' : form}
 return render(request, 'blogs.html', context)

@require_POST
def submitBlog(request):
 post = blogs_post.objects.order_by('id')
 #todo = userDetails.objects.get(pk=int(form[i]))
 form = blogForm(request.POST)
 context={'post':post, 'form':form}
 if form.is_valid():
  new_todo = blogs_post(title=request.POST['title'],text=request.POST['text'])
  new_todo.save()
 return render(request, 'blogs.html', context)

def displayBlog(request, bl_id):
 todo = blogs_post.objects.get(pk=bl_id)
 text_1=todo.text
 title=todo.title
 context={'text':text_1,'title':title}
 return render(request, 'display.html', context)
