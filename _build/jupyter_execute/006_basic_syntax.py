#!/usr/bin/env python
# coding: utf-8

# # Python's basic syntax

# ![](../img/get_started/python_code_2.png)

# This tutorial aims to provide just some very basic syntax so that you can **get started immediately**. It's like when you first learn a new language (says Spanish), you don't dive into learning grammar right away. Instead, you learn some basic **vocabulary** and **simple sentences**. This lesson serves such a purpose. In the next lessons, you will learn Python in a **more systematic way**.

# ## Python as a calculator
# 
# You can use Python as a calculator to compute math expressions, for example

# Addition

# In[1]:


2 + 3


# Subtraction

# In[2]:


2 - 3


# Multiplication

# In[3]:


2 * 3


# Division

# In[4]:


2 / 3


# Integer division

# In[5]:


2 // 3


# Modulus (get the remainder)

# In[6]:


2 % 3


# Exponential (use `**` not `^`)

# In[7]:


2**3


# More complicated expressions

# In[8]:


1000 * (1 + 0.05)**20


# ## Printing

# You can use `print()` **function** to print out values associated with a **literal**, a **variable**, or an **expression**.
# 
# - **Functions**: roughly speaking, a function takes some input (inside the parentheses), does something with the input, and spits out some output. Here, print takes in a string or an expression, evaluates it, and prints the evaluated value
# 
# - **Literals**: A literal is a fixed/constant value. When you see it, it is *literally* the value it represents. No additional conversion is needed, for example, `2`, `"Hello"`, `True`, etc.
# 
# - **Variables**: you will learn variables in greater depth in the next tutorial. For now, just accept that a variable is a *nickname* associated with some value.
# 
# - **Expressions**: an expression is anything that can be evaluated as a value, for example `2 + 5`, `(15 + 7) / 2`

# Print string literals (note, you need to wrap strings in quotes, either single or double quotes)

# In[9]:


print("Hello")
print('Nice to meet you')


# Print variables

# In[10]:


x = 2 + 3
print(x)


# Print expressions

# In[11]:


print(2**3 + 4)


# ## Comments
# 
# Comments are used to document your code so that other people can understand what you are doing (if your code is not so obvious). "Other people" also include "future you" because it is not common that you will forget what you have done after a few weeks (even days). 
# 
# Comments are for *human-only* and are ignored by the interpreter. In Python, a comment starts with `#`

# In[12]:


# This is a single-line comment


# In[13]:


# This is also a comments
# but it spans
# on multiple lines


# ## Statements
# A statement is a **complete instruction** that Python can execute. It is like a **full-sentence** in English. Each statement *normally* sits on one line, and you don't need to end a statement with a semi-colon `;` as in some other language such as `C/C++`.
# 
# The code block below has three statements. The first and second are two **assignments**, and the third is a print statement.

# In[14]:


x = 2 + 3
y = x**2
print(y)


# We can also use `;` to write multiple statements on one line as in the example below

# In[15]:


x = 5; y = 6; z = 7
print(x + y + z)


# However, this practice is **discouraged** because it reduces **readability**. It's best to keep each statement on its own line as shown below (we don't have to pay for the space anyway)

# In[16]:


x = 5
y = 6
z = 7

print(x + y + z)


# ## Line continuation
# 
# On some occasions, you might have to write a complex statement, and keeping everything in one line make it very ugly and hard to read. If so, you can break it into multiple (shorter) lines by putting a backslash `\` at the end of each line. This backslash indicates that the statement will continue to the next line. For example

# In[17]:


x = 1 + 2 + 3 +    4 + 5 + 6 +    7 + 8 + 9

print(x)


# Another approach is to wrap it multi-line statement inside parentheses

# In[18]:


x = (1 + 2 + 3 +
    4 + 5 + 6 +
    7 + 8 + 9)

print(x)


# ## White spaces
# 
# White spaces include spaces, tabs, newlines, and blank lines. Often, whitespaces are ignored by the interpreter.

# Example 1: extra spaces don't count

# In[19]:


print(2+3)
print(2 + 3)
print(    2 +     3)


# As you can see, all three statements print out the same result. However, among them, the second line is considered to follow **best practices** (more on **coding style guide** in future lessons)

# Example 2: new lines and blank lines don't count either

# In[20]:


# Snippet 1
x = 2 + 3


y = 4 + 5

print(x + y)


# In[21]:


# Snippet 2
x = 2 + 3
y = 4 + 5
print(x + y)


# Again, snippet 2 is better than snippet 1 in terms of coding style.

# ## Indentation
# 
# Indentation means the spaces at the beginning of each line. Unlike other languages, **indentation does matter** in Python. Python uses indentation to indicate a code block (similar to the use of curly brackets `{}` in other languages), and thus need to use properly.
# 
# You can try to run two following snippets in your notebook and observe what happens.
# 
# Snippet 1
# 
# ```python
# age = 30
# 
# if age >= 21:
#     print("Congrats! You can buy vodka")
# ```
# 
# And snippet 2
# ```python
# age = 30
# 
# if age >= 21:
# print("Congrats! You can buy vodka")
# ```
# 
# You will learn about indentation later. For now, if there is no reason, never indent your code.
