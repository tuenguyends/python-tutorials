#!/usr/bin/env python
# coding: utf-8

# # Definitive guide to Markdown

# ![](../img/get_started/markdown_ex.png)

# ## What is Markdown?
# 
# Markdown is a lightweight **markup language** that allows you to add **formatting elements** to plaintext text documents such as
# 
# - Headings
# - Bold, italic
# - Ordered/unordered lists
# - Links
# - Images
#     
# Markdown is extremely useful not only for **technical writing** but for any kind of writing in general.
# 
# ## Why use Markdown?
# 
# **Versatility**. Markdown can be used for many purposes such as
# 
# - Technical documentation (as this tutorial)
# - Notes and books
# - Static web pages
# 
# **Minimal distraction**. Compared to rich-text text processors such as Microsoft Word or Libre Writer, Markdown offers much fewer features. However, this turns out to be its main advantage. By restricting you to a small set of formatting options, Markdown forces you to focus on writing **good content** rather than spending time tweaking the appearances such as themes, fonts, colors, and other kinds of formatting.
# 
# **Portability**. Unlike a Word file (`.docx`), a Markdown file is just a simple plain text file and thus can be opened by any text editors such as Notepad++, Sublime Text, Atom, or Visual Studio Code. You won't have to worry when migrating your files to different operating systems or cloud services because you can always access their contents.
# 
# **Easy integration**. If you plan to be a data analyst/scientist/researcher, technical documentation is part of your daily work. Markdown makes your life much easier by allowing you to mix your technical notes and executable code in **the same place**. 
# 
# In the traditional workflow, you write code to perform some analysis then copy the results (statistics, figures, etc.) into a separate file (normally Word) for reporting purposes. What if the data or some of the requirements change? You have to **re-run your analysis and copy your results again**. This is painful! 
# 
# But by mixing your notes using Markdown with your Python analytics code in a single Jupyter Notebook, all you need to do is to modify the requirements and re-run your notebook. All the results will be automatically updated accordingly. No painful **copy-and-paste** stuff is needed.
# 
# **Easy conversion**. You can easily convert a Markdown file to different formats such as PDF and HTML as you can see in the picture below.

# ![](../img/get_started/markdown_ex_2.png)

# ## Basic Markdown syntax
# 
# This section introduces the basic Markdown syntax that is most commonly used in technical documentation. For more advanced syntax, see the next section.

# ### Headings
# 
# Headings are used to organize contents into **sections**. There are 6 levels from `h1` to `h6` with `h1` being the biggest and `h6` being the smallest. Normally, there should be only one `h1` heading in your whole file, which is the title of the document. Other sections will begin with `h2` headings.
# 
# Although Markdown allows up to 6 levels, you should never use beyond `h3`. Nesting your contents too deep make it hard to follow, thus keep your contents as flat as possible. This is also one of the guiding principles of **Zen of Python** - `Flat is better than nested`. I personally usually use `h1` and `h2` only.
# 
# A heading starts with `#`. The number of `#` indicates the heading level, for example
# 
# ```
# # Level 1
# ## Level 2
# ### Level 3
# #### Level 4
# ##### Level 5
# ###### Level 6
# ```
# 
# Open a notebook and try it yourself on a Markdown cell (see the previous tutorial for how to work with Markdown cells)

# ### Paragraphs
# 
# Two paragraphs are separated by a **blank line**. One common mistake is just using `Enter` and start writing the new paragraph. It will not work, you must add a blank line between graphs.
# 
# Here is the wrong way
# 
# ```
# Paragraph 1
# Paragraph 2
# ```
#   
# The correct way should be
# 
# ```
# Paragraph 1
# 
# Paragraph 2
# ```
# 
# Try it yourself in a notebook to see the difference.

