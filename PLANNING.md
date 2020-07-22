# Milestone Project 5 : Online fitness equipment and nutrition ecommerce site

This e-commerce site is aimed at customers looking to purchase a variety of fitness equipment and nutritional supplies to assist in their fitness goals.

## User experience

This site allow users to quickly search for and view fitness equipment to meet their fitness needs. Additionally, users can quickly search for nutritional supplements to meet their nutritional needs. Users can register for the site and these registered users can add items to a shopping cart and purchase the equipment and supplements via credit card for home delivery.

As an additional feature, aimed at enhancing nutritional understanding, users can input their current physical attributes and future physical attributes to calculate their BMI, recommended calorie consumption and recommended macro-nutrient ratios.

## Vision Statement

'This e-commerce site will display fitness equipment and nutritional supplements for purchase via credit card and home delivery. Products on the site can be searched for and filtered based on several categories. Products can be added to a shopping cart by logged in users and users can pay for these products and get them delivered to their home. To aid the users' nutritional requirements: users can input their physical attributes and obtain recommendations for daily calorie intake and macro-nutrient balance.'

The following feature list will fulfil this vision:

I can search for products based on the following search criteria: 

    Fitness products:
    
        Weights:
            Plates
            Bars
            Dumbells
            
        Gym Equipment:
            Home multigym
            Benches
            Squat racks
            
    Nutritional products:
    
        Supplements:
            Protein Powders
            Protein bars
            Healthy snacks
            
        Vitamins

Account:

    I can register for the site and create an account
    I can login into the site once I've registered
    I can add products to the shopping cart and purchase them once registered

Shopping cart:

    I can add products, in various quantities, to the shopping cart
    I can remove products from the shopping cart
    I can view the products in the shopping cart

Checkout:

    I can pay for the products via credit card
    I can arrange for home delivery of my purchase

Nutrition calculator:

    I can enter:
        
        Current height
        Current weight
        Current activity level
        Sex
        Goal weight
    
    I will be returned:
        
        Current BMI
        Goal BMI
        Goal calorie intake
        Goal macro balance
        Goal macro weights
    

General:

    When I enter the site I’m shown the landing page
    All products are displayed on the landing page 
    I can click any product shown to be taken to the product page
    When I click search I’m taken to the search form
    I can login to the site
    I can register for the site

## User stories

    ‘I'm a fitness enthusiast but my gym has been shut due to covid-19. I want to purchase some home gym equipment for my garage’

I would access the site and search for home multi-gym. Having perused the available products, I select one and add it to my shopping cart. I then proceed to checkout and pay for it via credit card and await my home delivery.

    'As a stay at home parent, I want some equipment that I can use to exercise then store away safely and doesn't take up loads of room'

The parent enters the site and is shown a dumbbell set and skipping ropes on the landing page. The user views both products and adds both products to their shopping cart. At checkout the user decides the skipping ropes are within budget and the dumbbells are a little expensive. The user then removes the dumbbells from their cart and proceeds with the purchase of the skipping ropes.

    ‘As an enthusiastic cook, I want to share my recipes with others so that I can see if others enjoy them too.’

The cook would enter the site and click on the add recipe link in the navbar, if they haven’t logged-in they will be asked to log-in. If they haven’t previously registered they will be asked to create an account. They will then redirected to the add recipe site where they can add details of their recipe, the recipe is submitted by clicking the add recipe button, they will then be redirected to the home page.

    ‘As I have uploaded recipes to the site before, I want to change the amount of garlic in my pasta dish, so that the recipe isn’t as overpowering.’

The user would enter the site and click on the edit/delete recipe link in the navbar, if they haven’t logged-in they will be asked to log-in then redirected to the edit/delete recipe site where they can edit details of their recipe, the recipe is submitted by clicking the edit recipe button, the user will then be redirected to the home page.

    ‘As I have uploaded recipes to the site before, I want to delete my recipe as I think there are better versions of this on the site already.’

