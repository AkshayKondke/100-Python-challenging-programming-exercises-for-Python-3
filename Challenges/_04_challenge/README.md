# 📌 Convert Input to List & Tuple

This is a simple Python script 🐍 that takes a comma-separated input from the user and converts it into both a **list** and a **tuple**.

## 📜 How It Works

1. The user is prompted to enter values separated by commas.
2. The script splits the input string into a list.
3. The list is then converted into a tuple.
4. Finally, both the list and tuple are displayed as output.

## 🛠 Code Explanation

```python
num = input("Enter the number in comma-seperation: ")

n = num.split(", ")  # Splitting input into a list

tup = tuple(n)  # Converting list into a tuple

print(f"List values: {n}")  # Displaying list
print(f"Tuple values: {tup}")  # Displaying tuple
```

## 🚀 How to Run

1. Make sure you have **Python 3** installed. 🐍
2. Copy the script and save it as `script.py`.
3. Open a terminal/command prompt and navigate to the script location.
4. Run the script using:
   ```bash
   python main.py
   ```
5. Enter comma-separated values when prompted, e.g., `1, 2, 3, 4`.
6. View the converted **list** and **tuple** in the output. 🎉

## 📂 GitHub Upload Guide

To upload this project on GitHub:

1. Initialize a Git repository:
   ```bash
   git init
   ```
2. Add the files:
   ```bash
   git add script.py README.md
   ```
3. Commit the changes:
   ```bash
   git commit -m "Added script and README"
   ```
4. Create a new repository on GitHub (via the website).
5. Link your local repo to GitHub:
   ```bash
   git remote add origin https://github.com/AkshayKondke/100-Python-challenging-programming-exercises-for-Python-3.git
   ```
6. Push the files:
   ```bash
   git push -u origin main
   ```

✅ Done! Your project is now on GitHub. 🚀