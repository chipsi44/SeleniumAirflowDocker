# Selenium, Airflow, Docker Tutorial. How to make them work together ?

__Airflow version : 2.5.1 | Tuto made in March 2023__

* Repository : SeleniumAirflowDocker
* Type of challenge : Learning
* Duration : 5 days
* Team challenge : Individual

# Mission objectives

* Learning the basics of Airflow
* Working with Selenium
* Working with Docker
* Ability to work with all three together

# Structure of the project

In the main branch, you'll find an incomplete tutorial that you'll need to complete on your own.

There is a 'Corrected_tuto' branch where you'll find the completed tutorial. However, if you get stuck at any point in the tutorial, feel free to switch to the 'Corrected_tuto' branch for assistance.

# How to 

In this part, I'm going to assume that you already have your scraping code and you're just looking for how to make the three technologies work together.

## __Selenium grid__

First of all, you need to install Docker Desktop. If you are a Windows user, do not forget to update your WSL.
"Now that you have Docker installed, the first objective is to see if you can access the Selenium Grid web interface. To do so, you'll need to pull the Selenium Grid image in Docker and launch it using the dedicated port. The command to do this is:
* docker pull selenium/standalone-firefox     
* docker run -p -d 4444:4444 selenium/standalone-firefox:latest  

You can now access the Selenium Grid on your local machine. I didn't encounter any problems accessing it, so I have no comments about debugging at this point. But you'll need to modify your scraping function a bit; your webdriver should now be a remote webdriver pointing towards the Selenium container on port 4444. If you want to see how it's done, you can check my function in the resource folder.

## __Docker network__

We are going to need to use a Docker network , which means we need to create it. :
* docker network create my-network 

Once it's created, stop your docker container with the selenium grid and relaunch it inside the network : 
* docker run -d --network my-network --name selenium-container -p 4444:4444 selenium/standalone-firefox:latest

The -d option (short for "detached mode") is used to run a Docker container in the background, without attaching to its console. This means that the container runs as a separate process and allows you to use the terminal without being blocked by the container's output.
You can now access the Selenium Grid on your local machine. I didn't encounter any problems accessing it, so I have no comments about debugging at this point.

## __Apache Airflow__

This is where things get a bit tricky. Once again, I'm going to assume that you already know how to create a DAG with your scraping function.
You'll need to create a Dockerfile to build a Docker image that will allow you to launch the Apache Airflow web interface in the same network as the Selenium Grid.

The specification of this Dockerfile are : 
* WORKDIR /app
* RUN airflow db init
* Launch three commands: one to run the Airflow scheduler, one to add the admin user, and the last one to run the Airflow web server
* * CMD ["sh", "-c", "airflow scheduler & airflow users  create --role Admin --username admin --email admin --firstname admin --lastname admin --password admin & airflow webserver"]

Once again, I'm going to assume that you know how to create a Dockerfile, and I'm just here to add the specification of Selenium for the Dockerfile. If you want more information about Dockerfile, you can check mine in this project.

It is now time to build and launch our DAG image:
* docker build -t my_airflow_container:latest .   
* docker run -d --network my-network --name monapp-container -p 8080:8080 my_airflow_container:latest

Run it on the port 8080 and do not forget to run it inside the network with selenium grid.

# Contributor 

[Cyril Verwimp](https://www.linkedin.com/in/cyril-verwimp-8a0457208/)

# Why making this project
As a data scientist, I found myself needing to work with these three major technologies quickly, and I realized that most of the tutorials were outdated. So, I decided to create my own tutorial, as we all know that it can be challenging to learn solely by going through official documentation.
# End
>“For the things we have to learn before we can do them, we learn by doing them.”
― Aristotle