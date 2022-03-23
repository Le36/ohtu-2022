*** Settings ***
Resource  resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser
Test Setup  Go To register page

*** Test Cases ***
Register With Valid Username And Password
    Set Username  kalle3
    Set Password  kalle456
    set confirm  kalle456
    Submit Credentials
    welcome page should be open

Register With Too Short Username And Valid Password
    Set Username  ka
    Set Password  kalle456
    set confirm  kalle456
    Submit Credentials
    register should fail with message  Username too short

Register With Valid Username And Too Short Password
    Set Username  kalle4
    Set Password  kalle
    set confirm  kalle
    Submit Credentials
    register should fail with message  Password too short

Register With Nonmatching Password And Password Confirmation
    Set Username  kalle4
    Set Password  kalle1234
    set confirm  kalle4321
    Submit Credentials
    register should fail with message  Passwords needs to be matching

Login After Successful Registration
    Set Username  kalle35
    Set Password  kalle456
    set confirm  kalle456
    Submit Credentials
    welcome page should be open
    Click Link  Continue to main page
    Click Button  Logout
    Set Username  kalle35
    Set Password  kalle456
    Click Button  Login
    Login Should Succeed

Login After Failed Registration
    Set Username  kalle352
    Set Password  kalle456
    set confirm  kalle456333
    Submit Credentials
    Click Link  Login
    Set Username  kalle352
    Set Password  kalle456
    Click Button  Login
    login should fail with message  Invalid username or password

*** Keywords ***
Submit Credentials
    Click Button  Register

Set Username
    [Arguments]  ${username}
    Input Text  username  ${username}

Set Password
    [Arguments]  ${password}
    Input Password  password  ${password}

set confirm
    [Arguments]  ${password}
    Input Password  password_confirmation  ${password}

register should fail with message
    [Arguments]  ${message}
    register page should be open
    Page Should Contain  ${message}

Login Should Succeed
    Main Page Should Be Open

Login Should Fail With Message
    [Arguments]  ${message}
    Login Page Should Be Open
    Page Should Contain  ${message}