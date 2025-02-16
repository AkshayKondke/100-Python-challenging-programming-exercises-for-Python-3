# 🚀 Challenge 06 - Python Math Calculation

## 📌 Introduction
Welcome to **Challenge 06**! 🎯 This Python program calculates values based on a given mathematical formula using user input. The formula used is:

\[ Q = \sqrt{\frac{2 * C * D}{H}} \]

where:
- **C** = 50 (constant)
- **H** = 30 (constant)
- **D** = User input (comma-separated values)

## 🛠️ How It Works
1. The program prompts the user to enter values for **D** (comma-separated).
2. It calculates the value of **Q** for each **D** using the given formula.
3. The result is displayed as a comma-separated list of integers.

## 🏗️ Installation & Usage
1. Make sure you have **Python 3** installed on your system.
2. Copy and paste the following code into a new Python file (`challenge_06.py`):

```python
import math

print("----------------------||||||||||||||||||--------------------------")
print("\n")
print("\t \tWelcome to the challenge no 06.")

C = 50
H = 30

D_value = input("Enter the value of the D variable for comma separated value: ").split(",")

Q_value = [round(math.sqrt((2 * C * int(D)) / H)) for D in D_value]

print(",".join(map(str, Q_value)))
```

3. Run the script using:
   ```bash
   python challenge_06.py
   ```
4. Enter comma-separated values when prompted.
5. The calculated values of **Q** will be displayed. ✅

## 📖 Example
**Input:**
```
Enter the value of the D variable for comma separated value: 100,150,180
```
**Output:**
```
8,10,11
```

## 🔥 Features
✅ Simple & easy to use  
✅ Uses **math.sqrt()** for accurate calculations  
✅ Supports multiple inputs in a single execution  
✅ Rounds values for better readability  

## 🤝 Contributing
Feel free to modify and improve this script! Contributions are always welcome. 🎉

## 📜 License
This project is **free to use** and open-source. 💡

Happy coding! 🚀

