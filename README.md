# PROJECT GOALS
This is the fourth project under the Code Institute Diploma in Software Development  program. This website is for a fictional gym called CrossFit - where the tough prevail. It is designed to be a website where members of this gym can sign up for CrossFit workout classes.

# UX

User stories
First time visitor goals

As a first time visitor, I want:

* to easily understand the main purpose of the site,
* to be able to easily navigate through the site,
* to be able to register a user account to access all content without restrictions,
* to be able to reserve a day and time for a class, view my bookings and delete my bookings,
* to be able to log out of my user account.

Returning and frequent user goals

As a returning user, I want:

* to sign into my user account,
* to make a booking for a class on a certain day and time,
* to view my bookings,
* to delete my bookings,
* to sign out of my account

Site Administrator goals
* As a Site Administrator I would like to be able to create the workout sessions which users can book

# Agile Tools

The Projects section in GitHub was used for this project. A Kanban board was used for the development of this project, which made it possible to break down the project into subtasks and make it easier to complete and track project progress.

# Design and Structure

The layout and design of this site was kept basic and simple. Miminal color was used to keep it simple. User are booking workout sessions and therefore this website is meant to be functional.  

# Functional Structure
Home page: The home page contains a navigation menu, logo, and an image that gives the user an idea of what the website is about. Here users are given basic information about the class scheduled offered, and a brief explanation of the different sessions that are offered - WOD, Endurance, & Basic. Each section also has a icon for it. There is an image in the background of this part, which is kept dark, as not to take away fromt he important information given. The background image is of a box jump, something that they will expect to do in their classes.

Registration page: The user must create an account to make a booking. To do this,they are asked to fill out a form on the page with the required fields: username and password. There is also an optional email field.

Login page: A username and password are required to log in existing users. Once signed in, they are directed to the home page.

Logout page: Logging out of the account is done through the menu, after which the user is redirected to the logout page where he must confirm his desire to log out of the account. After a successful logout, the user is returned to the home page.

Bookings page: The page  is only available to authenticated users and displays the classes/sessions offered. It is displayed in a calendar and each day these are 4 workout sessions/classes to do choose from. For each sessions a title of the workout is given, as well as the day, time, and instructor. A user cannot access this page unless they are registered and logged in.

My Bookings page: Only authenticated users have access to this page. On this page displays all the user's bookings.It provides the user with information for each session booked: title, day, time, & instructor. There's an option to delete each booking. When clicked the user is brought to a new page in which the user needs to confirm if they want to delete the booking or can choose to return to My Bookings page. After deleting the user is returned to the My Bookings page. The user is informed if they have no bookings too.

# Wire Frames

The wireframes were used to create the basic layout of the project. The wireframes can be seen below:

# Navigation Bar

The navigation bar is present on all pages of the site. The nav bar as different sections: Home, Bookings, My Bookings, Registration and Login/Logout. Also, the navigation bar is an adaptive element, and on mobile screens it collapses into a hamburger icon.

Navigation for an unauthorized user:

Navigation for an authorized user - registration disappears:

Registration Page:

Sign-In Page:

Log Out Page:

Bookings Page:

My Bookings Page:

Booking Successful:

Booking Aleady Made Page: 

Delete Booking Page:

No Bookings

# Responsive Design

The site has been designed to be responsive and adapted for desktop and mobile use. The project has been tested using a multi-device emulator with different screen sizes in the Google Chrome Developer Dashboard.

# Future Features

* page with information about the instructors
* ability to have 10 attendee max for each session and inform the user that the session is full
* Create a user profile which the user can view 

# Technology Used:

## Languages:

* Python
* JavaScript
* HTML5
* CSS3

## Frameworks, Libraries, Programs:

* Django: python framework used to create all the backend

## Databse:
* PostgreSQL: the database used to store all the data.

## Programs and Tools

* [Google Fonts](https://fonts.google.com/): Was used to to incorporate font styles
* [Font Awesome](https://fontawesome.com/): was used to create the icons used on the website
* [Bootstrap](https://getbootstrap.com/): Was used to create the front-end design
* [Gitpod](https://gitpod.io/workspaces): Gitpod was used as IDE to commit and push the project to GitHub, though I started with Codeanywhere, but most of it was in Gitpod
* [GitHub](https://github.com/): Was used to store my code
* [Am I Responsive](https://ui.dev/amiresponsive): to generate an image showcasing the website's responsiveness to different screen sizes
* [Pip3](https://pypi.org/project/pip/): to install Python modules and libraries
* [Gunicorn](https://docs.djangoproject.com/en/4.1/howto/deployment/wsgi/gunicorn/): "Green Unicorn" is a Python Web Server Gateway to translate HTTP Requests for Python to understand
* [Spycopg2](https://pypi.org/project/psycopg2/): PostgreSQL database adapter so I can manage the Database in Python
* [Cloudinary](https://cloudinary.com/): the image hosting service used to upload images and other media
* [Heroku](https://dashboard.heroku.com/apps): the hosting service used to host the website
* [VSCode](hhttps://code.visualstudio.com/): the IDE used to develop the website
* [Chrome Developer Tools](https://developer.chrome.com/docs/devtools/open/): was used to debug the website
* [W3C Validator](https://validator.w3.org/): was used to validate HTML5 code for the website
* [W3C CSS validator](https://jigsaw.w3.org/css-validator/): was used to validate CSS code for the website
* [Github Projects](https://github.com/) and Kanban board was used to track the progress of the project in general and of every application in the project

# Testing

## Bugs

###
No known bugs remaining

# Manual Testing

The Project was tested using a multi-device emulator with different display sizes in the Google Chrome Developer Dashboard. The following devices have been tested:

Nest HubMax (Desktop)
iPad Pro (Tablet)
iPad Air (Tablet)
iPad Mini (Tablet)
Galaxy Tab S4 (Tablet)
Nexus 7 (Mobile)
Nokia N9 (Mobile)
iPhone 5/SE (Mobile)
iPhone 4 (Mobile)


### Browser Testing

Testing has been carried out on the following browsers:

* Google Chrome
* Firefox
* Safari


