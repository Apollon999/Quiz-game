# Mystery-Quiz Game
## Introduction
This is project number three out of five for Code Institute full-stack development program: Python Terminal.

The Mystery quiz is made in the Python terminal and runs in the Code Institute mock terminal Heroku. 
The Quiz will test the player's knowledge about some of the worlds mysteries!

[Live project here](https://quiz-python.herokuapp.com/)

## README Table content
* [Introduction](#introduction)
* [User Experience - UX](#user-experience-ux)
* [User Stories](#user-stories)
* [Features](#features)
* [Intro Message](#intro-message)
* [Game features](#game-features)
* [Technologies Used](#technologies-used)
* [Languages Used](#languages-used)
* [Python Packages](#python-packages)
* [Programs Used](#programs-used)
* [Testing](#testing)
* [Extendclass](#extendclass)
* [Lighthouse](#lighthouse)
* [Bugs and Issues](#bugs-and-issues)
* [Deployment](#deployment)
* [Credits](#credits)
* [Content](#content)
* [Resources](#resources)




## User Experience - UX

### User Stories
* With this app my goal is to:

1. Build a clean and easy app to use.
2. Build a game that is challenging for the player.

* As a new user i want to:

1. Being welcomed and understand what the game is.
2. Get knowledge of hom many points each question is worth.
3. Know how well i did in the quiz with score and time tracking functions.

## Features

### Intro Message
Welcomes user and informs them about the topic of the quiz.
After that user gets the question if they wish to start the game, if yes a timer is displayed to prepare the player.

### Game features 
* The quiz contains of 4 questions with 4 alteratives each.
* The last two questions is harder and are worth dubble points.
* The game displays correct or incorrect straight after answer.
* The game keeps track of users time and total score.
* The game makes sure that you put valid letters as answer.
* The game gives a possibillity to try again.

## Technologies Used 
### Languages Used
* Python

#### Python Packages 
* Time: Defined time sleep and total time.

## Programmes Used
* GitPod: Used to create and edit the app.
* GitHub: Used to store the code after being pushed from GitPod.
* Heroku: Used to deploy the live project!
* PEP8: was used to validate all the python code.

## Testing
#### https://extendsclass.com/python-tester.html
The extendclass validator makes sure there are no syntax errors in the python file and has been used throughout the project.
![Skärmbild 2023-05-10 005016](https://github.com/Apollon999/Quiz-game/assets/118939854/3e25e563-95b5-4e27-a80f-cfe18f264347)
#### Lighthouse
Lighthouse was used to test the app at all stages
![Skärmbild 2023-05-10 010730](https://github.com/Apollon999/Quiz-game/assets/118939854/bc9854b6-9299-4700-9b21-00645f3c6d8f)

## Bugs And Issues
* Invalid inputs would freeze the game
Solution: Gave an error message that explains what the user should input to proceed.
* The app would continue forever after quiz was finished
Solution: Gave the user a choice to restart the game or shut down.
* The code was unneccesarily long and hard to read
Solution: Divided the code into three smaller functions.

## Deploying This Project 
1. Log in to Heroku or create an account
2. On the main page click the button labelled New in the top right corner and from the drop-down menu select Create New App
3. You must enter a unique app name
4. Next select your region
5. Click on the Create App button
6. The next page is the project’s Deploy Tab. Click on the Settings Tab and scroll down to Config Vars
7. Click Reveal Config Vars and enter port into the Key box and 8000 into the Value box and click the Add button
8. Click Reveal Config Vars again and enter CREDS into the Key box and the Google credentials into the Value box
9. Next, scroll down to the Buildpack section click Add Buildpack select python and click Save Changes
10. Repeat step 8 to add node.js. o Note: The Buildpacks must be in the correct order. If not click and drag them to move into the correct order
11. Scroll to the top of the page and choose the Deploy tab
12. Select Github as the deployment method
13. Confirm you want to connect to GitHub
14. Search for the repository name and click the connect button
15. Scroll to the bottom of the deploy page and select the preferred deployment type
16. Click either Enable Automatic Deploys for automatic deployment when you push updates to Github

## Credits
### Content
* All the content in the game is original

### Resources 
* FreeCode Camp
* Medium.com
* Code Institute Learing platform


