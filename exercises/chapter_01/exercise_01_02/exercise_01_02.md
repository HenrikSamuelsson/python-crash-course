**Hello World Typos**  
Some examples of erroneous code:

```python  
printt("Hello Python world!")  
```  
NameError: name 'printt' is not defined

```python  
print(Hello Python world!)  
```  
SyntaxError: invalid syntax

```python  
print[Hello Python world!]  
```  
TypeError: 'builtin_function_or_method' object is not subscriptable  

Example that runs but is inccorrect:  

```python  
print("Hello Python world!");  
```
Python uses the ; as a separator, not a terminator. You can also use them at the end of a line, which makes them look like a statement terminator, but this is legal only because blank statements are legal in Python. A line that contains a semicolon at the end is two statements, the second one blank.  
