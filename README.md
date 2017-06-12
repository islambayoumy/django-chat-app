# Chat System
Simple one to one chatting web application developed using python [Django](https://www.djangoproject.com) framework.


### Application features
* RESTful api based
* Full authentication system
* User online/offline status view
* Docker image with all required dependencies  


## Getting Started

### Prerequisites
Following steps assume that you have installed  
1. [Docker](https://www.docker.com)  
2. [Docker Compose](https://docs.docker.com/compose)  

### Instruction for running the project

- Open terminal and change directory to whatever you want  
~ choosen driver must by shared with docker 
- Clone the project  
`git clone https://github.com/islambayoumy/django-chat-app`
- change directory to project folder  
`cd django-chat-app`
- List content of the project (not important!)  
`dir`  
-> you should see these output:  
`Assets`   
`chat_app`  
`Chat_System`  
`docker-compose.yml`  
`Dockerfile`  
`manage.py`  
`requirements.txt`  
- Run the following command for building and start docker image & containers and run the project  
`docker-compose up --build`
- Now you can browse the application through http://127.0.0.1:8000

##### ~ Project isn't ready for production environment yet

#### Using the application
1. Sign Up to create an account
2. Login with the created account (you are now online)  
~ for first time you will not see users list as you are the only user in the system
3. Open another browser (if you are using chrome, just open new incognito tab) and go to http://127.0.0.1:8000
4. Repeat 1, 2 & 3 as many as you want more accounts to be online
5. You can send messages to any user in the system either he/she is online or offline
6. If you have no activity, a refreshing rate = 7sec is done
7. For two or more users in the system: you can navigate between users, see previous messages and send new ones
8. Logout to go offline

## Attachments
### Attached with the project an 'Assets' folder containing UML Diagrams :  
- Class diagram
- Use-case diagram
- Flow-chart diagram

## Implementation
 - python3 & django for back-end restful api and auth system
 - jquery & ajax for front-end calls
 - html5, css3 & bootstrap3 for setting content and designing responsive style
 - postgres for db (switched through sqlite3 to mysql to postgres)
 
 ## Further improvements
 - Using a front-end framework to call back-end api (e.g Angular2 or React.js)
 - For project expantion, using nosql database (e.g Mongodb)
 - Trying to use django 'Sockets' and 'Channels' for a real-time massenger
 - Handle some ux/ui enhancements
