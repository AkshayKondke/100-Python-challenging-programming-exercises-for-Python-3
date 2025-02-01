# 📖 Challenge 5: Class-Based String Manipulation

## 🚀 Overview
This challenge focuses on creating a Python class to perform basic string operations, including accepting user input and converting it to uppercase.

## 🎯 Problem Statement
You need to define a class with the following methods:
- **`getString(self)`** 📝: Accepts a string input from the user.
- **`printString(self)`** 🔠: Prints the stored string in **uppercase**.

Additionally, implement a **test function** to verify the class methods.

## 💡 Hints
- Use the `__init__` method to initialize necessary attributes.
- Ensure that the string is properly stored and retrieved before conversion.

## ✅ Solution
```python
class StringManipulator:
    def __init__(self):
        self.text = ""
    
    def getString(self):
        self.text = input("Enter a string: ")
    
    def printString(self):
        print("Uppercase String:", self.text.upper())

# Test function
def test_class():
    obj = StringManipulator()
    obj.getString()
    print("Output:")
    obj.printString()

# Uncomment the below line to test the function interactively
test_class()
```

## 📝 Example Usage
```
Enter a string: hello world
Output:
Uppercase String: HELLO WORLD
```

## 🎯 Learning Outcomes
- Understand the basics of **class definition** in Python.
- Learn how to **initialize attributes** using `__init__`.
- Practice **taking user input and manipulating strings**.

📌 **Happy Coding! 🚀**