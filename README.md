# Gymstuff.com : Ecommerce Site

This project is a web-based e-commerce site which allows users to view gym products, supplements and vitamins to aid their fitness goals. The user can search products by name or by category. In addition to this, the user can input their current physical attributes and gain insights such as current body mass index; recommended daily calorie intake for a selected aim; and recommended daily macronutrient intake.
The user is required to register and log-in to access the physical attribute features, the user must also log-in to purchase their chosen products and review products they have purchased. All products, users and physical attributes on the site are stored within a PostgreSQL relational database.

## Planning of Gymstuff.com
The planning undertaken prior to beginning the project is described in the following document: 

- [Project planning document](https://github.com/chrismurray1980/GymStuff/blob/master/PLANNING.md)

## Wireframe/site configuration development

The basic layout of the web page consists of all the page content surrounded by the background image. The header, content and footer are all contained within this main container. The header consists of the site brand; navigation links; and a search bar. The header is uniform across all the site's pages. Below the header is where the current page content is shown. Following the current page content is the footer which contains copyright information.

### Landing page

The home page of the site shows the top products from each of the product categories. Each category is separated by the category label and shows the three most expensive products for each category. These products are followed by a button to show all products of this specific category. At the bottom of the home page is a Home button to take the user back to the top of the page. The wireframe designed for the home page is shown below.

![Image not available](https://chris-m-ecommerce.s3.amazonaws.com/media/images/gumstuff_home_wireframe.JPG)

Fortunately, the layout used gives a clean, clear user experience and needed little modification from the initial wireframe design. The layout of the final homepage is shown in the images below. The products are shown as cards containing product title, image, information and price.

The header of the site, shown below, remains uniform and as stated previously contains the brand, links and search bar.

![Image not available](https://chris-m-ecommerce.s3.amazonaws.com/media/images/home1.JPG)

The weight category product cards are shown in the image below.

![Image not available](https://chris-m-ecommerce.s3.amazonaws.com/media/images/home2.JPG)

Finally, the category section is completed with a link to all products in that category. This is followed by the section showing the three most expensive products in the rack and bench category. This layout is repeated for all five product categories in the database.

![Image not available](https://chris-m-ecommerce.s3.amazonaws.com/media/images/home3.JPG)

### Product category

When selecting a product category from the navigation bar or by clicking the 'view similar products' link on the landing page, the user will be shown the product category page. This page contains all products of a particular category ordered from least to most expensive. Again, the products are shown as cards to give a clear layout and instantly convey the product information to the user. The wireframe for the all products page is shown below and is the same for all product categories. After all the products have been listed the user is given the option of returning home via the home button.

![Image not available](https://chris-m-ecommerce.s3.amazonaws.com/media/images/all_products.JPG)

The final layout of this page is shown below with the last three products and the home button shown.

![Image not available](https://chris-m-ecommerce.s3.amazonaws.com/media/images/all_products_complete.JPG)

### Product page

Within the product cards on the landing page and the category pages, the user is given the opportunity to view the specific product in more detail by clicking the 'view more' link. This will take the user to the product page for that specific product. 

The product page conatins the name of the product, a larger product image and a more in-depth product description. In addition to this, the page contains the add to cart form and button and the 'product reviews' button. The product reviews button lists the reviews of the product given by registered users. At the bottom of the page is the 'add review' button which allows logged in users to add a review for that product: this button and form is hidden for unauthorised users.

![Image not available](https://chris-m-ecommerce.s3.amazonaws.com/media/images/product_page.JPG)

The final layout of the page is shown below. When the 'add review' button is clicked the add review form is revealed.

![Image not available](https://chris-m-ecommerce.s3.amazonaws.com/media/images/product_page-actual.JPG)

### Calculator pages

The site also contains the BMI and Macro calculator features. The user inputs their physical attributes into the BMI or Macro calculator forms and their results are calculated and displayed to the user. The forms use simple bootstrap layout and the wireframe for the BMI form is shown below.

![Image not available](https://chris-m-ecommerce.s3.amazonaws.com/media/images/bmi_calc.JPG)

Again, implementation of this varied very little from the initial wireframe design, the final version is shown below.

![Image not available](https://chris-m-ecommerce.s3.amazonaws.com/media/images/bmi_calc_actual.JPG)

## Database schema

As stated in the project planning document, the database for the application consisted of database schemes based on several different app models, related via foreign keys within the database. As the project developed the database model for each app did also. The model definitions for the products themselves and the unique models added to this project are shown below.

### Product model

The product model, shown below, contains all information related to the product, including a field to upload the product image. The category field is populated by means of choices supplied in the product model.

    name = models.CharField(max_length=254, default='')
    category = models.CharField(max_length=30, choices=CATEGORY, default='Weights')
    short_description = models.CharField(max_length=254, default='')
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(upload_to='images')

### Physical model

The Physical model, for calculating user BMI, contained within the physical app has the following model definition:

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    height = models.FloatField(validators=[MinValueValidator(0), MaxValueValidator(300)],)
    weight = models.FloatField(validators=[MinValueValidator(0), MaxValueValidator(500)],)
    unit_height = models.FloatField(default=0)
    unit_weight = models.FloatField(default=0)
    bmi_calc = models.FloatField(default=0)
    bmi_category = models.CharField(default='', max_length=200)
    date_now = models.DateTimeField(auto_now_add=True)
    unit_type = models.CharField(choices=unit_type, default='Metric', max_length=200)

In this case the user is the foreign key used to link tables within the database. The site user is able to select the 'unit\_type' field based on choices defined within the model itself. The model fields from 'unit\_height' onwards, excluding 'unit\_type', are obtained via methods within the BMI model class.

### Macro model

The Macro model contained within the physical app has the following model definition:
    
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    height = models.FloatField(validators=[MinValueValidator(0), MaxValueValidator(300)],)
    weight = models.FloatField(validators=[MinValueValidator(0), MaxValueValidator(500)],)
    age = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(120)],)
    unit_height = models.FloatField(default=0)
    unit_weight = models.FloatField(default=0)
    activity_level = models.CharField(choices=activity_level, default='', max_length=200)
    bmr = models.FloatField(default=0)
    TDEE = models.FloatField(default=0)
    date = models.DateTimeField(auto_now_add=True)
    aim = models.CharField(choices=aim, default='', max_length=200)
    daily_calorie_goal = models.FloatField(default=0)
    carb_weight = models.FloatField(default=0)
    protein_weight = models.FloatField(default=0)
    fat_weight = models.FloatField(default=0)
    carb_percent = models.FloatField(default=0)
    protein_percent = models.FloatField(default=0)
    fat_percent = models.FloatField(default=0)
    unit_type = models.CharField(choices=unit_type, default='Metric', max_length=200)

Again, the user is the foreign key used to link tables within the database. The site user is able to select the 'unit\_type' field based on choices defined within the model itself. This also goes for the 'aim' and 'activity\_level' fields. Again, the majority of the fields are populated by means of methods contained within the model class.

### Customer Review model

The customer review model is contained within the customer-review app. In this case the product itself is used as the foreign key to link the review to a specific product. In this case the user is given choices for the rating which are defined within the model itself.

    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    username = models.CharField(max_length=200)
    headline = models.CharField(max_length=200)
    comment = models.TextField()
    rating = models.IntegerField(choices=RATING_CHOICES)
    date = models.DateTimeField(auto_now_add=True)
    
## Site configuration

The Gymstuff.com project consists of several applications working together to generate the final website. The applications within this project are:  

- Accounts  
- Cart  
- Checkout  
- Customer reviews  
- Physical  
- Products  
- Search  

### Settings

The settings script within the Gymstuff project directory allows for the setup of the databases used, the configuration of the media storage; email setup; and static file storage. Each of the project apps must be registered here to allow them to function within the website.

#### Database 

The database used within the project was the PostgreSQL database available through Heroku. A superuser was created for this database which allowed full access to the database. This access was available through django admin.

#### Storage

An Amazon S3 bucket was configured and linked to the project to store the static files ( CSS and JS). This is necessary as Heroku will delete static files so external storage is required. The S3 bucket was also used to store media files such as images that are used within the site.

#### Environment variables

The secret keys, email passwords, stripe variables and environment variables for S3 were stored within an env.py file during development, this file was never uploaded to the project git repository. During deployment the enviroment variables are stored in heroku.

#### URLs

The URLs script within the Gymstuff project directory itself allows each of the app urls to be accessed via a single location. This allows the content for each app to be accessed throughout the entirety of the website.

### Apps

Rather than reinventing the wheel; several of the core apps were imported from Code Institute's Ecommerce project. In this case, the link will be given to the app code rather providing a description of the code and functionality itself. In the case that the code was either personally generated or heavily modified: a more detailed description will be given.

#### Accounts

The accounts app used in this project was taken directly from Code Institute's Ecommerce project with minimal modification, the link to this application can be found [here](https://github.com/Code-Institute-Solutions/e-commerce/tree/master/2-Completed_Project/accounts). This app allows users to register, login, logout and provides 'forgot my password' reset functionality.

#### Cart  

The cart app used in this project was taken directly from Code Institute's Ecommerce project with minimal modification, the link to this application can be found [here](https://github.com/Code-Institute-Solutions/e-commerce/tree/master/2-Completed_Project/cart). This app allows users to add products to their cart via a form and amend or remove these products from their cart. The only modification made to this app is detailed below.

##### add\_to\_cart function

Minor modifications were made to this function primarily, to return the user back to the product page they were viewing rather than the landing page of the site. This was modified to provide a better user experience and achieved using the following code:

    return HttpResponseRedirect(reverse('product', args=(product.id,)))
    
Further minor modifications were made in returning more messages to the user to further improve their experience.

#### Checkout  

The checkout app used in this project was taken directly from Code Institute's Ecommerce project with minimal modification, the link to this application can be found [here](https://github.com/Code-Institute-Solutions/e-commerce/tree/master/2-Completed_Project/checkout). This app allows customers to pay for their chosen products using the Stripe API.

#### Customer reviews  

This is a relatively simple app and contains only the functionality used to display the customer reviews based on the specific product. The single view of the app is detailed below.

##### Customer review 

The function gets the product ID and queries the databse for all reviews associated with that product. The query will return the nine latest reviews of the product from newest to oldest. The user is then directed to the customer review html which lists all the reviews found for that product as shown below.

    def customer_reviews(request, id):
        # Get product from id
        product=get_object_or_404(Product, id=id)
        # List latest reviews by date
        latest_review_list = customer_review.objects.filter(product__id=id).order_by('-date')[:9]
        # Create view context
        context = {'latest_review_list':latest_review_list, 'product':product}
        # Render review page
        return render(request, 'customer_reviews.html', context)

#### Physical  

This app is used to take the user's physical inputs and calculate either the user bmi or provide information on recommended daily calorie intake and macronutrient ratios. This app contains two models: Physical (for BMI calculations) and Macro (for macronutrient calculations). The views for the Physical and Macro models are described below.

##### BMI form

For the BMI form, the user enters their height and weight in either Imperial or Metric units. The functions contained within the model do any conversion required and calculate the user's BMI. The function then queries the database for the latest post by the user and directs the user to the bmi results html to display the results. If the form data is invalid the user is returned to the form.

    @login_required
    def bmi_form(request):
        # Create instance of form
        form = bmi(request.POST)
        # Validate form 
        if form.is_valid():
            # Get data from form
            height = form.cleaned_data['height']
            weight = form.cleaned_data['weight']
            unit_type = form.cleaned_data['unit_type']
            # Create instance of model 
            physical = Physical()
            # Assign values to model instance
            physical.height= height
            physical.weight= weight
            physical.unit_type = unit_type
            physical.date_now = datetime.datetime.now()
            form_save= form.save(commit=False)
            form_save.user= request.user
            # Save created instance
            form_save.save()
            # Search database for model instance
            details = Physical.objects.filter(user=request.user).order_by('-date_now')[:1]
            # Render result with model instance
            return render(request, 'bmi_result.html', {'details':details})
            # Render bmi form
        return render(request, 'bmi_form.html', {'form': form})

##### Macro form

For the Macro form, the user enters their height and weight in either Imperial or Metric units. The functions contained within the model do any conversion required and calculate the user's recommended daily calorie intake and macronutrient ratios based on user golas. The function then queries the database for the latest post by the user and directs the user to the macro results html to display the results. If the form data is invalid the user is returned to the form.

    @login_required
    def macro_form(request):
        # Create form instance
        form = macro(request.POST)
        # Validate form
        if form.is_valid():
            # Get form data
            height = form.cleaned_data['height']
            weight = form.cleaned_data['weight']
            age = form.cleaned_data['age']
            activity_level = form.cleaned_data['activity_level']
            aim = form.cleaned_data['aim']
            # Create model instance
            macro_calc = Macro()
            # Assign data to model instance
            macro_calc.height= height
            macro_calc.weight= weight
            macro_calc.age = age
            macro_calc.activity_level = activity_level
            macro_calc.aim = aim
            form_save= form.save(commit=False)
            form_save.user= request.user
            # Save model instance
            form_save.save()
            # Search database for model instance 
            details = Macro.objects.filter(user=request.user).order_by('-date')[:1]
            # Extract weight and percentage data from macro database search
            for item in details:
                carb_weight = item.carb_weight
                protein_weight = item.protein_weight
                fat_weight = item.fat_weight
                carb_percent = 100*item.carb_percent
                protein_percent = 100*item.protein_percent
                fat_percent = 100*item.fat_percent
            # Create macro array
            macros = [carb_weight, protein_weight, fat_weight, carb_percent, protein_percent, fat_percent]
            # Convert array to JSON
            macros_json = json.dumps(macros)
            # Render macro results page passing details and macro_json as arguments
            return render(request, 'macro_result.html', {'details': details, 'macros': macros_json})
        # Render macro form
        return render(request, 'macro_form.html', {'form': form})

#### Products 

The products app used in this project was taken directly from Code Institute's Ecommerce project, the link to this application can be found [here](https://github.com/Code-Institute-Solutions/e-commerce/tree/master/2-Completed_Project/products). This app is used to define products within the database. The app model itself was modified to include a 'Category' field in addition to modification to existing views or creation of entirely new functions. These will be described in the following.

##### all\_products

The all products function is used in Code Insitute's Ecommerce site for the landing page to show all the products. This was modified to find all products of a particular category ordered by price and limited to three products. Passing this to the landing page template allowed products to be displayed by category and was achieved using the 'weights' category example below.

    def all_products(request):
        # Get products based on category
        weights = Product.objects.filter(category='Weights').order_by('-price')[:3] 
        # Render all products view
        return render(request, "all_products.html", {"weights": weights})

##### product

This function allows the user to view the product page for a specific product. The function finds the product by means of its ID, it then generates the review form for the product and then renders the product page as shown in the code below.

    def product(request, id):
        # Get product via id
        product = Product.objects.get(pk=id)
        # Generate review form
        form = ReviewForm()
        # Get product page
        return render(request, 'product.html', {'product': product, 'form':form })

##### Create product review 

The create product review view posts the data from the review form, validates the form and then returns the user to the specific product page if the review was posted successfully. The '@login' decorator ensures that only authorised users can post reviews, the code for this function is shown below.

    @login_required
    def create_or_edit_review(request, product_id):
        # Get product by id
        product = Product.objects.get(id=product_id)
        # Create form instance 
        form = ReviewForm(request.POST)
        # Validate form
        if form.is_valid():
            # Get data from form
            rating = form.cleaned_data['rating']
            comment = form.cleaned_data['comment']
            username = form.cleaned_data['username']
            headline = form.cleaned_data['headline']
            # Create model instance
            review = customer_review()
            # Add data to model instance
            review.product = Product.objects.get(id=product_id)
            review.username = username
            review.rating = rating
            review.comment = comment
            review.headline = headline
            review.date = datetime.datetime.now()
            review.save()
            # Inform user that review successfully submitted
            messages.success(request, "You have successfully reviewed this product")
            # Return to product view
            return HttpResponseRedirect(reverse('product', args=(product.id,)))
        # Render product view
        return render(request, 'product.html', {'product': product, 'form': form})

##### Similar products view

This view is used to allow users to view all products of a particular category. The function finds the product in the database by means of its ID then filters all products of that category in terms of price. The site then directs the user to the product category html page as shown in the code below.

    def view_similar_products(request, product_id):
        # Get product by id
        product = Product.objects.get(id=product_id)
        # Find product category
        product_category = product.category
        # Search db for products of category and order by price
        category = Product.objects.filter(category=product_category).order_by('price')
        # Display product category page
        return render(request, "product_category.html", {"products": category})

#### Search

The search app used in this project was taken directly from Code Institute's Ecommerce project, the link to this application can be found [here](https://github.com/Code-Institute-Solutions/e-commerce/tree/master/2-Completed_Project/search). This app is used to search for products or categories using the search bar and additionally, to search for products using navigation bar links. Modifications were made to the views of this app, as described in the following.

##### do_search

This function originally only searched for the name of the product. To improve user experience 'OR' functionality was added to include the category field of the product as shown in the code below.

    def do_search(request):
        products = Product.objects.filter(Q(name__icontains=request.GET['q']) |  Q(category__icontains=request.GET['q'])).order_by('price')
        return render(request, "product_category.html", {"products": products})

##### category search

A category search feature was added to allow navigation links to query the database for products of a particular category. An example showing the function to search the 'weight' category is shown below.

    def weight_search(request):
        weights = Product.objects.filter(category='Weights').order_by('price')
        return render(request, "product_category.html", {"products": weights})

## Site features

For clarity, site features will be outlined in terms of how they are implemented in each of the HTML templates.

#### base.html

This template is used as the basis for the more content specific html templates on the site: each of which will add unique content to the standard base.html. The base.html template consists of a navbar which contains the site logo; the navigation links for the the pages on the site; and a search bar for the user to search for products. The site logo, itself, provides a link anchor which will return the user to the landing page upon click. This allows the user to easily access the home page from any other page on the website. In addition to this, the navigation account links are log-in status specific. At the bottom of the page is where the footer is located and this contains copyright information for the website.

#### login.html

When the user clicks the log-in link on the navbar they are directed to the 'login.html' page. This page contains input fields for the user's email and password. If the user inserts an incorrect username or password the page is refreshed and the user is informed that an incorrect username or password has been entered. Once the user has logged-in they are redirected back to the home page unless the log-in was triggered by a request for a page that requires authentication wherein the user will be redirected to the originally requested page.

#### register.html

The register user page allows new users to be added to the website's datasbase. This consists of an html form with fields for username; email; password; and confirm password. If the password and confirm password do not match the user is informed of this and the register user page is reloaded. Upon submission, the user is added to the database and redirected to the login page to enter the website.

#### cart.html

This page displays the products added to the cart by the user and their quantities. In addition to this, the page displays the total cost of all cart items and a button to take the user to the checkout page. If the user visits their cart but hasn't added any products; they will be informed that their cart is empty and no checkout button will be visible.

#### checkout.html

The checkout page contains the forms used to insert the user's personal details for delivery and to insert payment details. At the bottom of the page is the 'Submit payment' button which will initiate interaction with Stripe API.

#### customer\_reviews.html

This page lists the customer reviews related to a specific product obtained by querying the database using the 'customer_reviews' function.

#### bmi\_form.html

This page contains the form used to submit user information for the bmi calculation. The user has the option of using either Metric or Imperial unit systems.

#### bmi\_result.html

This page displays the output of the bmi entry in the database created by the submission of the bmi form. This page displays the calculated bmi of the user and the bmi category of the user.

#### macro\_form.html

This page contains the form used to submit user information for the macro calculation. The user has the option of using either Metric or Imperial unit systems.

#### macro\_result.html

This page displays the output of the macro entry in the database created by the submission of the macro form. This page displays the calculated bmr of the user; TDEE; and daily calorie goal. In addition to this, information passed from the macro_form view, in json format, is used to generate a pie chart of recommended macro percentage and a bar chart of recommended macro weight using dc.js.

#### all\_products.html

This is the landing page of the entire site and displays the three most expensive products from each of the product categories, displayed as card elements. In each of these product cards there is a link to view the product in more detail and within each of the category sections there is a link to view all products of that particular category.

#### product.html

This page displays a specific product in more detail. The page contains a form to add a quantity of the product to the user cart and a button to view reviews of the product by registered users. In addition to this, if logged in, the user can add a review of the current product.

#### product\_category.html

This page displays all products, in the form of product cards, of a specific category in the product model.

## Features Left to Implement

Due to time constraints the following features, which would produce a more enjoyable user experience and more professional website, were not implemented:

- Email to user to confirm successful payment and estimated delivery date
- Ability to provide alternative delivery address for user
- In bmi and macro forms, a calculator to help users to convert stone to pounds and foot to inches
- Instead of the three most expensive products in each category on home page: a carousel showing the products bought most frequently
- A counter for the average rating of each product and the number of likes shown on the landing page and the product page

## Technologies Used

The following technologies were used in the development of the application:

- [Django](https://www.djangoproject.com/): A  high-level Python Web framework
- [PostgreSQL](https://www.postgresql.org/): A powerful, open source object-relational database 
- [JQuery](https://jquery.com/): A javascript library used for event handling and DOM manipulation
- [Bootstrap 4](https://getbootstrap.com/): A toolkit for developing HTML, CSS, and JS
- [Heroku](https://dashboard.heroku.com/): A cloud platform as a service
- [dc.js](https://dc-js.github.io/dc.js/): Dimensional charting javascript library
- [d3.js](https://d3js.org/): Javascript library for manipulating documents based on data
- [AWS S3](https://aws.amazon.com/s3/): Amazon simple storage device
- [GitHub](https://github.com/): used to store and save versions of the application  
- [AWS Cloud9](https://aws.amazon.com/cloud9/): online IDE used to develop the application
- [Stripe API](https://stripe.com/gb?utm_campaign=paid_brand-UK_en_Search_Brand_Stripe-2032860449&utm_medium=cpc&utm_source=google&ad_content=355351450073&utm_term=stripe%20api&utm_matchtype=e&utm_adposition=&utm_device=c&gclid=CjwKCAjwyo36BRAXEiwA24CwGS57sL_ESAoPiQB-CtpG2MG0zj-NJS5GDoFXO6J7O7Yy01--LcXxKRoCTLQQAvD_BwE): A complete payment platform
- [Travis CI](https://travis-ci.org/getting_started): A continuous integration service

## Testing

Manual testing of the user experience was undertaken on the site by various helpful volunteers. In addition to this, unit testing was conducted on each of the apps. This was undertaken by running the following command:

    $python3 manage.py test <app name>

### Travis CI Testing

Continuous integration testing was undertaken using Travis-CI. The results of which are shown below.

[![Build Status](https://travis-ci.org/chrismurray1980/GymStuff.svg?branch=master)](https://travis-ci.org/chrismurray1980/GymStuff)

## Code validation

The HTML, CSS and JS code was run through code validation to detect any errors.

### HTML validation

The W3C Markup validation service was used to check the quality of the HTML language used however the site advised me that the tool is an ongoing experiment in better HTML checking, and its behavior remains subject to change. This resulted in constant fatal errors occuring, I believe, due to the templating language used and therefore cannot be utilised at this time.

### CSS validation

The W3C CSS validation service was used to check the quality of the CSS used. The results are show here: 

- [W3C_CSS](https://chris-m-ecommerce.s3.amazonaws.com/media/images/W3C_CSS.JPG)

### JS validation

The written in the main.js and plot.js files was run through JSHint with no major errors as follows:

- [JSHint_main.js](https://chris-m-ecommerce.s3.amazonaws.com/media/images/JS_HINT_main.JPG)
- [JSHint_plot.js](https://chris-m-ecommerce.s3.amazonaws.com/media/images/JS_HINT_plot.JPG)

## Deployment

To deploy the application to Heroku firstly, a new project was created in Heroku. A Procfile was created which was used to tell Heroku how to run the application. In addition to this a requirements.txt file was created which told Heroku which Python modules were needed to run the application. In addition to this, environment variables had to be configured in Heroku. This was achieved by going to the project settings in Heroku and manually inputting the environment variables to be used by the application such as AWS S3 bucket settings; email settings; and the database url. In addition to this, for security within Django, a secret key for the application was also added to these variables. 

The project was deployed to Heroku by going to the deploy tab and manually deploying the master branch of the project's GitHub repository. Once the project was successfully deployed, the project was opened by clicking the 'view app' button in Heroku: this was achieved with a minimal number of issues.

There is no difference between the deployed and development versions of the application other than in development version debug is set to 'True' whereas in deployment debug is set to 'False'. The site can be accessed here [GymStuff.com](https://gymstuff.herokuapp.com/).

### Credits

The following websites were used for guidance and code snippets used within this application:

- [Django Documentation](https://docs.djangoproject.com/en/3.1/)
- [Code Insitute Ecommerce Account app](https://github.com/Code-Institute-Solutions/e-commerce/tree/master/2-Completed_Project/accounts)
- [Code Insitute Ecommerce Cart app](https://github.com/Code-Institute-Solutions/e-commerce/tree/master/2-Completed_Project/cart)
- [Code Insitute Ecommerce Checkout app](https://github.com/Code-Institute-Solutions/e-commerce/tree/master/2-Completed_Project/checkout)
- [Code Insitute Ecommerce Product app](https://github.com/Code-Institute-Solutions/e-commerce/tree/master/2-Completed_Project/products)
- [Django wine review website](https://www.codementor.io/@jadianes/get-started-with-django-building-recommendation-review-app-du107yb1a)
- [BMI calculator](https://patient.info/doctor/bmi-calculator-calculator)
- [Macro calculator](https://www.menshealth.com/uk/nutrition/a29366026/macro-calculator-keto-bodybuilding/)
- [Amazon](https://www.amazon.co.uk/)

### Media

The background image used on the website was obtained from Pexels (https://images.pexels.com/photos/669582/pexels-photo-669582.jpeg?cs=srgb&dl=pexels-lukas-669582.jpg&fm=jpg).