# ### Lists
# 
# There are two types of lists - unordered and ordered. Remember to add a blank line before starting a list.
# 
# To make an **unordered lists**, place `-` followed by a space before each item of the list, for example
# 
# Example 
# 
# ```
# - item 1
# - item 2
# - item 3
# ```
# 
# You will see something like this
# 
# - item 1
# - item 2
# - item 3
# 
# To make an **ordered** list, place `1.` followed by a space before each item of the list. You don't need to manually increase the number, it will be done automatically. This is very convenient because if you want to insert a new item into the list, you won't have to update the numbers for the items that follow it.
# 
# Example
# 
# ```
# 1. item 1
# 1. item 2
# 1. item 3
# ```
# 
# You will see something like this
# 
# 1. item 1
# 1. item 2
# 1. item 3
# 
# Lists can also be **nested** on multiple levels. However, try to keep it shallow (two levels at most)
# 
# Example of a two-level unordered list
# 
# ```
# - item 1
#     - sub-item 1.1
#     - sub-item 1.2
# - item 2
#     - sub-item 2.1
#     - sub-item 2.2
# ```
#     
#     
# Example of a two-level ordered list
# 
# ```
# 1. item 1
#     1. sub-item 1.1
#     1. sub-item 1.2
# 1. item 2
#     1. sub-item 2.1
#     1. sub-item 2.2
# ```
#     
# For nested lists, you can **mix ordered and unordered styles** together as long as the items of the same level have the same type
# 
# Example of a two-level mixed list
# 
# ```
# 1. item 1
#     - sub-item 1.1
#     - sub-item 1.2
# 1. item 2
#     - sub-item 2.1
#     - sub-item 2.2
# ```
#     
# Try all of these examples in your notebook.

# ### Emphasis
# 
# This one is simple
# 
# - `**Make bold**` will **Make bold**
# - `*Make italic*` will *Make italic*
# - `***Make bold and italic***` will ***Make bold and italic***

# ### Code fences
# 
# Code fences are used to emphasize texts that should be understood as a coding element such as a variable name, an expression, or a whole code block.
# 
# The **inline** code format is used for short elements such as a number, a variable name, or an expression. These elements stay in the line with normal texts (thus the name *inline*). To use the inline code format, wrap your code in a pair of **single backticks** `` ` ``
# 
# Example of inline code
# 
# - Numbers: `` `42` `` -> `42`
# - Variable names: `` `profit` `` -> `profit`
# - Expressions: `` `y = 3*x + 1` `` -> `y = 3*x + 1`
# 
# In contrast, the **code-block** style is for a block of code, which normally spans more than one line. To use code-block style, wrap your code in a pair of **triple backticks** `` ``` ``. You can specify the **language** to take advantage of syntax highlighting
# 
# Example of a Python code block
# 
# ````
# ```python
# def say_hi(name):
#     print(f"Hello {name}")
#     print("Have a good day")
# ```
# ````
# 
# will look like this
# 
# ```python
# def say_hi(name):
#     print(f"Hello {name}")
#     print("Have a good day")
# ```

# ### Latex
# 
# Markdown supports Latex syntax so you can type math formulas easily. Similar to code fences, there are inline (use `$`) and block (`$$`) math formulas. Copy and try the following examples in your notebook.
# 
# Inline latex
# 
# ```
# The probability mass function for a binomial distribution is given by $f(x) = {n \choose x} p^{x} (1-p)^{n-x}$ 
# ```
# 
# Block latex
# 
# ```
# $$
# M = \begin{bmatrix}a_1 & b_1\\
# a_2 & b_2 \\
# a_3 & b_3
# \end{bmatrix}
# $$
# ```

# ### Links
# 
# Here is how to embed a link
# 
# ```
# If some think you don't know, use [Google](https://www.google.com)
# ```
# 
# will appears like this
# 
# If some think you don't know, use [Google](https://www.google.com)

# ### Remark 1
# 
# The syntax introduced so far is enough for you to have a nice-looking notebook. I rarely use any Markdown features beyond this level. Remember, the most important thing is the **quality of your analysis**. Don't bother too much with fancy formatting. However, on some occasions, you might need a bit of fanciness. If so, then read the next section.

# ## Advanced Markdown syntax

# ### Blockquotes
# 
# As the name suggests, block quotes are used for quotes or excerpts. You start a blockquote with `>`, for example
# 
# ```
# > My advice to you is to get married: if you find a good wife you’ll be happy; if not, you’ll become a philosopher (Socrates)
# ```
# 
# will look like this
# 
# > My advice to you is to get married: if you find a good wife you’ll be happy; if not, you’ll become a philosopher (Socrates)
#     
#     
# For multi-paragraph block quotes, add a blank line between paragraphs and remember to start every line with `>` as in the following example
# 
# ```
# > My advice to you is to get married: if you find a good wife you’ll be happy; if not, you’ll become a philosopher (Socrates)
# >
# > Behind every great man is a woman rolling her eyes (Jim Carrey)
# ```
# 
# will look like this
# 
# > My advice to you is to get married: if you find a good wife you’ll be happy; if not, you’ll become a philosopher (Socrates)
# >
# > Behind every great man is a woman rolling her eyes (Jim Carrey)

