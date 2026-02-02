# kintsugi-stack-python

> “Python doesn’t make you smarter, it removes everything that was making you feel dumb.” - Guido van Rossum

- Author: [Kintsugi-Programmer](https://github.com/kintsugi-programmer)

![alt text](image.png)

> Disclaimer: The content presented here is a curated blend of my personal learning journey, experiences, open-source documentation, and invaluable knowledge gained from diverse sources. I do not claim sole ownership over all the material; this is a community-driven effort to learn, share, and grow together.

## Table of Contents
- [kintsugi-stack-python](#kintsugi-stack-python)
  - [Table of Contents](#table-of-contents)
  - [1. Introduction](#1-introduction)
    - [1.1. repository overview](#11-repository-overview)
    - [1.2. First Example: Welcome message](#12-first-example-welcome-message)
    - [1.3. Your first bug](#13-your-first-bug)
    - [1.4. The console](#14-the-console)
    - [1.5. Why Python](#15-why-python)
    - [1.6. What is code (source code and machine code)](#16-what-is-code-source-code-and-machine-code)
    - [1.7. Syntax and syntax errors](#17-syntax-and-syntax-errors)
  - [2. Variables](#2-variables)
    - [2.1. Variables](#21-variables)
    - [2.2. Math with variables](#22-math-with-variables)
    - [2.3. Comments](#23-comments)
    - [2.4. Naming variables](#24-naming-variables)
    - [2.5. Data types](#25-data-types)
    - [2.6. F-strings](#26-f-strings)
    - [2.7. None type](#27-none-type)
    - [2.8. Dynamic vs static typing](#28-dynamic-vs-static-typing)
    - [2.9. Math with strings](#29-math-with-strings)
    - [2.10. Multivariable declaration](#210-multivariable-declaration)
  - [3. Functions](#3-functions)
    - [3.1. What is a function](#31-what-is-a-function)
    - [3.2. Multiple parameters](#32-multiple-parameters)
    - [3.3. Define before you call](#33-define-before-you-call)
    - [3.4. Entry point (main)](#34-entry-point-main)
    - [3.5. Fahrenheit to Celsius](#35-fahrenheit-to-celsius)
    - [3.6. Functions quiz](#36-functions-quiz)
    - [3.7. Hours to seconds](#37-hours-to-seconds)
    - [3.8. Return vs no return](#38-return-vs-no-return)
    - [3.9. Returning multiple values](#39-returning-multiple-values)
    - [3.10. Parameters vs arguments](#310-parameters-vs-arguments)
    - [3.11. Default parameters](#311-default-parameters)
    - [3.12. Printing vs returning](#312-printing-vs-returning)
  - [4. Scope](#4-scope)
    - [4.1. What is scope](#41-what-is-scope)
    - [4.2. Python and block scope](#42-python-and-block-scope)
    - [4.3. Example (scope bug)](#43-example-scope-bug)
    - [4.4. Global scope](#44-global-scope)
  - [5. Testing and Debugging](#5-testing-and-debugging)
    - [5.1. Unit tests](#51-unit-tests)
    - [5.2. Learning effectively](#52-learning-effectively)
    - [5.3. Debugging](#53-debugging)
    - [5.4. Practice debugging (unlock\_achievement)](#54-practice-debugging-unlock_achievement)
    - [5.5. Stack trace (traceback)](#55-stack-trace-traceback)
  - [6. Computing](#6-computing)
    - [6.1. Numeric types](#61-numeric-types)
    - [6.2. Floor division](#62-floor-division)
    - [6.3. Exponents](#63-exponents)
    - [6.4. Changing in place](#64-changing-in-place)
    - [6.5. In-place operators](#65-in-place-operators)
    - [6.6. Bitwise AND](#66-bitwise-and)
    - [6.7. Bitwise OR](#67-bitwise-or)
    - [6.8. Logical NOT](#68-logical-not)
  - [7. Comparisons](#7-comparisons)
    - [7.1. Comparison](#71-comparison)
    - [7.2. Comparison operators practice](#72-comparison-operators-practice)
    - [7.3. if statements](#73-if-statements)
    - [7.4. if and return (check\_swords\_for\_army)](#74-if-and-return-check_swords_for_army)
    - [7.5. if / elif / else](#75-if--elif--else)
    - [7.6. Boolean logic (does\_attack\_hit)](#76-boolean-logic-does_attack_hit)
    - [7.7. should\_serve\_customer](#77-should_serve_customer)
  - [8. Loops](#8-loops)
    - [8.1. for loops and range](#81-for-loops-and-range)
    - [8.2. Countdown (negative step)](#82-countdown-negative-step)
    - [8.3. Sum and sum of odds](#83-sum-and-sum-of-odds)
  - [9. Lists](#9-lists)
    - [9.1. What is a list](#91-what-is-a-list)
    - [9.2. Adding and indexing](#92-adding-and-indexing)
    - [9.3. get\_inventory](#93-get_inventory)
    - [9.4. Length and last index](#94-length-and-last-index)
    - [9.5. Updating by index (smelt\_ore)](#95-updating-by-index-smelt_ore)
    - [9.6. pop](#96-pop)
    - [9.7. Counting items (get\_item\_count)](#97-counting-items-get_item_count)
    - [9.8. Iterating without index](#98-iterating-without-index)
    - [9.9. Finding an item (e.g. leather scraps)](#99-finding-an-item-eg-leather-scraps)
    - [9.10. Comparing two lists by index](#910-comparing-two-lists-by-index)
    - [9.11. Maximum in a list](#911-maximum-in-a-list)
    - [9.12. Modulo](#912-modulo)
    - [9.13. Slicing](#913-slicing)
    - [9.14. Concatenation](#914-concatenation)
    - [9.15. Deleting from a list](#915-deleting-from-a-list)
    - [9.16. Tuples](#916-tuples)
    - [9.17. First element / error](#917-first-element--error)
    - [9.18. Reverse a list](#918-reverse-a-list)
    - [9.19. Nested loops (filter messages)](#919-nested-loops-filter-messages)
  - [10. Dictionaries](#10-dictionaries)
    - [10.1. What is a dictionary](#101-what-is-a-dictionary)
    - [10.2. Creating and setting](#102-creating-and-setting)
    - [10.3. Accessing and updating](#103-accessing-and-updating)
    - [10.4. in keyword](#104-in-keyword)
    - [10.5. Iterating](#105-iterating)
    - [10.6. Ordered (Python 3.7+)](#106-ordered-python-37)
  - [11. Sets](#11-sets)
    - [11.1. What is a set](#111-what-is-a-set)
    - [11.2. Creating and using](#112-creating-and-using)
    - [11.3. Use cases](#113-use-cases)
  - [12. Errors](#12-errors)
    - [12.1. Syntax errors vs exceptions](#121-syntax-errors-vs-exceptions)
    - [12.2. try / except](#122-try--except)
    - [12.3. Raising exceptions](#123-raising-exceptions)
    - [12.4. Catching specific exceptions](#124-catching-specific-exceptions)
    - [12.5. Review](#125-review)

---

## 1. Introduction

### 1.1. repository overview

- **Python** is one of the most popular programming languages in the world (excluding frontend technologies). It is one of the easiest to learn and is used by millions of developers for **backend development**, **devops**, **data science**, and **AI**.

- This repository teaches **Python** from Stratch. You will not learn everything about Python, but you will learn enough to be effective and build your own projects. The repository also teaches **coding fundamentals** and **computer science basics** that apply to any language (e.g. JavaScript, Go). No prior knowledge is assumed.

### 1.2. First Example: Welcome message

- Task: Write Hello World

```py
print("Hello World")

# for installation: Google

# run command in terminal: python 1_2_.py

# for alias python3 as python:
# echo "alias python=python3" >> ~/.zshrc
# source ~/.zshrc
```

### 1.3. Your first bug

- **Bug**: Something in the code causes it either not to run or to behave differently than intended.

- **Strategy**: Before hunting through code, **run the code**. The output often shows where the bug is.

- **Example**: Player health is 100, they are hit by a sword for 10 damage, but health becomes 110. The bug is that health **increases** instead of **decreases**.

- **Fix**: Find where health after attack is set. It is set to **player health + sword damage**. Change the **plus** to a **minus** so the math is correct. After the fix, health goes down to 90. Run again before submitting to confirm.

```py
sword_damage = 10
start_health = 100
# end_health = start_health + sword_damage # bug
end_health = start_health - sword_damage # fix

# Don't touch below this line
print(f"Sam's health is: {start_health}")
print(f"Sam takes {sword_damage} damage...")
print(f"Sam's health is: {end_health}")
# Sam's health is: 100
# Sam takes 10 damage...
# Sam's health is: 90
```

### 1.4. The console

- The **console** is where your code's output appears. Only what you tell Python to output (e.g. with **print**) appears there.

> A terminal/console is like a chatbox where you type messages to the computer and it replies by doing the work no buttons, no pictures, just text.

- **Example**: If you set `answer = 2 + 2` and run, nothing shows in the console. Python still computes and stores 4 in `answer`, but you must **print** it to see it.
- print() function will print anything you put inside its parentheses

```python
print(answer)  # Now 4 appears in the console.
```

- final code

```py
answer = 2+2 # no console output
print(answer) # prints output
# 4
```

### 1.5. Why Python

- Python is especially good for beginners: simple to write and read. It is used in **machine learning**, **data science**, **cloud engineering**, **scripting**, **automation**, and **backend web development**.

- **Backend** vs **frontend**:
  - **Backend**: Code that does not produce a visual interface for the user.
  - **Frontend**: Code that produces visual interfaces (websites, desktop apps). Python is not usually used for frontend but can be.

- https://www.python.org/
- https://survey.stackoverflow.co/2025/technology#1-programming-scripting-and-markup-languages

### 1.6. What is code (source code and machine code)

- Code is just a series of instructions for a computer to follow one after another. Programs can have a lot of instructions.

- Multiple Instructions: Code runs in order, starting at the top of the program. 

```py
print("Step 1: open maggie packet")
print("Step 2: put maggie in pot")
print("Step 3: put water in pot")
print("Step 4: turn on the gas and Starts boiling ")
print("Step 5: after 3mins add masala")
print("Step 6: boil till feel it's cooked, max 10mins")
print("Step 7: Turn off the gas")
print("Step 8: serve maggie in bowl and eat")

# Step 1: open maggie packet
# Step 2: put maggie in pot
# Step 3: put water in pot
# Step 4: turn on the gas and Starts boiling 
# Step 5: after 3mins add masala
# Step 6: boil till feel it's cooked, max 10mins
# Step 7: Turn off the gas
# Step 8: serve maggie in bowl and eat
```

- Example: Print Steps to Make a Maggie program, in order
```py
print("Step 1: open maggie packet")
print("Step")
```

- **Source code**: Code humans write and read. It must be converted into **machine code** because computers only understand ones and zeros (binary). We write source code because we cannot work directly in binary; the computer turns our instructions into machine code.

- **Print** can show messages, numbers, or the result of expressions. Example: `print(4 + 5)` prints **9**, not the expression "4 + 5".

```py
print("4 + 6 ")
print(4+6)

# 4 + 6 
# 10
```

### 1.7. Syntax and syntax errors

- **Syntax**: The rules for how expressions and statements are correctly put together in a language. Correct syntax means the structure makes sense (like a proper sentence in English).

- **Syntax error**: The statement is not put together correctly; a rule is broken. Python reports the error and often what to fix.

- **Example**: In a **print** statement, a closing **bracket ]** does not match the opening **(**. Replace the bracket with a closing **)** so the parentheses match. Then the statement is syntactically correct.

```py
# print("Hello world"] # error

# ➜  kintsugi-stack-python git:(main) ✗ python -u "/Users/bali-king/BaliGit/kintsugi-
# stack-python/1_7_.py"
#   File "/Users/bali-king/BaliGit/kintsugi-stack-python/1_7_.py", line 1
#     print("Hello world"]
#                        ^
# SyntaxError: closing parenthesis ']' does not match opening parenthesis '('
# ➜  kintsugi-stack-python git:(main) ✗ 

print("Hello world") # fix
```

- **Syntax differs by language**: Printing "hi" in Python, Go, and Fortran uses different syntax. Using Python syntax in Go would cause a syntax error.
  - Python: `print("hi")`
  - Go: `fmt.Println("hi")`
  - Fortran: `print *, "hi"`
- Syntax errors aren't the only kind of problems you can run into when coding, for example:
  - A bug in your logic: Your code is valid, and will run, but it does something unexpected.
  - It's too slow: Your code is valid and does what's expected, but it does it slowly.

---

## 2. Variables

### 2.1. Variables

- A **variable** stores data so you can use it later, refer to it, change it, or pass it around. Instead of hardcoding values, you give data a name.

- **Example**: `player_health = 1000`. Now you can use **player_health** anywhere, change it, or pass it. Print it to verify.

- **Why "variable"**: The value can change (it varies). Example: Start with `player_health = 1000`, then set `player_health = 1000 - 100` (900), or `player_health = 800`, then 700 in later lines. Each Example updates what the variable holds.

### 2.2. Math with variables

- Use normal math operators: `+`, `-`, `*`, `/`. Example: **armored_health = player_health * armor_multiplier** (e.g. 1000 * 2 = 2000).

- **Negative numbers**: To reduce health (e.g. poison damage), set **poison_damage** to a negative number (e.g. **-10**) so that **player_health + poison_damage** decreases health.

### 2.3. Comments

- A **comment** is ignored by the computer. In Python a comment starts with **#** (pound sign). Use comments to explain code for yourself or others; they do not run.

- **Example**: A line that is not valid code causes a syntax error. Turn it into a comment by adding **#** at the start so the computer skips it.

### 2.4. Naming variables

- **Rules**: You can use letters, numbers, and underscores. A number cannot start the name. No special characters. Python allows this; breaking these rules causes errors.

- **Convention**: Other developers expect readable names. Do not smash words together (e.g. **variablename**). Use **snake_case** in Python (e.g. **variable_name**). **Camel case** (e.g. **variableName**) is used in JavaScript/Go. **Screaming snake case** is often used for constants. Following convention helps others read your code.

### 2.5. Data types

- **String**: Text (a "string" of characters). Use quotes. Example: `"hello"`.

- **Integer**: Whole numbers (positive or negative), e.g. **5**, **-5**.

- **Float**: Numbers with a decimal, e.g. **5.2**, **-5.2**.

- **Boolean**: One of two values — **True** or **False** (like 1 or 0). Example: `player_has_magic = True`.

- **Example**: Set **player_health** to an integer (remove quotes) and **player_has_magic** to a Boolean so types match what the code expects.

### 2.6. F-strings

- **F-string**: A formatted string. Put **f** before the opening quote; inside the string use **squiggly brackets {}** to embed variables. Python replaces them with their values.

- **Without f-string**: You would concatenate with **+**, e.g. `"My name is " + name + " and I am " + str(height) + " feet tall"`. F-strings are simpler: `f"My name is {name} and I am {height} feet tall"`.

- **Example**: Turn the given string into an f-string and put **name**, **race**, and **height** in the correct places using **{name}**, **{race}**, **{height}**.

### 2.7. None type

- **None**: Represents "no value." Useful for variables you set early and may or may not set later; you can check whether they are still **None**.

- **Example**: Declare **enemy = None**. Then **print(enemy is None)** prints **True**. **print(enemy is not None)** prints **False**.

### 2.8. Dynamic vs static typing

- **Python is dynamically typed**: The type of value a variable holds can change. Example: **speed = 5** (integer), then **speed = "five"** (string). In a statically typed language (e.g. Go) you declare the type (e.g. **var speed int**) and cannot assign a string later.

- **Best practice**: Do not change variable types in the middle of code; it causes bugs and confusion. Keep each variable's type consistent.

### 2.9. Math with strings

- **Plus (+)**: Concatenates strings (smooshes them together). Example: **sentence_start + player_one_health** → **"You have 1200"** (add spaces in your strings if you want them).

- **Times (*)**: Repeats the string. Example: **sentence_start * 6** prints **"You have"** six times in a row.

- **Example**: Use **sentence_start**, **player_one_health**, **player_two_health**, and **sentence_end** to print "You have 1200 health" and "You have 1100 health" using concatenation. Watch spaces.

### 2.10. Multivariable declaration

- You can declare multiple variables on one line: list variables on the left of **=**, values separated by commas on the right. Example: **sword_name, sword_damage, sword_length = "Excalibur", 10, 200**. Same as declaring each on its own line.

- **Clean code**: Code that is easy for people to read. Declaring related variables on one line can make code cleaner when it fits.

---

## 3. Functions

### 3.1. What is a function

- A **function** lets you reuse code. Instead of repeating the same operations, you put them in a function and **call** (use) it.

- **Example**: **area_of_circle(radius)** computes the area and **returns** it. You call it with **sword_length** or **spear_length** instead of writing the same formula twice.

- **Declaration**: **def** keyword, function name, **parameters** in parentheses. Example: **def area_of_circle(radius):**. **radius** is a **parameter** — what the function needs to do its job.

- **Return**: The **return** keyword sends a value back to the caller. Example: **sword_area = area_of_circle(sword_length)** — the returned value is stored in **sword_area**. Code after **return** in the function does not run.

- **Example**: Set **spear_area** by calling **area_of_circle(spear_length)** instead of 0 so the spear area is computed correctly.

### 3.2. Multiple parameters

- Functions can take multiple parameters. Order matters: the first argument goes to the first parameter, the second to the second, etc. Example: **result = triple_attack(damage1, damage2, damage3)**; inside the function, **total_damage = slash1 + slash2 + slash3**, then **return total_damage**.

### 3.3. Define before you call

- You must **define** a function before you **call** it. If you call **main()** on line 1 and define **main** on line 4, Python raises **NameError: main is not defined**. Move the function definition above the call.

### 3.4. Entry point (main)

- A common pattern: define all helper functions first, then define **main** (the entry point) that uses them, and at the very end of the file call **main()**. That way everything is defined before any execution starts.

### 3.5. Fahrenheit to Celsius

- Formula: **Celsius = (5/9) * (F - 32)**. Implement the function with parameter **F**, compute **Celsius**, and **return** it. Use ***** for multiplication.

### 3.6. Functions quiz

- **def** is the keyword to create functions. Values passed in are **arguments**; in the definition they are **parameters**. You define a function once and can call it many times with different arguments.

### 3.7. Hours to seconds

- **minutes = hours * 60**, **seconds = minutes * 60**, **return seconds**. Example: 1 hour → 3600 seconds.

### 3.8. Return vs no return

- If a function does not **return** anything (or has no **return** line), it returns **None**. You can **return None** explicitly or just **return** with nothing.

- **Print** shows something in the console; **return** gives a value back to the caller. A function does not both return and print unless you explicitly print the return value.

### 3.9. Returning multiple values

- Return multiple values on one line separated by commas: **return title, new_power**. Catch them with multiple variables: **title, new_power = become_warrior(first_name, last_name, power)**. Do not put two **return** statements (the second would never run).

### 3.10. Parameters vs arguments

- **Parameters**: The names in the function definition (e.g. **a**, **b** in **def add(a, b)**).
- **Arguments**: The actual values passed when you call the function (e.g. **5** and **6** in **add(5, 6)**).

### 3.11. Default parameters

- Give a parameter a default value in the definition: **def get_punched(health, armor=0)**. If the caller does not pass **armor**, it is **0**. Use it to compute new health after damage and return it. Same idea for **get_slashed** with different damage.

### 3.12. Printing vs returning

- **print** sends output to the terminal; it does not return a value to the caller. A function that only **print**s and does not **return** gives **None** to the caller. To both use a value in the rest of the program and show it, **return** the value and let the caller **print** it if needed.

---

## 4. Scope

### 4.1. What is scope

- **Scope** is the context a variable or function belongs to. What you create in one scope may not be visible in another.

- **Parent and child**: The main program (parent) can have variables and functions (children). Functions can see the parent's variables. Variables created inside a function exist only in that function unless you **return** them; then the caller gets a copy in its scope.

- **Example**: **get_actor** cannot use **code_name** if **code_name** is only created inside **get_code_name** and not returned. Fix: **return code_name** from **get_code_name**, store it in a variable (e.g. **cn**) in the parent, and use **cn** where needed (e.g. in **get_actor**).

### 4.2. Python and block scope

- In many languages, **if** blocks have their own scope. In **Python**, variables are scoped to the **function**, not to **if** blocks. So a variable assigned inside an **if** still exists in the rest of the function. In other languages you might declare the variable before the **if** and set it inside.

### 4.3. Example (scope bug)

- **NameError: modifier is not defined** on a line that uses **modifier**. The variable in the parent scope is **my_modifier**. Use **my_modifier** (and **my_level** if applicable) where the parent scope is intended.

### 4.4. Global scope

- **Global scope** is the whole program. Anything you create there is available everywhere. Putting **player_level** in global scope (e.g. at the top) lets all functions that need it see it.

- Functions can access variables declared in global scope. Code outside a function cannot access variables defined inside that function; they exist only in the function's scope.

---

## 5. Testing and Debugging

### 5.1. Unit tests

- **Unit tests** run your code with given inputs and check the outputs. They test behavior, not just console output. You may see a **main_test.py** (or similar) that runs test cases; **Run** uses sample tests, **Submit** runs more (and often harder) tests.

- **Pass**: Use the **pass** keyword as a placeholder so an empty function does not cause an error. Replace **pass** with real logic.

- **Output tests** vs **unit tests**: Output tests check exactly what is printed; extra **print** statements can break them. Unit tests call your functions and check return values; you can leave **print** statements for debugging.

### 5.2. Learning effectively

- Read every lesson and each Example. Use boot.dev and Discord if stuck. Add **print** statements to inspect variables and find bugs. You can look at solutions after you have passed; looking before can reduce XP. When stuck, ask Boot or the community before peeking at the solution.

### 5.3. Debugging

- **Debugging** is finding and fixing bugs. **Run** is like testing before release; **Submit** is like going live. Submit runs more cases and can expose bugs you did not hit with Run. Add **print** statements for key values, fix one piece at a time, then remove or comment out debug prints before submit (for output-based tests).

### 5.4. Practice debugging (unlock_achievement)

- Function returns **(after_xp, alert)**. Compute **after_xp = before_xp + achievement_xp** (use **+**, not **-**). Build **alert** with an f-string: **f"Achievement unlocked: {act_name}"** (spelling and punctuation matter). Return **(after_xp, alert)**. Use **print** to verify each part before returning.

### 5.5. Stack trace (traceback)

- A **stack trace** (Python calls it **traceback**) lists where the error occurred, often through several files. Focus on the **bottom** (last) message — that is usually where the error started.

- **IndentationError**: Python uses indentation (typically 4 spaces) for blocks. Code inside a function must be indented; code inside an **if** must be indented again. Wrong amount of spaces causes this error.

- **SyntaxError**: e.g. **unterminated string literal** — a string is missing its closing quote. Add the closing quote.

- Fix indentation and syntax, then run again; the next error (if any) may appear.

---

## 6. Computing

### 6.1. Numeric types

- **Integers**: Whole numbers. **Floats**: Numbers with a decimal. Division in Python produces a float (e.g. **4 / 2** → **2.0**). Addition, subtraction, multiplication of integers give integers; division gives float.

- **Example**: Sum all weapon damages for **total_damage**, then **average = total_damage / 5**. Return **(total_damage, average)**.

### 6.2. Floor division

- **Floor division** operator: **//**. It gives an integer result by "flooring" (rounding down). **Floor** of a number is the largest integer ≤ that number. **9 // 4** → **2** (since 9/4 = 2.25, floor is 2). For negative numbers: **9 // -4** → **-3** because the largest integer ≤ -2.25 is -3.

### 6.3. Exponents

- Use ******: e.g. **9 ** 2** → **81**. **2 ** 3** → **8**.

### 6.4. Changing in place

- You can use the same variable on both sides of **=**: **current_score = current_score + 300**. This reassigns **current_score** to its old value plus 300. It is Example, not mathematical equality.

### 6.5. In-place operators

- **+=**, **-=**, ***=**, **/=** shorten in-place updates. **current_score -= 1** is the same as **current_score = current_score - 1**. Use **current_health -= damage** and return **current_health** for **get_hurt**.

### 6.6. Bitwise AND

- **&** performs bitwise AND. Used to check if a specific bit is set (e.g. permissions). Compare **user_permissions** with a permission mask; if the result is non-zero, the permission is present. Return the result of **user_permissions & can_create_guild** (and similar for review, delete, edit).

### 6.7. Bitwise OR

- **|** performs bitwise OR. Used to combine permissions: if any role has a permission, the party has it. Start with a default (e.g. 0) and OR with each role's permissions: **party_permissions = glorfindel | galadriel | elrond** (or equivalent parameter names). Return the combined value.

### 6.8. Logical NOT

- **not** inverts a Boolean. **not True** → **False**. The operators **and**, **or**, and **not** are logical (Boolean) operators.

---

## 7. Comparisons

### 7.1. Comparison

- Comparisons produce Booleans. **==** means equal; **!=** means not equal. **>**, **<**, **>=**, **<=** for greater/less than (or equal). Example: login check — compare **login_username == user_username** and **login_password == user_password**; both must match for success.

- **Storing result**: Save comparison results in variables, e.g. **usernames_match = (login_username == user_username)**. Combine with **and**: **both_match = usernames_match and passwords_match**; return **both_match**.

### 7.2. Comparison operators practice

- **can_withstand_blow**: Return **hero_armor >= damage** (True if armor is greater than or equal to damage, False otherwise).

### 7.3. if statements

- **if** runs a block of code when a condition is **truthy**. In Python, indentation (e.g. 4 spaces) defines the block. **Truthy**: values that count as true (e.g. non-zero, non-empty string). **Falsy**: e.g. **0**, **""** (empty string), **None**.

- **Example**: **if player_health == 0:** then **print("dead")**. After the **if** block, **print("status check complete")** runs regardless. So: if health is 0, print "dead" then "status check complete"; otherwise only "status check complete".

### 7.4. if and return (check_swords_for_army)

- If **num_swords == num_soldiers**, **return "correct amount"**. Otherwise **return "incorrect amount"**. You do not need a second **if**; if the first condition is false, the only remaining case is "not equal," so a single **return "incorrect amount"** after the **if** block is enough.

### 7.5. if / elif / else

- For multiple conditions, use **if**, **elif** (else if), **else**. Python evaluates in order; once one condition is true, it runs that block and skips the rest. More efficient and readable than separate **if**s.

- **Example (status by health)**: **if health <= 0: status = "dead"**; **elif health <= 5: status = "injured"**; **else: status = "healthy"**. Then **return status**. Do not write three separate **if**s — if health is 0, the first sets "dead" but a second **if** (e.g. health <= 5) would also be true and could overwrite to "injured".

### 7.6. Boolean logic (does_attack_hit)

- Return **True** if: (attack_roll != 1 and attack_roll >= armor_class) **or** (attack_roll == 20). Break into variables: **condition1 = (attack_roll != 1)**, **condition2 = (attack_roll >= armor_class)**, **condition3 = (attack_roll == 20)**. Result: **(condition1 and condition2) or condition3**.

### 7.7. should_serve_customer

- Return **True** only if all hold: **customer_age >= 21**, bartender is **not on_break**, and **time** is between 5 and 10 inclusive. For time: **5 <= time <= 10**. Combine with **and**: **return (customer_age >= 21) and (not on_break) and (5 <= time <= 10)**.

---

## 8. Loops

### 8.1. for loops and range

- A **for** loop repeats code. **for i in range(0, 10):** — **i** takes values 0, 1, …, 9. **range(start, end)**: **start** is inclusive, **end** is exclusive. So **range(0, 10)** gives 0–9, not 10. **range(0, 100)** for 0–99; **range(0, 200)** for 0–199; **range(5, 16)** for 5–15.

- **Step**: **range(0, 10, 2)** steps by 2 (0, 2, 4, 6, 8). **range(10, 0, -1)** counts down from 10 to 1 (end -1 so 0 is excluded when stepping backward). Indentation is required for the loop body.

### 8.2. Countdown (negative step)

- Use **range(start, end, -1)** to go backward. **start** must be greater than **end** when step is negative; otherwise the loop does not run.

### 8.3. Sum and sum of odds

- **Sum 0..n-1**: Initialize **total = 0**, then **for i in range(end): total += i**. Return **total**.

- **Sum of odd numbers**: Use **range(1, end, 2)** so **i** is always odd, then **total += i**. Alternatively, loop over all **i** and add only when **i % 2 != 0**.

---

## 9. Lists

### 9.1. What is a list

- A **list** is a data structure that holds items in order. Syntax: square brackets **[]**, items separated by commas. Can mix types (strings, numbers, etc.). In other languages similar structure is often called an **array**; Python also has an **array** type (stricter about types).

### 9.2. Adding and indexing

- **Indexing**: **list[0]** is the first item, **list[1]** the second. Indexing starts at **0**. **len(list)** is the number of items. Last index is **len(list) - 1**; **list[len(list)-1]** or **list[-1]** (negative index) for the last item. Accessing **list[len(list)]** causes **IndexError**.

- **Update**: **inventory[0] = "150 gold"** changes the value at that index. **append**: **inventory.append("short sword")** adds one item at the end.

### 9.3. get_inventory

- Add **"short sword"** to the given list (with a comma before it) and return the list.

### 9.4. Length and last index

- **length = len(inventory)**. Last valid index is **length - 1**. **get_last_index**: return **len(inventory) - 1**.

### 9.5. Updating by index (smelt_ore)

- Replace the item at the correct index (e.g. **inventory[1] = "iron bar"**) and return the list.

### 9.6. pop

- **list.pop()** removes and **returns** the last item. Use in a loop to "sell" items: **for _ in range(len(inventory)): item = inventory.pop()** (or similar). The list shrinks each time.

### 9.7. Counting items (get_item_count)

- Loop over **items** with **for i in range(len(items))**, **current_item = items[i]**. Use **if**/ **elif**/ **else** to increment **potion_count**, **bread_count**, **short_sword_count**. Return the counts (or as required).

### 9.8. Iterating without index

- **for item in items:** — **item** is each value. Use when you do not need the index. **for item in items** is cleaner when the index is not needed.

### 9.9. Finding an item (e.g. leather scraps)

- Use a **found** flag (Boolean). **for item in items:** if **item == "leather scraps"**, set **found = True**. Return **found**.

### 9.10. Comparing two lists by index

- When you need the same index in two lists, use **for i in range(len(old_levels))**: **old_level = old_levels[i]**, **new_level = new_levels[i]**. Then **if old_level < new_level:** (e.g. print index or collect indices). Do not use "no index" iteration when you need to pair two lists by position.

### 9.11. Maximum in a list

- Initialize **max_damage_dealt = float("-inf")**. Loop over each value: **if damage > max_damage_dealt: max_damage_dealt = damage**. Return **max_damage_dealt**. Using **float("-inf")** ensures the first comparison always updates (handles all-negative lists).

### 9.12. Modulo

- **%** gives the **remainder** of division. **5 % 2** → **1**. **6 % 2** → **0**. So **num % 2 != 0** means **num** is odd; **num % 2 == 0** means even. Use this to filter odd numbers or to add only odd numbers to a total/list.

### 9.13. Slicing

- **list[start:stop:step]**. **start** inclusive, **stop** exclusive (like **range**). **step** default 1. **champions[0:3]** → first three. **champions[::-1]** reverses. **champions[2:]** from index 2 to end. **champions[:-2]** excludes last two. **champions[::2]** every other (even indices).

### 9.14. Concatenation

- **list1 + list2** creates a new list with all items from both, in order. **megalist = favorite_weapons + favorite_armor + favorite_items**, then return **megalist**.

### 9.15. Deleting from a list

- **del strongholds[0]** removes first element. **del strongholds[-2:]** removes last two. Then return the modified list.

### 9.16. Tuples

- **Tuple**: Like a list but with parentheses **()** and **immutable** — you cannot add, remove, or change items after creation. Use for small, fixed groups of data (e.g. name and age). **Lists** are mutable. Converting a list of hero data into a list of tuples keeps each hero's data grouped and unchanged.

### 9.17. First element / error

- If **len(items) > 0**, **return items[0]**; else **return "error"**. Prevents **IndexError** on empty lists.

### 9.18. Reverse a list

- **Option 1**: **reversed = items[::-1]**. **Option 2**: Build a new list by iterating from **len(items)-1** down to **0** with **range(len(items)-1, -1, -1)** and appending **items[i]**.

### 9.19. Nested loops (filter messages)

- **Outer loop**: **for current_message in messages:**. **Inner loop**: **for word in current_message.split():**. **split()** turns a string into a list of words. If **word == "dang"**, increment a counter and do not add that word to the "clean" message. Build a list of clean messages (join words back with **" ".join(filtered_words)**) and a list of "dang" counts per message. Return both.

---

## 10. Dictionaries

### 10.1. What is a dictionary

- **Dictionary**: Key–value pairs. Syntax: **{}** with **key: value**, comma-separated. **potion["name"]** accesses the value for **"name"**. Use for structured data (e.g. potion name, stat buff, multiplier). Keys should be unique; duplicate keys overwrite (last wins).

### 10.2. Creating and setting

- **record = {"name": name, "server": server, "level": level, "rank": rank, "id": f"{name}#{server}"}**. You can add or update with **dict[key] = value** even if the key is new. **del dict[key]** removes a key. If the key does not exist, **del** raises an error.

### 10.3. Accessing and updating

- **value = dict["key"]**. **dict["key"] = new_value** updates or adds. Duplicate keys: remove the wrong one so the correct value (e.g. from parameters) is kept.

### 10.4. in keyword

- **"key" in dict** returns a Boolean (checks keys only, not values). Use to check before accessing or to count: **if enemy in counts: counts[enemy] += 1** else **counts[enemy] = 1**.

### 10.5. Iterating

- **for key in dict:** gives each key. Use **dict[key]** to get the value. For "most common enemy": iterate, compare **enemies_dict[enemy]** (occurrences), track the key with the highest count. Handle empty dictionary (e.g. **if not enemies_dict: return None**).

### 10.6. Ordered (Python 3.7+)

- As of Python 3.7, dictionaries preserve insertion order. Earlier versions did not guarantee order.

---

## 11. Sets

### 11.1. What is a set

- **Set**: Holds unique items only (no duplicates). Good for "is this value in the collection?" and for removing duplicates. **Unordered** — iteration order is not guaranteed. Fast membership testing.

### 11.2. Creating and using

- **set(list)** or **{item1, item2}**. Empty **{}** is a dict; for empty set use **set()**. **add** adds one item; **remove** removes one. **unique_spells = set(spells_list)** then optionally **list(unique_spells)** if you need to return a list.

### 11.3. Use cases

- Remove duplicates from a list. Store "all possible spells" or "all possible potions" for fast lookup. Type of **my_var = {}** is **dict**; use **set()** for an empty set.

---

## 12. Errors

### 12.1. Syntax errors vs exceptions

- **Syntax error**: Invalid structure; Python refuses to run the file (e.g. wrong bracket, missing quote). **Exception**: Code is syntactically valid but something goes wrong at runtime (e.g. **IndexError**, **TypeError**). Syntax errors stop execution before any code runs; exceptions occur during execution.

### 12.2. try / except

- **try:** block runs code; **except Exception as e:** catches errors so the program does not crash. You can **print(e)** to see the message. If no exception is raised, the **except** block does not run. If an exception is raised outside a **try**, the program crashes unless caught elsewhere.

### 12.3. Raising exceptions

- **raise Exception("message")** triggers an error with a custom message. Use for invalid cases (e.g. **player_id not found**, **negative ID not allowed**). Good for expected error conditions (e.g. no arrows left) vs **bugs** (unexpected logic errors found later).

### 12.4. Catching specific exceptions

- **except TypeError as e:** catches only **TypeError**. **except Exception as e:** catches all. Put the more specific **except** before the general one; otherwise the general one catches everything and the specific block never runs. Example: **except IndexError:** return **"index is too high"**; **except Exception as e:** return **e** (or handle otherwise).

### 12.5. Review

- The custom string in **raise Exception("message")** is the message, not the exception type. **raise Exception("zero division")** is still an **Exception**, not a **ZeroDivisionError**. So **except ZeroDivisionError** would not catch it; **except Exception** would. When you **except Exception**, you catch **ZeroDivisionError** and all other subtypes too.

---
End-of-File

The [KintsugiStack](https://github.com/kintsugi-programmer/KintsugiStack) repository, authored by Kintsugi-Programmer, is less a comprehensive resource and more an Artifact of Continuous Research and Deep Inquiry into Computer Science and Software Engineering. It serves as a transparent ledger of the author's relentless pursuit of mastery, from the foundational algorithms to modern full-stack implementation.

> Made with 💚 [Kintsugi-Programmer](https://github.com/kintsugi-programmer)