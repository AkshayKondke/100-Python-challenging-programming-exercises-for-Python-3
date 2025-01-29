
# 📌 Factorial of a Number - README

## 📝 Problem Statement
**Compute the Factorial of a Number**

Factorial of a non-negative integer *n* is the product of all positive integers from *1* to *n*. It is represented as:

```
n! = n × (n-1) × (n-2) × ... × 1
```

For example:
```
5! = 5 × 4 × 3 × 2 × 1 = 120
```

---

## ✅ Solution Approaches
We provide two methods to calculate the factorial of a given number:

1️⃣ **Normal (Iterative) Method** 🏗️
2️⃣ **Recursive Method** 🔄

---

## 📜 Solution Explanation

### 🏗️ Normal Method (Using Loop)
- Initialize `factorial = 1`.
- Use a `for` loop from `1` to `n`.
- Multiply `factorial` by the loop variable in each iteration.
- Print the final factorial value.

#### **Code:**
```python
num = int(input("Enter a number: "))

factorial = 1

for i in range(1, num + 1):
    factorial *= i

print(f"Factorial calculation from normal method  : {factorial}")
```

#### **Time Complexity:**
⏳ **O(n)** (Linear Complexity)

---

### 🔄 Recursive Method (Using Recursion)
- Base Case: If `num == 0` or `num == 1`, return `1`.
- Recursive Step: Multiply `num` with `fact_cal(num - 1)`.
- This function keeps calling itself until the base case is reached.

#### **Code:**
```python
def fact_cal(num):
    if num == 0 or num == 1:
        return 1
    
    return num * fact_cal(num - 1)

print(f"Factorial calculation from Recursive method: {fact_cal(num)}")
```

#### **Time Complexity:**
⏳ **O(n)** (Linear Complexity due to recursive calls)

#### **Space Complexity:**
📦 **O(n)** (Due to recursive function call stack)

---

## 🛠️ Step-by-Step Execution
1️⃣ **User Input**: Enter a number (e.g., `5`).
2️⃣ **Normal Method Execution**:
   - Initialize `factorial = 1`.
   - Loop multiplies values up to `n`.
   - Prints the result (`120`).
3️⃣ **Recursive Method Execution**:
   - Calls `fact_cal(num)`.
   - Recursively multiplies `n × (n-1) × ... × 1`.
   - Returns the result (`120`).

---

## 🎯 Example Execution
### **Input:**
```
Enter a number: 5
```

### **Output:**
```
Factorial calculation from normal method  : 120
Factorial calculation from Recursive method: 120
```

---

## 🏆 Conclusion
- The **normal method** is simple and avoids recursion overhead.
- The **recursive method** is concise but may cause a **stack overflow** for large numbers.

Choose the method based on your use case! 🚀

