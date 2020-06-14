# Sfia2 Project
# Contents
* [Introduction](#Introduction)
* [The Brief](#The-Brief)
    * [Scope](#Scope)
* [Technologies Used](#Technology-Used)
* [Project Tracking/Planning](#Project-Tracking)
    * [Initial Tracking Board](#Initial-Trello-board)
    * [Final Tracking Board](#Final-Trello-board)
    * [Tables](#Tables)
* [Risk Assessment](#Risk-Assessment)
* [Testing](#Testing)
* [Deployment](#Deployment)
    * [Version Control System](#Version-Control-System)
* [Improvements for the future](#Improvements)

# Introduction



For my application, I decided to create a randomly generated cartoon character and displayed either their catchphrase, species or the TV show they are a part of.

# The Brief


## Scope

# Project Tracking
A trello board was used for project management and tracking. Having already used trello for practise exercises during training, it was easy to use and simple to follow. The user stories were planned out first implementing the MoSCoW principle to keep the focus on the essential areas. Scrum framework was used with the sprint backlog, this was then explored further by adding specific tasks and sprints relating to the backlog.
## Initial Tracking Board
The MoSCoW prioritisation method is displayed through the use of labels. Everything on the board is a Must Have unless specifically mentioned otherwise. 
![](https://raw.githubusercontent.com/misbahmehmood/Sfia2/development/images/Initial%20Trello%20board.png)

## Final Tracking Board 
![](https://raw.githubusercontent.com/misbahmehmood/Sfia2/development/images/Final%20Trello%20Board.png)

# Tables
A database was required in this project which could persist data. Instead of creating a mysql service through Docker and persisting it with the use of volumes, I created a database on the cloud due to being familiar with using databases on the cloud from previous projects and the scalability benefits the cloud provides. 
## Initial tables
Below are the initial tables I planned out for the application using the MOSCOW principle to help me with keeping focus on what is important to include:

![](https://raw.githubusercontent.com/misbahmehmood/Sfia2/development/images/Initial%20tables-Page-1.jpg)

## Final table
![](https://raw.githubusercontent.com/misbahmehmood/Sfia2/development/images/Final%20table.jpg)

When the application was built and I understood how the database would incorporate within the microservices, I decided it was easier to merge the initial tables together in a single table. Instead of seperating the characters into Disney and Marvel, I included all cartoon characters. 

The name column would include their names, the profile type would be either their catchphrases, tv shows or species. Finally, the information column would list their catchphrase, tv show or species depending on which profile type was generated in the third microservice. 

# Risk Assessment
![](https://raw.githubusercontent.com/misbahmehmood/fundamental_project/images/images/Risk%20Assessment%20key.jpg)
![](https://raw.githubusercontent.com/misbahmehmood/Sfia2/development/images/Risk%20Assessment.png)
(Please click on the images to show a clearer view)

# Deployment
![](https://raw.githubusercontent.com/misbahmehmood/Sfia2/development/images/CI%20Pipeline%20(1).jpg)

## Version Control System
Most of my work was completed on the development branch. I added a docker branch when completing all the docker tasks and merged with the development branch once I was sure docker deployment was fully working. As I went on through the project, I continued adding branches and merged with development once I had working code after completing individual tasks/sprints in the trello board. 

I also made use of the issues option to record any issues faced during the application.

Overall I used 5 branches including an app branch when I decided to update the application and add more options to randomly generate.

# Improvements
