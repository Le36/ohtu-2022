*** Settings ***
Resource  resource.robot
Test Setup  Create User And Input New Command

*** Test Cases ***
Register With Valid Username And Password
    input credentials  kalle3  kall33gfdsagfd3
    Output Should Contain  New user registered

Register With Already Taken Username And Valid Password
    input credentials  kalle  kalle123
    Output Should Contain  User with username kalle already exists

Register With Too Short Username And Valid Password
    input credentials  ka  kall3333
    Output Should Contain  Username too short

Register With Valid Username And Too Short Password
    input credentials  kalle3  kall33
    Output Should Contain  Password too short

Register With Valid Username And Long Enough Password Containing Only Letters
    input credentials  kalle3  kalleeee
    Output Should Contain  Password needs to have at least 1 digit

*** Keywords ***
Create User And Input New Command
    Create User  kalle  kalle123
    input new command
