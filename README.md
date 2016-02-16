# Underscore.py

This is a Python implementation of the JavaScript utility library [underscore.js](http://underscorejs.org/). Underscore.js helps programmers write JavaScript programs in a functional manner. 

## Functional Programming Principles

I aimed to use Functional Programming principles when implementing the functions. Below are the most important ones I was mindful of: 
- Using map and reduce instead of loops for iterating over a list of elements.
- Not mutating variables that were passed into a function as a parameter. In other words, calling a function never has a side-effect.
- Using higher-order functions and anonymous functions to make code more declarative and easier to reason about.

Typically, functional programming makes extensive use of recursion. This is not ideal in Python due to the lack of tail call optimization. Therefore I wrote both recursive and non-recursive versions of a few functions just for fun. 

## To Use

All of the functions under the "collections" heading have been implemented except for indexBy and toArray. Function names and parameters are identical to their JavaScript counterparts. The functions work with Python lists. 

