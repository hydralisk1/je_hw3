# HW3.

## 0. Repeat everything I coded during the class. ```done``` 
Materials:
Start looking at interview prep file: Interview Q&A
Read about Behave: https://behave.readthedocs.io/en/latest/gherkin.html

## 1. Find the most optimal locators for Create Account (Registration) page elements: ```done```
```
    - Amazon Logo: XPATH - "//i[@aria-label='Amazon' and @role='img']"
    - "Create Account" text: XPATH - "//h1[@class='a-spacing-small']"
    - Name input field: XPATH - "//input[@name='customerName']"
    - Email input field: XPATH - "//input[@name='email']"
    - Password input field: XPATH - "//input[@name='password']"
    - Password rule message: XPATH - "//div[@class='a-alert-content']"
    - Re-enter password input field: XPATH - "//input[@name='passwordCheck']"
    - Create account button: XPATH - "//input[@type='submit']"
    - "Conditions of use" link: XPATH - "//a[@href='/gp/help/customer/display.html/ref=ap_register_notification_condition_of_use?ie=UTF8&nodeId=508088']"
    - "Privacy notice" link: XPATH - "//a[@href='/gp/help/customer/display.html/ref=ap_register_notification_privacy_notice?ie=UTF8&nodeId=468496']"
    - "Sign in" link: XPATH - "//a[@href='/ap/signin?openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Fwww.amazon.com%2F%3Fref_%3Dnav_custrec_signin&prevRID=Z2HP2D3W68EECACNH07N&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.assoc_handle=usflex&openid.mode=checkid_setup&failedSignInCount=0&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&pageId=usflex&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0']"
```
## 2. Update a test case for support search using BDD ```done```
User can search for Cancelling an order on Amazon (test case from Ex 2 of HW2)
``` 
    - features/tests/cancel_order_amazon.feature
```

## 3. Create a test case using BDD that opens amazon.com, clicks on the cart icon and verifies that Your Shopping Cart is empty. ```done```
```
    - features/amazon_shopping_cart.feature
```

## 4* [Not required] Creative! ```done``` 
Create your own test case to add any product you want into the cart, and make sure it’s there (check for the number of items in the cart OR open the cart and verify it’s there, up to you!)
```
    - features/tests/search_for_covid19.feature
    - Feature: Test Scenarios for user googles COVID 19 and verifies COVID 19 alert on the search result page
```

## 5* Codewars, solve this kata: https://www.codewars.com/kata/57eadb7ecd143f4c9c0000a3 ```done```
```
    - https://www.codewars.com/users/hydralisk1/completed_solutions 
```

Submit your homework from the course dashboard
Note: submit by February 6, 2021

How to submit your homework in LMS:

1. Open the necessary lesson with homework.
2. Press Submit assignment.
3. Add your comment in the Comment field if you need it.
4. Add the link to your homework with opened Commenter rights.