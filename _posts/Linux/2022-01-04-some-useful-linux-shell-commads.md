---
layout: post
author: "Vijay Kumar Polimeru"
title: "Some Useful Linux Terminal Commands And Code Snippets"
permalink: /linux-commads/
tags:
  - Linux Terminal
comments: true
more_updates_card: true
---

Following are some of the useful linux terminal commands and code snippets that enhances our productivity on linux terminal

# **Code Snippets**

---	
- Splitting a large text file into many number of smaller text files, ([Source Link](https://stackoverflow.com/q/25249516/9806044))


	```shell
       split -l 250 -d --additional-suffix=.txt $abc.txt abc
	```
	*where*, `-l 250` are number of lines to be kept in each file, `-d` is for numerical suffix (by default it uses alphabetical suffix)

---	
- Executing several comands in one go on linux terminal, ([Source Link](https://askubuntu.com/q/413866/952787))

	You can separate commands with `&&` or `;`. 

	- `&&` only runs the next command if the previous one exited with status 0 (was successful) :

			command1 && command2 && command3

	- `;` runs every commands, even if the previous one exits with a non zero status :

			command1; command2; command3

    You can combine these separators as you wish. 

---
- Open file browser
	- `nautilus` in the terminal to open file browser
	- `nautilus .` in the terminal to open file browser in the current directory

---	
- `echo $SHELL` , to know the type of shell that we are using.

---
- Search for hidden files in terminal directory `ls -la ~/ | more`.

---
- Automation
  - Create a ‘.tcshrc’ or `.bashrc` file in the home directory, and write the commands in that file, it will automatically run at the startup. 
  - If it is not loaded at the startup, then type `source ~/.bashrc` from any directory. `~` is most important, otherwise it throws a file not found error. 

---
- To clear the terminal type `clear && printf '\e[3J'` on screen (more explanation can be found [here](https://apple.stackexchange.com/a/113168)).

---
- Searching
  - To search for a text or for a word in a directory type, `grep -Ril "text-to-search"`

---
- File/Folder Opeartions
  - Remove all files except an extension - `rm -i !(*.zip)`
  - List files in a directory with a specific extension `ls *.{mp3,exe,mp4}`


More concepts on arrays will be added soon...

Hope this information may be useful…

***Note*** - If any example is not working or any links are not working, please comment I will update with appropriate ones…

