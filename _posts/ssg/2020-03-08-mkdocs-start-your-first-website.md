---
layout: post
author: "Vijay Kumar Polimeru"
title: "Start your first website using MkDocs"
permalink: /start-your-first-website/
tags:
  - Static Site Generators
  - MkDocs
comments: true
more_updates_card: true
---

No matter what profession you are in, having a website helps you in multiple ways. With the inception of [***static site generators (SSG)***](https://wiki.tcl-lang.org/page/Static+site+generator),
the process of building a website became very easy and free. 

In this post, I have provided step-by-step information to create your first website using
a python based *SSG* called [MkDocs](https://www.mkdocs.org/). 
Using MkDocs you can build awesome websites (or project documentations) in a matter of seconds and can host it on [gh-pages](https://pages.github.com/) for free. 
Along with MkDocs, there exists 460 other SSGs availble at your disposal. You can find a
defnitive list of all available SSGs [here](https://staticsitegenerators.net/). I the upcoming posts, I will try to cover as many as I can.

With that said, Lets start installing prerequisites and build our first website using MkDocs.

MkDocs installation involves three stpes 

1. Installing `Python`
2. Installing `pip` and
3. Installing `mkdocs` and associated themes via `pip`

Once you finished these three steps, you are ready to go launch your first website.

## Installing `Python`

To install `Python` download [Anaconda Python](https://www.anaconda.com/distribution/#download-section) or simply download [Python](https://www.python.org/downloads/). 

## Installing `pip`

To install `pip` on Linux or MacOS machines, please type `pip install -U pip` on Windows Machines please type `python -m pip install -U pip` in the command prompt. 
For more information, please refer to `pip` documentaion [here](https://pip.readthedocs.io/en/stable/installing/)

Once you are done with steps 1 and 2, please check the version numbers of `Python` and `pip` to confirm that installation is succefull.

On Linux/MacOS Machines
```
$ python --version
Python 3.7.2
$ pip --version
pip 19.3.1
```

On Windows Machines
```
>python --version
Python 3.7.2
>python -m pip --version
pip 19.3.1
```

## Installing `mkdocs` and associated themes via `pip` 

To install `mkdocs` please enter the commands `pip install mkdocs` on Linux/MacOS Machines or `python -m pip install mkdocs` on Windows Machines. To confirm that installation is successfull, please type 

On Linux/MacOS Machines
```
$ mkdocs --version
mkdocs, version 1.0.4
```

On Windows Machines
```
>python -m mkdocs --version
__main__.py, version 1.0.4 from C:Users\blah\blah\Python\Python37\site-packages\mkdocs (Python 3.7)
```

***Congragulations, installation is succesfull...***, Now please follow the instructions to generate your first website and make it live using [gh-pages](https://pages.github.com/)

Launching mkdocs website on `gh-pages` invloves three stpes 

1. Creating a `git` repository
2. Creating `mkdocs` website in the local repository
3. Building and deploying the site to `gh-pages`

Once you finished these three steps, your site is online.

## Creating a `git` repository

`mkdocs` offers inbuilt support to deploy the website on `gh-pages`, provided by GitHub. Hence for that to happen you need to create a repository on GitHub and Pull it to your computer. 
To create a repository on GitHub, please follow the instructions posted [here](https://vijaypolimeru.github.io/Something_Abt_Everything/Misc/Git_Rel/#creating-a-git-repo-from-command-line-and-push-to-github).

If you are working on windows/mac, you can use GitHub Desktop application to create your repository from GitHub Desktop itself. On Linux machines using `Kernel` is the easiest way.

## Creating `mkdocs` website in the local repository

Once `git` repository is created, type the command `python -m mkdocs new [dir-name]`, this will create a folder with name as `dir-name` with in the folder 
you see a subfolder called `docs` and a file named `mkdocs.yml`. To see the live website while developing it type the commnad `python -m mkdocs serve` on command 
prompt and type the link which appears on command prompt, which probaly looks like this `http://127.0.0.1:8000` copy it and paste it in your browser. You will see a site like this 

![like this](/images/ssg/firstsite.PNG)

## Building and deploying the site to `gh-pages`

Once the site is developed, type `python -m mkdocs build` follwed by `python -m mkdocs gh-deploy`. Your site will shortly appear on `https://username.github.io/repository-name/`

In the subsequent posts, we will discuss in detail about basic concepts like *styling your pages, modifying yml file, adding plugins etc.* and advanced cocepts like *enhancing the theme, developing your own themes etc.*

---
Hope this information may be useful…

***Note*** - If any example is not working or any links are not working, please comment I will update with appropriate ones…

Last Updated: 2020-03-09