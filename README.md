# Gymstuff.com : Ecommerce Site

This project is a web-based e-commerce site which allows users to view gym products, supplements and vitamins to aid their fitness goals. The user can search products by name or by category. In addition to this, the user can input their current physical attirubutes and gain insights such as current body mass index; recommended daily calorie intake for a selected aim; and recommended daily macronutrient intake.
The user is required to register and log-in to access the physical attribute features, the user must also log-in to purchase their chosen products and review products they have purchased. All products, users and physical attributes on the site are located in PostgreSQL database.

## Planning of Gymstuff.com
The planning undertaken prior to beginning the project is described in the following document: [Project planning document](https://github.com/chrismurray1980/GymStuff/blob/master/PLANNING.md)

## Wireframe/site configuration development
![Image not available](https://chris-m-ecommerce.s3.amazonaws.com/media/images/gumstuff_home_wireframe.JPG)

kbkjbkjbkjbkjb

![Image not available](https://chris-m-ecommerce.s3.amazonaws.com/media/images/home1.JPG)

fgdfhfdhdfhdfhdfhdf

![Image not available](https://chris-m-ecommerce.s3.amazonaws.com/media/images/home2.JPG)

## Final database schema

## Site configuration

## Site features

For clarity, site features will be outlined in terms of how they are implemented in each of the HTML templates.

## Features Left to Implement

Due to time constraints the following features, which would produce a more enjoyable user experience and more professional website, were not implemented:

## Technologies Used

The following technologies were used in the development of the application:

Flask: A microframework for Python
MongoDB Atlas: Automated cloud mongoDB service
JQuery: A javascript library used for event handling and DOM manipulation
Bootstrap 4: A toolkit for developing HTML, CSS, and JS
SASS: A professional level CSS extension language
Jinja: Templating language for Python
Heroku: A cloud platform as a service
dc.js: Dimensional charting javascript library
d3.js: Javascript library for manipulating documents based on data
Ming: An object document mapper for mongoDB which extends Pymongo
AWS S3: Amazon simple storage device
flask_login: Provides user session management for Flask applications
flask_sslify: Converts all incoming requests from application to https
Flask-testing: Provides unittesting utilities for Flask
GitHub: used to store and save versions of the application
Cloud9: online IDE used to develop the application

## Testing

Both automated and manual testing was undertaken on the application and this is described in detail in the following document: Testing document

### Travis CI Testing

[![Build Status](https://travis-ci.org/chrismurray1980/GymStuff.svg?branch=master)](https://travis-ci.org/chrismurray1980/GymStuff)

## Code validation

The HTML, CSS and JS code was run through code validation to detect any errors.

### HTML validation

The W3C Markup validation service was used to check the quality of the HTML language used. This was run for all the document templates and the base template as follows:

W3C_base.html
W3C_add_recipe.html
W3C_edit_recipe.html
W3C_favourites.html
W3C_index.html
W3C_login.html
W3C_my_recipes.html
W3C_register.html
W3C_search_results.html
W3C_show_recipe.html

The the main issues found were due to the use of Jinja.

### CSS validation

The W3C CSS validation service was used to check the quality of the CSS used. The results are show here: W3C_CSS

### JS validation

The written in the main.js and plot.js files was run through JSHint with no major errors as follows:

    JSHint_main.js
    JSHint_plot.js

## Deployment

To deploy the application to Heroku firstly, a new project was created in Heroku. A Procfile was created which was used to tell Heroku how to run the application. In addition to this a requirements.txt file was created which told Heroku which Python modules were needed to run the application. In addition to this, environment variables had to be configured in Heroku. This was achieved by going to the project settings in Heroku and implementing the IP and PORT to be used by the application in the config variables settings. In addition to this the name of the mongoDB collection and the URI of the database were added to these settings. In addition to this, for security within Flask, a secret key for the application was also added to these variables. The variables used by S3 such as the access key, secret key and bucket name were configured for use with Heroku by running:

$heroku config:set S3_KEY=****** S3_SECRET=******* S3_BUCKET=*********

in the console of the Cloud9 application. The project was deployed to Heroku by going to the deploy tab and manually deploying the master branch of the project's GitHub repository. Once the project was successfully deployed, the project was opened by clicking the 'view app' button in Heroku: this was achieved with minimal number of issues.

There is no difference between the deployed and development versions of the application other than in development version debug is set to 'True' whereas in deployment debug is set to 'False'. The site can be accessed here The Good Grub Guide

### Credits

The following websites were used for guidance and code snippets used within this application:


### Media

The background image used on the website was obtained from Pexels.

django reviews  https://django-rated-reviews.readthedocs.io/en/latest/quickstart.html


