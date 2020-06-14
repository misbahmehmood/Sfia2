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
* [Improvements for the future](#Improvements)

# Introduction



For my application, I decided to create a randomly generated cartoon character and displayed either their catchphrase, species or the TV show they are a part of.

# The Brief


## Scope

# Project Tracking
# Tables
## Initial tables
A database was required in this project which could persist data. Instead of creating a mysql service through Docker and persisting it with the use of volumes, I created a database on the cloud due to being familiar with using databases on the cloud from previous projects and the scalability benefits the cloud provides. 

Below are the initial tables I planned out for the application using the MOSCOW principle to help me with keeping focus on what is important to include:

![](https://raw.githubusercontent.com/misbahmehmood/Sfia2/development/images/Initial%20tables-Page-1.jpg)

## Final table
![](https://raw.githubusercontent.com/misbahmehmood/Sfia2/development/images/Final%20table.jpg)

When the application was built and I understood how the database would incorprate within the microservices, I decided it was easier to merge the initial tables together in a single table. Instead of seperating the characters into Disney and Marvel, I included all cartoon characters. 

The name column would include their names, the profile type would be either their catchphrases, tv shows or species. Finally, the information column would include list their catchphrase, tv show or species depending on which profile type was generated in the third microservice. 

# Risk Assessment

# Deployment
![](https://raw.githubusercontent.com/misbahmehmood/Sfia2/development/images/CI%20Pipeline%20(1).jpg)

# Improvements