The user would enter the site and click on the edit/delete recipe link in the navbar, if they haven’t logged-in they will be asked to log-in then redirected to the edit/delete recipe site where they can delete their recipe, submitted by clicking the delete recipe button. The recipe will then be completely removed from the database, the user will then be redirected to the home page.

    ‘As a son, I want to go round to make my Italian Mother breakfast in bed on Mother’s day, I want to make a tasty Italian breakfast for her’

The son would access the site and click on the search button. The son would then filter for Italian as the cuisine and also filter for breakfast in the mealtime category. The results are then displayed.

    ‘As a husband, I want to cook that vegan recipe from the site that my wife loved, so that she knows how much I appreciate her’

The husband would access the site and click on the favourite’s link in the navbar, if they haven’t logged-in they will be asked to log-in then redirected to the their favourite’s page where they can either look through their favourite recipes or filter the results to find it directly.

    ‘As a cook, I have just cooked the lamb recipe from the site and want to show that I think it’s a good recipe’

The cook accesses the site and searches for the recipe. The cook then clicks the upvote button on the recipe, if they haven’t logged-in they will be asked to log-in then redirected back to the page with the upvote now in place.

## Page content and wireframes Base page layout

### Header: contains site name, links to: log-in if not already completed, personal favourites, home, edit/delete recipe, add recipe, and search.

### Footer: copyright

### Side bar: shows list of recipes based on ingredients, allergens, cuisine type, dietary choice, meal time: can add multiple filters selected by user. Shows data on number of recipes based on ingredient, cuisine type, meal time. Shows data on most popular of recipes based on ingredient, cuisine type, meal time. Landing page

### Home page on site. Contains header, footer and sidebar. Contains site title. Contains most popular recipes (information and picture) based on up-votes from users.

This image is not available Show recipe page

Shows image, ingredients, preparation and cooking time, detailed instructions for cooking.

This image is not available Add recipe page

Form to add name, time, instructions, and ingredients. Contains submit recipe button.

This image is not available Edit recipe page

Form to edit name, time, instructions, and ingredients, etc. Contains edit recipe button and delete recipe button (page only visible if it is the author who created the recipe).

This image is not available Search recipe page

Form containing specifics such as allergens, main ingredient, cuisine type, meal time.

This image is not available Search results page

Shows all recipes which match the specified criteria during the search.

This image is not available Favourite recipes page

Contains user’s favourite recipes (information and picture) based on saved recipes.

This image is not available Log-in page

Contains form for username and password and submit button.

This image is not available Add user page

Add new user to site. Contains header and footer. Contains form to add new user to database.

This image is not available 

## Languages/Technologies to be used

Flask
MongoDB Atlas
Python 3
JQuery
CSS 3
HTML 5
JS
Bootstrap
SASS
Jinja
Heroku
dc/d3.js
python bcrypt library

## Scripts and files

app.py: contains all code to generate html templates; contains code to open/close connection to database and perform CRUD operations based on the template contents
base.html: contains the base html content to be used by the site pages index.html: extends base.html and is the landing page for the site, shows most popular recipes
addrecipe.html: extends base.html and allows user to add new recipe
editrecipe.html: extends base.html and allows user to edit or delete recipe
favourites.html: extends base.html and displays user favourites
search.html: extends base.html and used to search for recipes
showrecipe.html: extends base.html and shows details of recipe
login.html: extends base.html and allows user to log-in to site
register.html: extends base.html and allows user to register for site
style.css: contains styles to be used on site
main.js: contains js code to be executed by site
display.js: contains data presentation JS code
Test files: run unit level test on python
Procfile: tells Heroku how to run the app
requirements.txt: list of packages to be installed to run application

## Database schema

The document scheme used to organise the site data on Mongo DB Atlas is a hybrid approach which uses components of both normalised and de-normalised data patterns. All the documents required for the site are contained within a single collection and allocated a ‘document’ attribute, as follows:

User: stores specific user data
Recipe: stores specific recipe data

The database schema is shown below:

This image is not available

Recipe name and recipe author values are duplicated across the Recipe and User document types as these values will be regularly used whilst the remainder of the Recipe and User properties remain separated out.