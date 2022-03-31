#!/usr/bin/env python
# coding: utf-8

# # Start your first project with Jupyter Lab
# 
# Best practices for starting a data science project with Jupyter Lab

# ![](../img/get_started/jlab_interface_1.png)

# ## What is Jupyter Lab?

# Jupyter Lab is an integrated development environment (IDE) commonly used for interactive coding with languages such as Python, R, and Julia. In fact, **Jupyter** is an acronym for **Ju**lia-**Py**thon-**R**. You can also you Jupyter Lab with other scripting languages such as Matlab or Octave.
# 
# **What is an IDE?** An IDE is simply a text editor with some features that make coding easier and more efficient such as
# 
# - Syntax highlighting
# - File organization/navigation
# - Code execution
# - Integrated terminal
# - Debugger
# 
# Jupyter Lab is the next generation of **Jupyter Notebook** (the older version). Besides full support for Jupyter Notebook, JLab provides much more features and enhancements that boost your **productivity** and **enjoyment** while coding.
# 
# You don't need to install Jupyter Lab because it comes with Anaconda's standard installation, which you already installed in the previous tutorial.
# 
# Jupyter Lab is not the only IDE for Python, but in my opinion, it is the best for data-related tasks. Other common IDEs include
# 
# - Pycharm
# - Spyder
# - Visual Studio Code
# - Zeppelin

# ## Create a workspace
# 
# The first thing to do when starting a Python project is to set up a **workspace** for that project. A workspace is just a **folder** (or directory) on your computer where you host the code files, data, and related stuff. It is sometimes called the **root directory**.
# 
# You might be working on multiple projects, so it's best to have a parent folder for them. For example, in my laptop, the super-folder for data science projects is located at `D:/ds_projects`.
# 
# Inside `D:/ds_projects`, create a folder for your first project and name it `example`. For your future projects, you should use meaningful names. Then go into `example` and create sub-folders following the structure below
# 
# ```
# example/
#     |____ data/
#     |____ nb/
#     |____ lib/
#     |____ out/
#     |____ docs/
# ```
# 
# `data/` is for your data files. `nb/` is for your analytics notebooks. `lib/` is for your custom modules. `out/` is for output such as exported Excel files or graphs. `docs/` is for related documents.
# 
# To keep things simple, for this tutorial, you only need `nb/` folder. The structure suggested above is a **guideline** for you when working on more complex projects in the future.
# 
# Inside `example`, right-click and choose `Git Bash Here` (now you know why we installed `Git`). For macOS users, when right-clicking, you will see an option `Terminal at folder` under `Services` menu, which serves the same purpose - to launch a terminal at the current folder.

# ![](../img/get_started/git_bash_here.png)

# Type in the terminal `jupyter lab` and hit `Enter`. Jupyter Lab will be launched via a new tab of your default browser. For a better experience, I recommend you use a modern browser such as Chrome or Microsoft Edge as your default browser.

# ## Jupyter Lab's interface
# 
# You can find very detailed and up-to-date tutorials on how to use Jupyter Lab [here](https://jupyterlab.readthedocs.io/en/stable/user/interface.html).

# ![Jupyter Lab interface](../img/get_started/jlab_interface.png)

# ## Create your first notebook

# Your project can contain only a single **notebook** or a collection of notebooks, depending on the complexity of your analysis. Each notebook is a piece of analysis that contains code and explanatory text.
# 
# Now use the navigation panel on the left to go inside `nb/` subfolder. When inside `nb/`, click the big blue button with a plus sign, and on the **launcher panel** on the right, choose `Python 3 (ipykernel)` (see below picture)

# ![](../img/get_started/new_notebook.png)

# Right-click on the file name in the left panel and rename it to `first_analysis` (see below picture)

# ![](../img/get_started/first_analysis.png)

# ## Components of a notebook
# 
# A **notebook** consists of editable **cells** (meaning you can write into those cells). The main reason for breaking our code into multiple cells is better management - easier to maintain and debug.
# 
# 
# There are two types of cells **Code** cells and **Markdown** cells
# 
# - Code cells: used for writing Python code, thus what you write must conform to Python syntax. If not, you will get an error when the cell is executed.
# 
# - Markdown cells: used for writing explanatory text (like what you are reading now). You can write whatever you want, there will be no error.
# 
# **Markdown** specifies a simple set of rules that allow you to format your text similar to what you do with Microsoft Word (but much more limited)
# 
# - Headings (h1, h2, ..., h6)
# - Bullet points
# - **Bold text**
# - *Italic text*
# - `code fences`
# - Math formula $E = mc^2$
# - And many more
# 
# By default, a new cell will be a Code cell. To convert a cell to a Markdown cell, use `Esc + M`. To convert it back to a Code cell, use `Esc + Y`. You will learn more about Markdown in the next tutorial.

