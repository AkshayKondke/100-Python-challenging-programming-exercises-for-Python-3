# 📌 Challenge 3 - Generate Dictionary of Squares

## 📝 Problem Statement
**With a given integral number `n`, write a program to generate a dictionary that contains (i, i*i) such that `i` is an integral number between `1` and `n` (both included). Then, print the dictionary.**

### 🔹 Example Input:
```
Enter an integer: 8
```

### 🔹 Example Output:
```
{1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64}
```

---

## 📚 Theoretical Knowledge
### 🔹 What is a Dictionary in Python?
A **dictionary** is a built-in data type in Python that stores data in key-value pairs. It allows fast lookups, modifications, and insertions. The syntax is:
```python
my_dict = {key1: value1, key2: value2, ...}
```
For this problem, we use numbers as **keys** and their squares as **values**.

### 🔹 What is a Loop?
A **loop** in Python allows us to iterate over a sequence and perform repetitive tasks. Here, we use a `for` loop to iterate through numbers and store their squares in the dictionary.

---

## ✅ Solution Approach
We provide a detailed, step-by-step solution to solve the problem using loops and dictionaries.

### 🛠️ Step-by-Step Solution

1️⃣ **User Input**:
   - The program prompts the user to enter an integer `n`.
   - Example: If the user enters `8`, then `n = 8`.

2️⃣ **Initialize an Empty Dictionary**:
   - We create an empty dictionary `squares_dict = {}` to store key-value pairs.

3️⃣ **Use a Loop to Generate Squares**:
   - We use a `for` loop to iterate from `1` to `n`.
   - For each `i`, we compute `i * i` and store it in the dictionary.
   - Example iterations:
     - `i = 1` → `{1: 1}`
     - `i = 2` → `{1: 1, 2: 4}`
     - `i = 3` → `{1: 1, 2: 4, 3: 9}`
     - ... (continues until `n`)

4️⃣ **Print the Final Dictionary**:
   - After the loop completes, we print the dictionary.
   - Example output for `n = 8`:
     ```
     {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64}
     ```

---

## 📜 Python Solution
```python
# 📌 Generate a dictionary with squares of numbers

# Step 1: Take input from the user
n = int(input("Enter an integer: "))

# Step 2: Initialize an empty dictionary
squares_dict = {}

# Step 3: Use a loop to generate key-value pairs
for i in range(1, n + 1):  # Loop from 1 to n (inclusive)
    squares_dict[i] = i * i  # Assign key as 'i' and value as 'i squared'

# Step 4: Print the final dictionary
print(squares_dict)
```

---

## ⏳ Time Complexity
- **O(n)** (Linear complexity since we iterate from `1` to `n` once).

## 📦 Space Complexity
- **O(n)** (Storing `n` key-value pairs in the dictionary).

---

## 🎯 Summary
- We used a loop to generate dictionary key-value pairs.
- The dictionary stores numbers as keys and their squares as values.
- Finally, we print the dictionary to display the result.

🚀 **This approach is simple, efficient, and beginner-friendly!**

