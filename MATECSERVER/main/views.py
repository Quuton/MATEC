from django.shortcuts import render, redirect
from django.contrib import auth
from . import interface
MAIN_PATH = 'main/'
TEMPLATES = {
            'home':'index.html',
            'contact':'contact.html',
            'about':'about.html',
            'login':'login.html',
            'signup':'signup.html',
            'downloads':'downloads.html',
            'announcement':'announcement.html',
            'announcements':'announcements.html',
            'announcement_add_form':'announcement_add_form.html',
            'announcement_edit_form':'announcement_edit_form.html',
            'projects':'projects.html',
            'project':'project.html',
            'project_add_form':'project_add_form.html',
            'project_edit_form':'project_edit_form.html',
            'userforms':'userforms.html',
            'userform':'userform.html',
            'userform_add_form':'userform_add_form.html',
}

def home(request):
    return render(request, MAIN_PATH + TEMPLATES['home'])

def forbidden(request):
    return render(request, "forbidden")

def not_found(request):
    return render(request, "Not found 404 :(")

def login(request):
    if request.user.is_authenticated:
        return redirect('/')
    
    elif request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(request, username = username, password = password)

        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            return render(request, MAIN_PATH + TEMPLATES['login'], context = {'auth_status':'Credentials do not match any account!'})

    else:
        return render(request, MAIN_PATH + TEMPLATES['login'])

def logout(request):
    auth.logout(request)
    return redirect('/')

def signup(request):
    if request.user.is_authenticated:
        return redirect('/')
    else:
        if request.method == 'POST':
            username = request.POST['username']
            first_name = request.POST['first_name']
            last_name = request.POST['last_name']
            email = request.POST['email']   
            password = request.POST['password']
            phone = request.POST['phone']
            interface.register_user(username, first_name, last_name, password, phone, email)
            return redirect('/login/')
        else:
            return render(request, MAIN_PATH + TEMPLATES['signup'])

def get_announcement(request, id: int = None):
    context = {'announcement':interface.get_announcement(id)}
    return render(request, MAIN_PATH + TEMPLATES['announcement'], context = context)

def get_all_announcement(request):
    context = {'announcements':interface.get_all_announcement(10)}
    return render(request, MAIN_PATH + TEMPLATES['announcements'], context = context)

def delete_announcement(request, id: int = None):
    if not (request.user.is_superuser and request.user.is_authenticated):
        return redirect('/forbidden')

    if (request.method == "GET" and id != None):
        interface.delete_announcement(id)
        return redirect('/announcements')
    else:
        return redirect('/')

def add_announcement(request):
    if not (request.user.is_superuser and request.user.is_authenticated):
        return redirect('/forbidden')

    if (request.method == "POST"):
        title = request.POST['title']
        description = request.POST['description']

        image = None
        if request.FILES.get('thumbnail') != None:
            image = request.FILES.get('thumbnail')

        interface.save_announcement(title, description, image)
        return redirect('/announcements/')
    else:
        return render(request, MAIN_PATH + TEMPLATES['announcement_add_form'])
    
def edit_announcement(request, id:int):
    if not (request.user.is_superuser and request.user.is_authenticated):
        return redirect('/forbidden')
    
    if (id == None or not interface.check_announcement_exists(id)):
        return redirect('/not-found')
    
    temp_announcement = interface.get_announcement(id)

    if (request.method == "POST"):
        title = request.POST['title']
        description = request.POST['description']

        image = temp_announcement.thumbnail
        if request.FILES.get('thumbnail') != None:
            image = request.FILES.get('thumbnail')

        interface.save_announcement(title, description, image, id)
        return redirect(f'/get-announcement/{id}')
    else:
        context = {'announcement':interface.get_announcement(id),
                    'id':id
                }
        return render(request, MAIN_PATH + TEMPLATES['announcement_edit_form'], context = context)
    

def get_project(request, id: int = None):
    context = {'project':interface.get_project(id)}
    return render(request, MAIN_PATH + TEMPLATES['project'], context = context)

def get_all_project(request):
    context = {'projects':interface.get_all_project(10)}
    return render(request, MAIN_PATH + TEMPLATES['projects'], context = context)

def delete_project(request, id: int = None):
    if not (request.user.is_superuser and request.user.is_authenticated):
        return redirect('/forbidden')

    if (request.method == "GET" and id != None):
        interface.delete_project(id)
        return redirect('/projects')
    else:
        return redirect('/')

def add_project(request):
    if not (request.user.is_superuser and request.user.is_authenticated):
        return redirect('/forbidden')

    if (request.method == "POST"):
        title = request.POST['title']
        description = request.POST['description']
        location = request.POST['location']

        image = None
        if request.FILES.get('thumbnail') != None:
            image = request.FILES.get('thumbnail')

        interface.save_project(title, description, location, image)
        return redirect('/projects/')
    else:
        return render(request, MAIN_PATH + TEMPLATES['project_add_form'])
    
def edit_project(request, id:int):
    if not (request.user.is_superuser and request.user.is_authenticated):
        return redirect('/forbidden')
    
    if (id == None or not interface.check_project_exists(id)):
        return redirect('/not-found')
    
    temp_project = interface.get_project(id)

    if (request.method == "POST"):
        title = request.POST['title']
        description = request.POST['description']
        location = request.POST['location']

        image = temp_project.thumbnail
        if request.FILES.get('thumbnail') != None:
            image = request.FILES.get('thumbnail')

        interface.save_project(title, description, location, image, id)
        return redirect(f'/get-project/{id}')
    else:
        context = {'project':interface.get_project(id),
                    'id':id
                }
        return render(request, MAIN_PATH + TEMPLATES['project_edit_form'], context = context)
    

def get_userform(request, id: int = None):
    if not request.user.is_authenticated:
        return redirect('/forbidden')

    if not interface.check_form_exists(id):
        return redirect('/not-found')
    
    user_form = interface.get_form(id)

    if request.user.is_superuser or request.user == user_form.user:
        context = {'user_form':user_form}
        return render(request, MAIN_PATH + TEMPLATES['userform'], context = context)
    else:
        return redirect('/forbidden')

def delete_userform(request, id: int = None):
    if not (request.user.is_superuser and request.user.is_authenticated):
        return redirect('/forbidden')
    
    if not interface.check_form_exists(id):
        return redirect('/not-found')
    
    user_form = interface.get_form(id)

    if (request.method == "GET" and id != None and (request.user.is_superuser or request.user == user_form.user)):
        interface.delete_form(id)
        return redirect('/forms')
    else:
        return redirect('/')
    
def add_userform(request):
    if not (request.user.is_superuser and request.user.is_authenticated):
        return redirect('/forbidden')

    if (request.method == "POST"):
        type = request.POST['type']

        file = None
        if request.FILES.get('file') != None:
            file = request.FILES.get('file')

        interface.save_form(request.user, type, file)
        return redirect('/user-forms/')
    else:
        return render(request, MAIN_PATH + TEMPLATES['userform_add_form'])