# ## Run a cell
# 
# When you finish writing, you need to **run** or **execute** it to tell Jupyter Lab to process and render what you write
# 
# - The processing of a **Code** cell will call Python to evaluate the code you wrote and display the output (if any) or errors (if you did something wrong).
# 
# - The processing of a **Markdown** cell just renders the text according to Markdown's rules. There will be no error.
# 
# 
# There are three ways to run a cell, and they are the same for both Code cells and Markdown cells
# 
# 1. `Ctrl + Enter`: run the current cell and stay at that cell
# 1. `Shift + Enter`: run the current cell and move to the next cell
# 1. `Alt + Enter`: run the current cell, then insert a new cell below and move to that cell

# **Example 1**: run a code cell

# In[1]:


print("Hello. How are you?")
print(2 + 3)


# **Example 2**: run a Markdown cell with the following content
# 
# ```
# - item 1
# - **item 3**
# - *item 4*
# - $y = \frac{1}{2}\int e^{2x}dx$
# ```

# Here is what you will see
# 
# - item 1
# - **item 3**
# - *item 4*
# - $y = \frac{1}{2}\int e^{2x}dx$

# ## Command vs. editing mode
# 
# There are two working modes in a notebook - **command** mode and **editing** mode. You are in the **editing** mode when you are typing something inside a cell, and what you do is mostly just **writing**. In contrast, when in **command mode** you perform actions on the whole cell (and potentially on multiple cells) such as
# 
# - Delete, copy, cut a cell
# - Paste a cell below another cell
# - Add a cell above or below another cell
# 
# To activate the command mode, you hit `Esc` and then press another key to perform an action you wish. For example, `Esc + A` will add a new cell above the current cell (see the next section for a complete list of actions)
# 
# To activate the editing mode on a cell, you simple double-click on that cell and start typing.

# ## Useful shortcuts in command mode
# 
# The following are common keyboard shortcuts to work on a notebook in the command mode. Of course, there are equivalent GUI options that allow you to accomplish them with your mouse, but I highly recommend using shortcuts because they will allow you to code **a lot faster**.
# 
# - Add a cell **Above** the current cell: `Esc + A`
# - Add a cell **Below** the current cell: `Esc + B`
# - **Delete** the current cell: `Esc + DD`
# - **Copy** the current cell: `Esc + C`
# - **Cut** the current cell: `Esc + X`
# - **Paste** a cell in the clipboard *below* the current cell: `Esc + V`
# - **Undo** last action: `Esc + Z`
# - Convert a cell to a **Markdown** cell: `Esc + M`
# - Convert a cell to a **Code** cell: `Esc + Y`

# ## Practice
# 
# As I mentioned in the first tutorial when introducing this series, the only way to master any skill is through practice. Thus, here are some exercises to help you internalize what you have learned. They are very simple and won't take much time. There might be some activities that I did not cover in the main text, but you can figure out how to accomplish them easily.

# ### Ex 1
# 
# 1. Create a folder named `test/` on your computer
# 1. Launch Jupyter Lab inside `test/`
# 1. Create three sub-folders and rename them `data/`, `nb/`, and `/docs` (Hint: using the left panel)
# 1. Go inside `data/` and upload a random file (Hint: using the left panel)
# 1. Go inside `nb/`, create a new notebook and rename it to `analysis.ipynb`
# 1. Go inside `docs/`, create a new text file and rename it to `manual.txt`

# ### Ex 2
# 
# Open `analysis.ipynb` in Ex 1 and do the following
# 
# 1. Add a Markdown cell with the content `Monthly analysis`
#     
# 1. Add a Code cell with the following content and run it. What output do you see?
# 
# ```python
# store_1_sales = 5000
# store_2_sales = 7000
# total_sales = store_1_sales + store_2_sales
# print(f"Total sales:  {total_sales}")
# ```
# 
# 1. Add a Markdown cell and write some random text
# 
# 1. Copy the above Markdown cell and paste it right below the first cell
# 
# 1. Delete the cell you have just pasted
# 
# 1. Undo the deletion
# 
# 1. Convert the code cell in step 2 into a Markdown cell and execute it. What do you see?
# 
# 1. Convert it back to a code cell and execute it. What do you see?
# 
# 1. Notice on the top-right corner, do you see something like `Python 3 (ipykernel)`. If yes, it means you are in an active session and Python is still running under the hood. No more action is needed for this task.
# 
# 1. Now shut down the kernel for this notebook (but do not close it). Do you see something like `No Kernel`?  If yes, it means the kernel is dead and Python is not running. (Hint: do you see a button with a square inside a circle on the left side of Jupyter Lab?)
# 
# 1. Add a code cell at the end of the notebook and run the following statement `print("Kernel is dead")`. What do you see?
# 
# 1. Now reactivate the kernel. Do you see a green dot on the left of the file name and the top-right corner is back to `Python 3 (ipykernel)`? If yes, it means the kernel is up and running. (Hint: `Menu > Kernel > Restart Kernel)`
# 
# 1. Now re-run the code cell in step 9. Does it work now?
# 
# 1. Scroll to the end of the notebook, add 10 blank code cells. How to make it fast? (Hint: `Esc` then hit (fast) `B` ten times)
# 
# 1. Now delete all the blank cells you have just added. How to make this fast? (Hint: click on the first cell, hold the `Shift` key, then click the last blank cell while still holding `Shift`. You will see all the cells are highlighted. Now hit `Esc + DD`)
# 
# 1. Undo the deletion
