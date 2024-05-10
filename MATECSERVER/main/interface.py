from .models import *
from django.contrib.auth.models import Group

def register_user(username:str, first_name:str, last_name:str, password:str, phone:str, email:str = None):
    user = User.objects.create_user(username = username, email = email, password = password, first_name = first_name, last_name = last_name)
    group, created = Group.objects.get_or_create(name='User')
    user.groups.add(group)
    profile = User_Profile(user = user, phone = phone)
    profile.save()

def get_all_announcement(max_posts = 999):
    return Announcement.objects.order_by('-date_posted')[:max_posts]

def get_announcement(id):
    return Announcement.objects.get(id = id)

def delete_announcement(id):
    Announcement.objects.filter(id = id).delete()

def check_announcement_exists(id:int):
    return Announcement.objects.filter(id = id).exists()

def save_announcement(title, description, image, id = None):
    temp = None

    if id != None:
        temp = Announcement.objects.get(id = id)
        temp.title = title
        temp.description = description
        temp.thumbnail = image
        temp.save()

    else:
        temp = Announcement(
            title = title,
            description = description,
            thumbnail = image
        )
        temp.save()
        
    return temp

def get_all_project(max_posts = 999):
    return Project.objects.order_by('-date_posted')[:max_posts]

def get_project(id):
    return Project.objects.get(id = id)

def delete_project(id):
    Project.objects.filter(id = id).delete()

def check_announcement_exists(id:int):
    return Project.objects.filter(id = id).exists()

def save_project(title, description, image, id = None):
    temp = None
    
    if id != None:
        temp = Project.objects.get(id = id)
        temp.title = title
        temp.description = description
        temp.thumbnail = image
        temp.save()

    else:
        temp = Project(
            title = title,
            description = description,
            thumbnail = image
        )
        temp.save()
        
    return temp

def get_all_forms(pending = True):
    if pending:
        return Form.objects.filter(approval_status = "pending").order_by('-date_posted')
    else:
        return Form.objects.order_by('-date_posted')
        
def get_user_forms(user:User):
    return Form.objects.filter(user = user).order_by('-date_posted')

def get_form(id):
    return Form.objects.get(id = id)

def delete_form(id):
    Form.objects.filter(id = id).delete()

def check_form_exists(id:int):
    return Form.objects.filter(id = id).exists()

def change_approval_form(id:int, approval_status:str):
    temp = Form.objects.get(id = id)
    temp.approval_status = approval_status
    temp.save()


def save_form(user, type, file, id = None):
    temp = None
    
    if id != None:
        temp = Form.objects.get(id = id)
        temp.user = user
        temp.type = type
        temp.file = file
        temp.save()

    else:
        temp = Form(
            user = user,
            type = type,
            file = file
        )
        temp.save()
        
    return temp

