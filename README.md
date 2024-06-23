# MATEC
The web project for Barangay Bagna

## Startup Guide

1. Clone this repository
2. Make a virtual enviroment and install the packages listed in `requirements.txt`
3. Open the console and use the virtual enviroment
4. Migrate the change through the console.
```
python MATECSERVER/manage.py migrate
```
5. Create a super user account
```
python MATECSERVER/manage.py createsuperuser
```
6. Run the server
```
python MATECSERVER/manage.py runserver
```
