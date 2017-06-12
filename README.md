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
- Run the following command for building and start docker image & containers and run the project  
`docker-compose up --build`
- Now you can browse the application through http://127.0.0.1:8000

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
