# Milestone Project 5 : E-commerce site planning

This e-commerce site is aimed at customers looking to purchase a variety of fitness equipment and nutritional supplies to assist in their fitness goals.

## User experience

This site allow users to quickly search for and view fitness equipment to meet their fitness needs. Additionally, users can quickly search for nutritional supplements to meet their nutritional needs. The user can add their selected products to their cart. Users can register for the site and these registered users can add product reviews and purchase the equipment and supplements via credit card for home delivery.

As an additional feature, aimed at enhancing nutritional understanding, users can input their current physical attributes to calculate their BMI, recommended calorie consumption and recommended macro-nutrient ratios.

## Vision Statement

'This e-commerce site will display fitness equipment and nutritional supplements for purchase via credit card and home delivery. Products on the site can be searched for and filtered based on several categories. Products can be added to a shopping cart and logged in users can pay for these products and get them delivered to their home. To aid the users' nutritional requirements: users can input their physical attributes and obtain recommendations for daily calorie intake and macro-nutrient balance.'

The following feature list will fulfil this vision:

I can search for products by name and based on the following search categories: 

- Fitness products:
    - Weights
    - Benches and racks
    - Accessories
        
- Nutritional products:
    - Supplements
    - Vitamins

The site will have the following functionality:

- Account:
    - I can register for the site and create an account
    - I can login to the site once I've registered
    - I can logout of the site
    - I can reset my password if I forget it
    - I can purchase products once registered

- Shopping cart:
    - I can add products, in various quantities, to the shopping cart
    - I can remove products from the shopping cart
    - I can view the products in the shopping cart

- Checkout:
   - I can pay for the products via credit card

- BMI calculator:
    - I can enter current height
    - I can enter current weight
    - I will be returned calculated BMI
    - I will be returned my BMI category
        
- Macro calculator:
    - I can enter current height
    - I can enter current weight
    - I can enter my activity level
    - I can enter my fitness aim
    - I can enter my age
    - I will be returned my base metabolic rate (bmr)
    - I will be returned my Total Daily Energy Expenditure (TDEE)
    - I will be returned my daily calorie goal
    - I will be returned my recommended macronutrient ratio
    - I will be returned my recommended macronutrient weights in grams

- Customer reviews:
    - I can view reviews associated with a particular product
    - When logged in, I can add a review for a particular product
    - I can add comments and a rating for the product to my review

- General:
    - When I enter the site I’m shown the landing page
    - Products from each category are displayed on the landing page 
    - I can click any product shown to be taken to the specific product page
    - I can enter search terms to find products

## User stories

    ‘I'm a fitness enthusiast but my gym has been shut due to covid-19. I want to purchase some home gym equipment for my garage’

I would access the site and search for 'multi-gym'. Having perused the available products, I select one and add it to my shopping cart. I then proceed to checkout and pay for it via credit card and await my home delivery.

    'As a stay at home parent, I want some equipment that I can use to exercise then store away safely and doesn't take up loads of room'

The parent enters the site and is shown a dumbbell set and skipping ropes on the landing page. The user views both products and adds both products to their shopping cart. At checkout the user decides the skipping ropes are within budget and the dumbbells are a little expensive. The user then removes the dumbbells from their cart and proceeds with the purchase of the skipping ropes.

    'I'm an enthusiatic body builder but have grown bored of my current protein powder flavour but still don't want to pay through the nose for it'

The user enters the site and searches for protein powders. The user is then directed to the search results page showing all available protein powders. They select one and proceed through checkout to pay for their product.

## Page content and wireframes 

The site will consist of a main content container surrounded by an image. The content container will contain the header; page specific content; and the footer. The Header contains the site name, links to products, account, cart and body calculators (BMI/Macro). The header will also contain a search input for the user to search for products. The page content will contain specific information for each page. The footer will contain copyright information for the site.

### Landing page layout

The landing page will consist of products from each category displayed on the page. A link to all products of each category will be included at the bottom of each category section as shown below.

![Image not available](https://chris-m-ecommerce.s3.amazonaws.com/media/images/gumstuff_home_wireframe.JPG)

### Show products of category

When the user clicks on the 'view related products' button on the home page or the product category link in the navigation bar they will be directed to the show product category page. This contains all products of a particular category as shown below.

![Image not available](https://chris-m-ecommerce.s3.amazonaws.com/media/images/all_products.JPG)

### Product page

When the user clicks on the 'view product' link they are directed to the product page. This gives further information on the product; allows the user to add the product to their cart and allows the user to view reviews of that product. Additionally, logged in users can add reviews of that product.

![Image not available](https://chris-m-ecommerce.s3.amazonaws.com/media/images/product_page.JPG)

### Calculator forms

When the user decides to calculate their BMI or macronutrients the user clicks the relevant link and is directed to either the BMI calculator form or the macro calculator form with a layout as shown below.

![Image not available](https://chris-m-ecommerce.s3.amazonaws.com/media/images/bmi_calc.JPG)

## Languages/Technologies to be used

- Django
- Python 3
- Javascript
- PostgreSQL
- JQuery
- Bootstrap 4
- Heroku
- dc.js
- d3.js
- AWS S3
- GitHub
- AWS Cloud9
- STRIPE API
- Travis CI

## Database schema

The database used will be a PostgreSQL relational database. The database will follow the schema shown below.

![Image not available](https://chris-m-ecommerce.s3.amazonaws.com/media/images/db_schema.JPG)