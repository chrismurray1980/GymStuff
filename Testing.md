# Milestone Project 5 : Testing

The testing conducted to verify the functionality of the website consisted of both automated testing and manual testing, using various screen sizes and web browsers ( safari, firefox and chrome). Continuous integration testing was undertaken using Travis CI with the results of these tests shown as passed in the Readme.md document for this project.

## Running automated tests

Automated unit testing was conducted on each of the apps. This was undertaken by running the following command:

    $python3 manage.py test <app name>


## Manual testing

Testing was also conducted manually on each of the website pages and overall functionality verified.


### Tests conducted on navbar

The following tests were conducted on the site navbar on all pages of the site:

| Test          | Functionality| Result  |
| ------------- |:--------------:| -----:|
| 1             | Clicking site logo on all pages returns landing page|pass|
| 2             | Clicking bmi calculator or macro calculator link on all pages when not logged-in redirects to login page then to the correct calculator page|pass|
|3          	|Clicking bmi or macro calculator on all pages when logged-in redirects to the correct calculator page |pass|
|4          	|Log-in and register links visible on accounts dropdown when not logged in|pass|
|5              |Log-out visible on accounts dropdown when logged in|pass|
|7              |Clicking register renders register form on all pages|pass|
|8              |Clicking log-out logs out user and redirects to landing page on all pages|pass|
|9              |Clicking on products link redirects to correct products on all pages|pass|


### Tests conducted on landing page

The following tests were undertaken on the landing page:

| Test          | Functionality| Result  |
| ------------- |:--------------:| -----:|
|1              |Page is rendered on accessing the site|pass|
|2              |Three most expensive product for each category shown|pass|
|3          	|'view product' link takes you to product page|pass|
|4          	|'view similar' products button shows all products from that category|pass|
|5              |'home' button at bottom of page takes user to landing page|pass|


### Tests conducted on product page

The following test were undertaken on the product page:

| Test          | Functionality| Result  |
| ------------- |:--------------:| -----:|
|1              |Correct information presented for product|pass|
|2              |Clicking the 'add' button adds quantity to cart and returns user to product page|pass|
|3          	|'view reviews' button displays reviews for product|pass|
|4          	|Clicking 'add review ' button shows add review form|pass|
|5              |Clicking 'submit review' button submits review and returns user to product page|pass|
|7              |If user not logged in 'add review' button not visible|pass|
|8              |'home' button at bottom of page takes user to landing page|pass|


### Tests conducted on product category page

The following tests were undertaken on the product category page:

| Test          | Functionality| Result  |
| ------------- |:--------------:| -----:|
|1              |All products of this category shown|pass|
|2              |Products listed from cheapest to most expensive|pass|
|3          	|'view product' link takes you to product page|pass|
|4              |'home' button at bottom of page takes user to landing page|pass|

### Tests conducted on Macro and BMI forms

The following tests were undertaken on the macro and bmi form pages:

| Test          | Functionality| Result  |
| ------------- |:--------------:| -----:|
|1              |Forms correctly displayed|pass|
|2              |Clicking 'calculate' button displays correct results|pass|
|3          	|When form field blank are incorrect page is reloaded and error message displayed|pass|

### Tests conducted on login page

The following test were undertaken on the log-in page:

| Test          | Functionality| Result  |
| ------------- |:--------------:| -----:|
|1              |Log-in page rendered on 'log-in' button click|pass|
|2              |Log-in page rendered when unauthorised user attempts to access page which requires authorisation|pass|
|3          	|User logged in when correct details given and 'log-in' button clicked and success message displayed|pass|
|4              |Log-in page re-rendered when password is incorrect on 'log-in' button click and error message displayed|pass|

### Tests conducted on search functionality

The following test were undertaken on the search functionality:

| Test          | Functionality| Result  |
| ------------- |:--------------:| -----:|
|1              |Type 'dumbbell' into the search box and submit. Products containing 'dumbbell' returned|pass|
|2              |Type 'weights' into the search box and submit. Products in 'weights' category returned|pass|


### Test conducted at various screen resolutions

The following test were undertaken on the sites screen size responsiveness:


| Test          | Functionality| Result  |
| ------------- |:--------------:| -----:|
|1              |Font adjusts at media breakpoints as defined by CSS|pass|
|2              |Bootstrap grid system automatically adjusts at specified breakpoints as per html definition|pass|
|3              |Element padding and margins adjust correctly at media breakpoints as per CSS|pass|
|4              |Background image becomes visible at large screen breakpoint and margin varies accordingly|pass|
