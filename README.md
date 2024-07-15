# Part 7

## Accompanying resources
* Slide deck: https://zipcoder.github.io/reveal-slides.data-engineering/zcw_content/python/fundamentals-part7.html

## Exercise 1

Open the program called *multilingual_greeter.py*

* For each function, remove the line containing the pass statement and implement the functionality described in the docstrings.
* Run the unit tests to validate that the implementation passes unit tests.

```
python3 -m unittest test_multilingual_greeter.py
```

Once all tests are passing, you should be able to run the program.
![multilingual_greeter](multilingual_greeter_sample.gif)

## Exercise 2

Create a program called *multilingual_greeter_v2.py*

Extend the functionality from exercise 1 so it meets the following requirements:
* When the application is executed, the user is prompted for admin mode or user mode.
* In admin mode, the user is given the choice perform the following actions:
  * Add support for additional languages.
  * Update greetings for existing languages.
* Be sure to create tests for all new functionality.
* Be sure to enhance existing tests where appropriate.


## Exercise 3

Create a program called *multilingual_greeter_v3.py*

Extend the functionality from exercise 2 to meet the following requirements:
* Each key in the greetings dictionary is associated with a list rather than a string. 
* Each list should contain at least 3 greetings per language. 
* The greet function will select a random item from the list when invoked.
* Ensure appropriate support for these new features while in admin mode.
* As always, be sure to include appropriate test coverage. 
