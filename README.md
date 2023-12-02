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
