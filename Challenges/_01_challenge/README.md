# 🏆 Challenge: Find Numbers Divisible by 7 but Not 5

## 🔍 Problem Statement
Write a Python program that finds all numbers **divisible by 7 but not a multiple of 5** in the range **2000 to 3200 (both included)**.

## 📌 Requirements
- The program should iterate through numbers in the given range.
- It should check for numbers that are:
  - ✅ **Divisible by 7**
  - ❌ **Not divisible by 5**
- The output should be a **comma-separated sequence** of valid numbers, printed on a single line.

## 🚀 Sample Output
```
2002,2009,2016,2023,2037,2044,2051,2058,2065,2079,2086,2093,2107,2114,2121,2128...
```

## 💡 Solution Approach
To solve this challenge, follow these steps:

### 1️⃣ Understand the Problem:
We need to find numbers that:
- Are **divisible by 7** (i.e., `num % 7 == 0`)
- Are **not multiples of 5** (i.e., `num % 5 != 0`)
- Belong to the range **2000 to 3200** (both included).

### 2️⃣ Plan the Solution:
- Use a **loop** to iterate through numbers from `2000` to `3200`.
- Use an **if condition** to check both criteria.
- Store the valid numbers in a list.
- Convert the list elements to strings and print them as a **comma-separated** sequence.

### 3️⃣ Code Implementation:
```python
# Create an empty list to store the valid numbers
numbers = []

# Loop through numbers from 2000 to 3200 (both included)
for num in range(2000, 3201):
    # Check if the number is divisible by 7 but NOT by 5
    if num % 7 == 0 and num % 5 != 0:
        numbers.append(str(num))  # Convert the number to a string and add to the list

# Join the numbers with commas and print the result
print(",".join(numbers))
```

### 4️⃣ Explanation of the Code:
- **Step 1:** Create an empty list `numbers` to store the valid values.
- **Step 2:** Use a `for` loop to go through numbers from `2000` to `3200`.
- **Step 3:** Use an `if` statement to check if the number is:
  - Divisible by 7 (`num % 7 == 0`)
  - Not divisible by 5 (`num % 5 != 0`)
- **Step 4:** If the number meets both conditions, convert it to a string and store it in the `numbers` list.
- **Step 5:** After the loop ends, join all elements in the `numbers` list with commas and print the final result.

## 🎯 Key Takeaways
✅ Uses **loops and conditionals** effectively.  
✅ Demonstrates **list operations and string manipulation**.  
✅ Simple, clean, and beginner-friendly Python code.  

## 📌 Notes
- You can modify the range to test other number sets.  
- This approach ensures efficient computation with minimal memory usage.  

---
### 🤖 Happy Coding! 🚀