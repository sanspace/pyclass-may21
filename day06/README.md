# Day 06

## Topics

  - Python Basics
    - exception handling
    - classes
    - working with files

## Refer

  - https://docs.python.org/3/tutorial/errors.html
  - https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files
  - https://docs.python.org/3/tutorial/classes.html

## Practice

  - Modify the guessing game program to
    - add error handling for non numeric inputs
    - Raise a NoMoreGuessesError when the user is out of guesses
    - create a report file at the end of the game that has the original number, user's each guesses and the final result if the user won or not.
      - for each game use a new file and use the current timestamp in the file name (like game-timestamp.txt)
      - do play the game few times to generate files
  - Write a program to process the file created above
    - traverse through the current directory (find out how)
    - read each game file (you should have used a nameprefix to identify game files)
    - print a list of results
    - print a list of original numbers

## Extra Mile

  - create  class that mimics the behavior of a stack
    - limit it to integers alone
    - have an upper limit for stack, it shouldn't hold more than N items
    - raise an error if user tries to pop an empty stack
    - leverage list's pop function for your pop method
