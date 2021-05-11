# Day 07

## Topics

  - Python Basics
    - Classes
      - Inheritance
    - Third Party packages
    - Comprehensions
    - Iterators

## Refer

  - https://docs.python.org/3/tutorial/stdlib.html
  - https://docs.python.org/3/tutorial/stdlib2.html
  - https://docs.python.org/3/tutorial/venv.html
  - https://docs.python.org/3/tutorial/classes.html#iterators


## Practice

  - Demonstrate subclassing using your favorite usecase
  - Demo virtual env using your favorite package from PyPI
    - you should use a venv
    - this should be a separate repo in github
    - I should be able to fork your repo, install your requirements.txt and run your code successfully
  - Write programs to demonstrate options from stdlib
    - Write a program that accepts command line args and outputs the args and their position in the form of a dict (use dict comprehension)
    - Write a program that can traverse your current directory and print only python file names. (use os and glob if applicable)
    - Showcase doctest for one of your existing programs
    - Implement a program to showcase one item from collections module
    - Implement a program to showcase one item from itertools module
    - Note: Do not just copy the exisiting examples. Try to come up with your own or modify it a bit to show case your understanding of it.
  - Comprehension exercises
    - Given a list ['a', 'b', ...], make a dict of elements along with their position like {0: a, 1: b ... }
    - Do list comprehension to get odd numbers' squares from this list: [1, 3, 3, 4, 5, 6]
  - Demostrate Iterator Protocol using your favorite usecase

## Extra Mile
  - Try list comp to get keys that are longer than 4 chars in a dict. (notice you're making a list out of a dict)
  - implement nested list comp in any use case
