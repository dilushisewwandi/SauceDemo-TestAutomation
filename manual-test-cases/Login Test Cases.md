Test Case ID     : TC_001_Login  

Title            : Login with Valid Credentials 
 
Preconditions    : User is on the SauceDemo login page  

Test Steps       :
  1. Enter username as "standard_user"
  2. Enter password as "secret_sauce"
  3. Click the "Login" button  

Test Data        :
  • Username: standard_user  
  • Password: secret_sauce  

Expected Result  : User should be logged in successfully and navigated to the Inventory page (URL contains 'inventory.html')  

Actual Result    : Login was successful and navigated to the Inventory page as expected  

Status           : Pass



Test Case ID     : TC_002_Login
  
Title            : Login with Incorrect Username  

Preconditions    : User is on the SauceDemo login page  

Test Steps       :
  1. Enter username as "incorrect"
  2. Enter password as "secret_sauce"
  3. Click the "Login" button  

Test Data        :
  • Username: incorrect  
  • Password: secret_sauce  

Expected Result  : 
  • User should not be logged in successfully
  • An error message should be displayed as "Username and password do not match any user in this service" 
  • User should not be navigated to the Inventory page (URL should not    contain'inventory.html')   

Actual Result    :  
  • Login was not successful  
  • An error message was displayed as expected
  • User was not navigated to the Inventory page 

Status           : Pass



Test Case ID     : TC_003_Login
  
Title            : Login with Incorrect Password  

Preconditions    : User is on the SauceDemo login page  

Test Steps       :
  1. Enter username as "standard_user"
  2. Enter password as "incorrect"
  3. Click the "Login" button  

Test Data        :
  • Username: standard_user
  • Password: incorrect  

Expected Result  : 
  • User should not be logged in successfully
  • An error message should be displayed as "Username and password do not match any user in this service"
  • User should not be navigated to the Inventory page (URL should not    contain'inventory.html')   

Actual Result    :  
  • Login was not successful  
  • An error message was displayed as expected 
  • User was not navigated to the Inventory page 

Status           : Pass



Test Case ID     : TC_004_Login
  
Title            : Login with Empty Fields  

Preconditions    : User is on the SauceDemo login page  

Test Steps       : Click the "Login" button  

Test Data        :
  • Username: 
  • Password: 

Expected Result  : 
  • User should not be logged in successfully
  • An error message should be displayed as "Username is required"
  • User should not be navigated to the Inventory page (URL should not    contain'inventory.html')   

Actual Result    :  
  • Login was not successful  
  • An error message was displayed as expected
  • User was not navigated to the Inventory page 

Status           : Pass



Test Case ID     : TC_005_Login
  
Title            : Login with Lockedout User  

Preconditions    : User is on the SauceDemo login page  

Test Steps       :
  1. Enter username as "locked_out_user"
  2. Enter password as "secret_sauce"
  3. Click the "Login" button  

Test Data        :
  • Username: locked_out_user  
  • Password: secret_sauce  

Expected Result  : 
  • User should not be logged in successfully
  • An error message should be displayed as "Sorry, this user has been locked out."
  • User should not be navigated to the Inventory page (URL should not    contain'inventory.html')   

Actual Result    :  
  • Login was not successful  
  • An error message was displayed as expected
  • User was not navigated to the Inventory page 

Status           : Pass
