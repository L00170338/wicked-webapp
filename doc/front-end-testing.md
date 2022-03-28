
Front End testing
============

The front end is the client-side section of a program. We can say that it 
involves everything visible while using an application. Every web application 
has a three-tier architecture. It includes clients, servers, and information 
systems or resources. The presentation layer comprises the client. Front end 
testers test this layer. They perform GUI testing and test usability and how 
a site or application works.*

To perform Front End testing on the Project the [Selenium Webdriver](https://www.selenium.dev/documentation/) was used.
The test is performed as part of `front-end-testing.yml` workflow. During this workflow run a `Docker` image is generated
from the Project on push to `Dev` branch of the repo. Once this part is done, then the python file `Front-end-tester.py`.

### The following tests scenarios are done to confirm the Project is in a working condition: ###
 * The code checks if the Search field presents on the main page of the Web-App
 * A text inserted into that field and the search button is pressed.
 * The test scrip press to `Register` button on the main page of the Web-App
 * It types in all required values into fields for a new user registration and hits `Submit`
 * It logs out from the user account, and tries to login back with the same credentials
 * If the test script can find `Add profile` button, this means the login was successful
 * Test has PASSED.

Part of the test code is demontrated below:

~~~python
def check_register():
    '''
        This function checks if the user can get registered.
        If it successful, then function 'check_login()' uses
        same credentials to check if the user can get logged in.
    '''
    home_button = driver.find_element(By.CSS_SELECTOR, ".material-icons-outlined")
    home_button.click()
    time.sleep(1)

    register_button = driver.find_element(By.NAME, "base_register_btn")
    register_button.click()
    time.sleep(1)

    username_filed = driver.find_element(By.ID, "username")
    username_filed.send_keys("seleniumtester")
    time.sleep(1)
~~~
*Note 1: The first paragraph is taken from* [here](https://www.testim.io/blog/front-end-testing-complete-overview/)

This page is created by L00169827
