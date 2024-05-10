# MATEC
A project for some government entity.


## Startup Guide

1. Clone this repository
2. Make a virtual enviroment and install the packages listed in `requirements.txt`
3. Open the console and use the virtual enviroment
4. Migrate the change through the console.
```
python MATEC/MATECSERVER/manage.py migrate
```
5. Create a super user account
```
python MATEC/MATECSERVER/manage.py createsuperuser
```
6. Run the server
```
python MATEC/MATECSERVER/manage.py runserver
```
