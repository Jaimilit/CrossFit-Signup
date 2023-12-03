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
![nav bar](./assets/features/nav-bar.png)

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

Footer

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

The site was constantly tested during the process of creating the site in the Gitpod Environment and the deployed site on Heroku was also tested in terms of user experience. The available functionality and user experience is reflected in the table below.

| Golas and Actions | As a Guest | As a User | Comment |
| -------- | -------- |  -------- | -------- |
| I can use menu and navigating through pages   | X | X | Click on items
| I can see the Home Page   | X | X | Click on items
| I can see the Registration Page  | X | X | Click on items and this disapears from the nav bar once registered
| I can see the Bookings Page |   | X | Need to be authorized to see
| I can see the My Bookings page  |  | X | Need to be authorized to see
| I can see the Sign Up Page | X | X | Click on items
| I can see the Login/Logout Pages | X | X | You see one or the other depending on if you are logged in or logged out
| I can complete the registration form  | X | X | Click on items
| I can complete the Sign In form  | X | X | Click on items
| I can complete make a booking for a particular session/class |  | X | Need to be authorized to do
| I can complete delete a particular session/class |   | X | Need to be authorized to do
| I can see if I have made a booking successfully  |   | X | Need to be authorized to do
| I can see if I have already made a booking for a session  |  | X | Need to be authorized to do

# HTML Validation

HTML Validation:
The W3C Markup Validation Service was used to validate the HTML of the website. There were errors and warnings in the reports about unclosed elements and tags, incorrect values ​​and types of elements, unnecessary trailing slashes. All errors and warnings have been fixed, the project's HTML code has been re-checked without errors.

Home page
Base
Bookings page
My Bookings
Sign Up page
Login page
Logout page
Delete booking page
Already booked page
Booking Success




# CSS Validation:
The website CSS style has successfully passed the W3C Jigsaw CSS Validation Service.

### Python Validation (PEP8)
All Python code was manually checked using CI Python Linter. The Linter reports had messages about exceeding the string length of 79 characters, which have been fixed. Re-testing did not reveal any errors.

* urls.py
* models.py
* forms.py
* views.py
*

# Deployment
The project was first created in GitHub, then using the workspace in CodeAnywhere, and then in Gitpod. The project code is stored on GitHub, and then deployed to Heroku. To deploy, follow these steps:

1. Log in to Heroku or create an account, if required. On the Welcome page in the top right corner click the button labeled 'New'.

2. From the drop-down menu select 'Create new app'. Enter a preferred app name. Select the relevant geographical region. Click to 'Create App'.

3. Navigate to 'Settings' and scroll down to the 'Config Vars' section. Click 'Reveal Config Vars' and enter 'PORT' for the key and '8000' for the value. Then click 'Add'. Add CLOUDINARY_URL, DATABASE_URL and SECRET_KEY. URL variable values ​​must be copied from your CLOUDINARY account and ElephantSQL account. To create a SECRET KEY, use the online service or come up with your own.

4. Click on the 'Deploy' tab. Next to 'Deployment method' select 'GitHub'. Connect the relevant GitHub repository. Under 'Manual deploy' choose the correct branch and click 'Deploy Branch'. Also you can select 'Automatic Deploys' so that the site updates when updates are pushed to GitHub.

5. After successful deployment message in the page top right corner click the button labeled 'Open app' and you can access live app.


# Credits

## Code
The structure and the code of the project was based on two walkthroughs by the Code Institute:

Hello Django - I created CRUD functionalities based on the examples of this walkthrough.
From I think therefore I blog - I used the main layout/structure of what they did. However, I altered it as it is not a blog. 

## Content

Information is fictional and created by me and I was inspired by my own CrossFit box. 
[CrossFit Fabriken](https://www.cf-fabriken.com/) This is my CrossFit box and my inspiration for this project. Though this information is in Swedish. They use an app called [Wonder](https://wondr.cc/en-gb/home) in which members book their own CrossFit sessions for the week.

## Media

The one image was free to use from Pexels.

## Inspiration

This project was inspired by the Hello Django project and the I Think Therefore I Blog project.
 Larisa LG's Readme.md file was used as a template for writing Readme.md.
 CrossFit Fabriken website and Wondr App.




