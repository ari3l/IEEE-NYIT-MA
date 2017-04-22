# IEEE NYIT MA Chapter

## Official website build on Django

This is the website created for Institute of Electrical and Electronics Engineers at NYIT manhattan campus 
Website is build on Django, users are capable of adding events to the calendar 
Installation

## Activation of virtual environment:
```
source local/bin/activate
pip install -r /path/to/requirements.txt
```

Adding hosts: The website will only run in local host, in order to add a host go to /IEEE-NYIT-MA/mysite/settings.py and add a host
```
#/IEEE-NYIT-MA/mysite/settings.py
ALLOWED_HOSTS = ["127.0.0.1", ""]
```
## Configuring and running Django:
```
#creating a super user
./manage.py createsuperuser 
#creating a migration
./manage.py makemigrations
#run the server
./manage.py runserver
```
## Capabilities
-----------------------------------------
By going to the admin page (localhost/admin) and entering superuser login and password </br>
Admin can create events, posts, and access the db of signedup users </br>
Creation of the event:</br>
![alt tag](https://github.com/Denisolt/acm/blob/master/page2.png?raw=true)</br>
Creation of the blog post:</br>
![alt tag](https://github.com/Denisolt/acm/blob/master/page1.png?raw=true)</br>
Accessing the db of signed up users:</br>
![alt tag](https://github.com/Denisolt/acm/blob/master/page3.png?raw=true)</br>
