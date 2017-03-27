# IEEE NYIT MA Chapter
<h3> Official website build on Django </h3>
This is the website created by <a href="https://github.com/denisolt">Denisolt Shakhbulatov</a>
for Institute of Electrical and Electronics Engineers at NYIT manhattan campus <br/>
Website is build on Django, users are capable of adding events to the calendar <br/>

Installation
-----------------------------------------
Activation of virtual environment:
```
source local/bin/activate
pip install -r /path/to/requirements.txt
```
Configuring and running Django:
```
#creating a super user
./manage.py createsuperuser 
#creating a migration
./manage.py makemigrations
#run the server
./manage.py runserver
```
Capabilities
-----------------------------------------
By going to the admin page (localhost/admin) and entering superuser login and password </br>
Admin can create events, posts, and access the db of signedup users </br>
Creation of the event:</br>
![alt tag](https://github.com/Denisolt/acm/blob/master/page2.png?raw=true)</br>