# ### Images
# 
# To insert an image, use the following syntax `![Caption](path_to_the_image)`. You can use an **absolute** or a **relative** path. 
# 
# Example
# 
# ```
# ![Python logo](https://upload.wikimedia.org/wikipedia/commons/thumb/c/c3/Python-logo-notext.svg/242px-Python-logo-notext.svg.png)
# ```
# will insert and display the following photo
# 
# ![Python logo](https://upload.wikimedia.org/wikipedia/commons/thumb/c/c3/Python-logo-notext.svg/242px-Python-logo-notext.svg.png)
# 

# ### Tables
# 
# Here is an example of a table
# 
# 
# ```
# | id | name       | email            |
# |----|------------|------------------|
# | 1  | John Doe   | john@gmail.com   |
# | 2  | Jane Smith | jane@hotmail.com |
# | 3  | Nam Tran   | nam@yahoo.com    |
# ```
# 
# 
# | id | name       | email            |
# |----|------------|------------------|
# | 1  | John Doe   | john@gmail.com   |
# | 2  | Jane Smith | jane@hotmail.com |
# | 3  | Nam Nguyen | nam@yahoo.com    |
# 
# However, my advice is not to type tables by yourself. Go to some (free) website that offers **Markdown table generator** such as this one https://www.tablesgenerator.com/markdown_tables

# ### Emails
# 
# Put your email inside `<>` and when someone clicks on the link, the default email app will be launched. 
# 
# Example
# 
# ```
# <pythonisfun@example.com>
# 
# ```
# 
# will become this
# 
# <pythonisfun@example.com>

# ### HTML
# 
# You can also use HTML tags inside a Markdown file, and they will be parsed according to HTML rules
# 
# Try the following example in your notebook
# 
# ```html
# <div>
#     <p>This is a paragraph</p>
#     <p>Next one will be an unordered list</p>
#     <ul>
#         <li>item 1</li>
#         <li><b>item 1 in bold</b></li>
#         <li><span style="color: red;">item 3 in red</span></li>
#     </ul>
# </div>
# ```

# ## Summary 2
# 
# The following summarizes all the Markdown syntax you need to know.

# ````
# HEADINGS
# # Level 1
# ## Level 2
# ### Level 3
# #### Level 4
# ##### Level 5
# ###### Level 6
# 
# EMPHASIS
# Bold: **bold**
# Italic: *italic*
# Bold and italic: ***Bold and italic***
# Strike through: ~~Strike through~~
# 
# ORDERED LISTS
# - item 1
# - item 2
# - item 3
# 
# UNORDERED LISTS
# 1. item 1
# 1. item 2
# 1. item 3
# 
# NESTED LISTS
# - item 1
#     - sub-item 1.1
#     - sub-item 1.2
# - item 2
#     - sub-item 2.1
#     - sub-item 2.2
# 
# MIXED NESTED LISTS
# 1. item 1
#     - sub-item 1.1
#     - sub-item 1.2
# 1. item 2
#     - sub-item 2.1
#     - sub-item 2.2
# 
# INLINE CODE
# Numbers: `42`
# Variable names: `profit`
# Expressions: `y = 3*x + 1`
# 
# BLOCK CODE
# ```python
# def say_hi(name):
#     print(f"Hello {name}")
#     print("Have a good day")
# ```
# 
# INLINE LATEX
# $E = mc^2$
# 
# BLOCK LATEX
# $$
# M = \begin{bmatrix}a_1 & b_1\\
# a_2 & b_2 \\
# a_3 & b_3
# \end{bmatrix}
# $$
# 
# LINKS
# [Google](https://www.google.com)
# 
# SINGLE-PARAGRAPH QUOTES
# > This is a quote
# 
# MULTI-PARAGRAPH QUOTES
# > This is the first paragraph
# >
# > This is the second paragraph
# 
# IMAGES
# ![Caption](path_to_the_image)
# 
# TABLES
# | id | name       | email            |
# |----|------------|------------------|
# | 1  | John Doe   | john@gmail.com   |
# | 2  | Jane Smith | jane@hotmail.com |
# | 3  | Nam Tran   | nam@yahoo.com    |
# 
# EMAILS
# <pythonisfun@example.com>
# 
# HTML
# <div>
#     <p>This is a paragraph</p>
#     <p>Next one will be an unordered list</p>
#     <ul>
#         <li>item 1</li>
#         <li><b>item 1 in bold</b></li>
#         <li><span style="color: red;">item 3 in red</span></li>
#     </ul>
# </div>
# 
# HORIZONTAL LINES
# ---
# 
# FOOT NOTES
# This line will have a foot note [^1]
# [^1]: here is the foot note
# ````
