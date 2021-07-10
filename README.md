# Match Finder
Getting a JSON file from *https://mach-eight.uc.r.appspot.com/* to find a list of all pairs of players
whose height in inches adds up to the integer input to the application.

# Getting Started
## Commands 
  ```
  x      : Close
  exit   : Close
  test   : Run the testing module
  number : Find the matches
  ```
## Prerequisites
Python version 3.8

>*Run the file called 'requirements.txt'*
  ```sh
  [app path]/pip install -r requirements.txt 
  ```
Or just intstall the packages manually:
>*Requests*
  ```sh
  pip install requests
  ```
## Installation
>*Run example*
  ```sh
    [app folder]/python app.py
    Welcome to Match finder - Type 'x' or 'exit' to close
    --- Type 'test' for testing
    >139

    Please enter a number: 139
    Brevin Knight  Nate Robinson
    Mike Wilks  Nate Robinson
  ```
## Testing
>*Running testing module*
 ```sh
    [app folder]/python app.py
    Welcome to Match finder - Type 'x' or 'exit' to close
    --- Type 'test' for testing
    >test
    
    Please enter a number: test
    Getting the item 800 to simulate a index out of range exception
    .Set the number to 5000
    .Set the number to 139
    Brevin Knight  Nate Robinson
    Mike Wilks  Nate Robinson
    .
    ----------------------------------------------------------------------
    Ran 3 tests in 0.016s

    OK
  ```