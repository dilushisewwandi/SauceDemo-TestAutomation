Test Case ID     : TC_006_Product_Listing  

Title            : View all products after login
 
Preconditions    : 
  • User is on the SauceDemo login page
  • User has valid login credentials (standard_user / secret_sauce)  
  
Test Steps       :
  1. Enter username as "standard_user"
  2. Enter password as "secret_sauce"
  3. Click the "Login" button 
  4. Observe the inventory page

Test Data        :
  • Username: standard_user  
  • Password: secret_sauce  

Expected Result  : 
  • User should be navigated to the Inventory page after login
  • Six product items should be displayed 
  • Every product should show 
  	• Product name
  	• Small description
	  • Price
  	• "Add to Cart" button

Actual Result    : • Six product items were displayed with all expected elements 

Status           : Pass



Test Case ID     : TC_007_Product_Listing  

Title            : View all products with sorting A-Z
 
Preconditions    : 
  • User is on the Inventory page after logging in with valid credentials  
  

Test Steps       :
  1. Enter username as "standard_user"
  2. Enter password as "secret_sauce"
  3. Click the "Login" button 
  4. Observe the inventory page
  5. Select "Name (A-Z)" from the sort drop-down
 
Test Data        :
  • Username: standard_user  
  • Password: secret_sauce  

Expected Result  : 
• Product items should be sorted alphabetically from A-Z
• Each product should be displayed with:
	• Product name
	• Small description
	• Price
	• "Add to Cart" button

Actual Result    : 
• Products were sorted in A–Z order as expected
• All product details were correctly displayed  

Status           : Pass



Test Case ID     : TC_008_Product_Listing  

Title            : View all products with sorting price low-high
 
Preconditions    : 
  • User is on the Inventory page after logging in with valid credentials  
  

Test Steps       :
  1. Enter username as "standard_user"
  2. Enter password as "secret_sauce"
  3. Click the "Login" button 
  4. Observe the inventory page
  5. Select "Price (low-high)" from the sort drop-down
 
Test Data        :
  • Username: standard_user  
  • Password: secret_sauce  

Expected Result  : 
• Product items should be sorted price from low-high
• Each product should be displayed with:
	• Product name
	• Small description
	• Price
	• "Add to Cart" button

Actual Result    : 
• Products were sorted in low-high order as expected
• All product details were correctly displayed  

Status           : Pass



