## Conditional Statements
Used for decision-making operations based on the condition.

## Condition
An expression that evaluates to produce a result which is a Boolean value(T/F)

```python
if(CONDITION):
  BODY STATEMENT

else:
  BODY STATEMENT
```
Python relies on indentation to define scope

### Elif

`elif` allows us to add more than one condition to our `if` blocks

Conditional Statements always start with `if` header, `elif` is optional, but we can have as many as we want. `else` is also optional can only have 1 else for every `if`

Ex. 
```python
month = 2
if(month== 1)
   print("January")
elif(month == 2):
   print("Fedruary")
elif(month == 3):
  print("March")
elif(month == 4):
  print("April")
else:
  print("The month is between May and Decemeber")

 ```