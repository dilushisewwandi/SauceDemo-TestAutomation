Test Case ID     : TC_009_Add_to_Cart

Title            : Add a Single Item to the Cart
 
Preconditions    : 
  • User is on the SauceDemo login page
  • User has valid login credentials (standard_user / secret_sauce)  
  
Test Steps       :
  1. Enter username as "standard_user"
  2. Enter password as "secret_sauce"
  3. Click the "Login" button 
  4. Observe the inventory page
  5. Click on the "Add to Cart" button of one item

Test Data        :
  • Username: standard_user  
  • Password: secret_sauce  

Expected Result  : 
  • The clicked product should be added to the cart
  • "Add to Cart" button name should be changed to "Remove"
  • Cart badge should display item count as 1
  	
Actual Result    : • Product added to the cart as expected 

Status           : Pass



Test Case ID     : TC_010_Add_to_Cart

Title            : Add Multiple Items to the Cart
 
Preconditions    : 
  • User is on the SauceDemo login page
  • User has valid login credentials (standard_user / secret_sauce)  
  
Test Steps       :
  1. Enter username as "standard_user"
  2. Enter password as "secret_sauce"
  3. Click the "Login" button 
  4. Observe the inventory page
  5. Click on the "Add to Cart" button for two items

Test Data        :
  • Username: standard_user
  • Password: secret_sauce  

Expected Result  : 
  • The clicked products should be added to the cart
  • "Add to Cart" button names should be changed to "Remove"
  • Cart badge should display item count as 2

Actual Result    : • Two products added to the cart as expected 

Status           : Pass



Test Case ID     : TC_011_Add_to_Cart

Title            : Remove Product Item from the Cart
 
Preconditions    : 
  • User is on the SauceDemo login page
  • User has valid login credentials (standard_user / secret_sauce)
  • An item should have been added to the cart
  
Test Steps       :
  1. Enter username as "standard_user"
  2. Enter password as "secret_sauce"
  3. Click the "Login" button 
  4. Observe the inventory page
  5. Click on the "Add to Cart" button of a item
  6. Click on the cart badge 
  7. Click on the "Remove" button 

Test Data        :
  • Username: standard_user
  • Password: secret_sauce  

Expected Result  : 
  • The clicked product should be removed from the cart
  • "Remove" button should be changed back to "Add to Cart" on the inventory page
  • Cart badge should no longer display item count
  	
Actual Result    : • Product item removed from the cart as expected 

Status           : Pass




Test Case ID     : TC_012_Add_to_Cart

Title            : View Cart
 
Preconditions    : 
  • User is on the SauceDemo login page
  • User has valid login credentials (standard_user / secret_sauce)
  • An item should have been added to the cart
  
Test Steps       :
  1. Enter username as "standard_user"
  2. Enter password as "secret_sauce"
  3. Click the "Login" button 
  4. Observe the inventory page
  5. Click on the "Add to Cart" button of an item
  6. Click on the cart badge 
  

Test Data        :
  • Username: standard_user
  • Password: secret_sauce  

Expected Result  : 
  • The added product should be listed in the cart
  • Product name and price should match what's shown on the Inventory page

Actual Result    : • Product items displayed in the cart as expected 

Status           : Pass