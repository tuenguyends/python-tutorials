#!/usr/bin/env python
# coding: utf-8

# # Environment setup

# There are several ways to start working on a Python project. You can choose to install pure Python and use its IDLE interface to write and run your code. However, a better alternative is to use Anaconda and Git Bash.

# ## Anaconda
# 
# **What is Anaconda?** Anaconda is a distribution of Python and R for  data science and scientific computing. The standard installation of Anaconda consists of
# 
# - 250+ popular packages
# - A package manager
# - An environment manager
# - Jupyter Lab - a powerful IDE for coding
# 
# 
# **Why Anaconda?** Anaconda makes it much easier for you to work on your data science project. 
# 
# - Often, your project will use different packages, many of which already come with Anaconda's standard installation
# 
# - You can also use Anaconda to install additional packages from a repository of 7,500+ open source packages
# 
# - Anaconda's package manager will take care of all the dependencies to make sure everything is compatible with each other
# 
# - You can also create multiple environments with different configurations for different projects you want.

# ## Git
# **What is Git?** Git is a version control system used to track modifications to a source code repository. However, it's not the reason we install it here. We install Git to get Git Bash, a great command-line app that makes launching Jupyter Lab much easier.
# 
# **Note** that only Windows users need to download and install Git. macOS and Linux have great native command-line apps already.

# ## Download Anaconda
# 
# You can download Anaconda at https://www.anaconda.com/products/distribution. If the link has changed you can use Google. 
# 
# Remember to choose the appropriate installer for your operating system.
# 

# ## Install Anaconda
# When installing Anaconda, just follow the instructions but pay attention to the `Advanced installation options` stage. You should select **both checkboxes** although the first one says *not recommended* (see picture below).

# <img src="img/anaconda_install.png" style="width:450px;"/>

# ## Download Git
# 
# You can download Git at: https://git-scm.com, and of course, use Google if the link has changed.

# ## Install Git
# 
# Just follow the instructions and accept all default options. No special modification is needed.

# ## Double-check
# 
# Type `Git Bash` into the search window, and if Git Bash is available then it was installed correctly.
# 
# Hit `Enter` to open Git Bash. You will see a black window with a blinking cursor. This window is the Git Bash **terminal**.
# 
# Now type `conda --version` into the terminal, and hit `Enter`. If you see something like `conda 4.12.0` printed out, then Anaconda was installed correctly.

# ## Create a workspace
# 
# A **workspace** is just a folder/directory on your computer where you host stuff for a given project such as code files, data, output, documentation, etc. The workspace is sometimes called the **root** directory.
#  
# Often, you will work on multiple projects, so it's best to have a parent folder for them, for example, `D:/ds_projects/`.
# 
# 
# Now go inside `D:/ds_projects/` and create a folder named `example/`, then go inside `example/` and create several sub-folders following the structure below.
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
# Here, `data/` is for your data files. `nb/` is for your analytics notebooks. `lib/` is for your custom modules. `out/` is for output such as exported Excel files or graphs. `docs/` is for related documents.
# 
# For simplicity, you only need the `nb/` folder in this tutorial. However, the structure suggested above is a good guideline for you when working on more complex projects in the future.
