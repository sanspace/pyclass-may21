# Day 04

## Topics

  - Python Basics
    - range()
    - else clause on loops
    - f-strings
    - Functions
      - return
      - default args
      - *args

## Refer

  - https://docs.python.org/3/tutorial/controlflow.html#the-range-function
  - https://docs.python.org/3/tutorial/controlflow.html#break-and-continue-statements-and-else-clauses-on-loops
  - https://docs.python.org/3/tutorial/controlflow.html#defining-functions
  - https://docs.python.org/3/reference/lexical_analysis.html#formatted-string-literals

## Practice
  - else
    - write a loop with an else clause being invoked
    - now modify the program so the else clause doesn't run
  - write a function that accepts N and prints 5 multiples of N 
    - get_multiple(5) should print `5 10 15 20 25`. you'll have to work with range and a bit of custom logic to figure out the stop value.In case of get_multiples(3), output should be `3 6 9 12 15`. N can be any positive int. not just 3 or 5.
  - rewrite yesterday's programs to use f-strings wherever applicable
  - write a product function that produces product of its args. It should accept any number of args
    - get_product(1, 2, 3) outputs 6
    - get_product(5, 20) outputs 25
    - get_product() outputs 1
  - write an add function that returns some of two numbers. Accept an optional third parameter that can make it print the output too.
    - add(2, 3) should return 5
    - add(2, 3, True) should print 5 to the screen and return 5

## Extra Mile

  - try writing your own print/sum/range
    - name 'em differently like print_ so they don't cause conflict with the built-in versions


