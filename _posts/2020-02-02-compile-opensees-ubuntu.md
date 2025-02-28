---
layout: post
author: "Vijay Kumar Polimeru"
permalink: /osees-compilation-ubuntu/
title: "Simply Simplest way to compile OpenSees in Ubuntu"
tags:
  - OpenSees
comments: true
more_updates_card: true
---
I have compiled OpenSees source code version 3.0.0 ([github-link](https://github.com/OpenSees/OpenSees/archive/v3.0.0.tar.gz)) on UBUNTU 18.04.2 LTS operating system 
using the [procedure](https://www.researchgate.net/post/How_to_install_opensees_in_UBUNTU), provided by [Mr. Farbood Panahi](https://www.researchgate.net/profile/Farbood_Panahi). 
Following are the detailed step-by-step instructions I followed for compiling this source code,

1. ***Dependency Check*** - Type the following commands in terminal to check whether the following prerequsites are installed, if not installed the command will automatically execute installing the softwares
	1. `sudo apt-get install make`
	2. `sudo apt-get install tcl8.6`
	3. `sudo apt-get install tcl8.6-dev`
	4. `sudo apt-get install gcc`
	5. `sudo apt-get install g++`
	6. `sudo apt-get install gfortran`
	7. `sudo apt-get install python3-dev`
2. Download the latest ***release*** version of the source code from the [link](https://github.com/OpenSees/OpenSees/releases). In this post, I have compiled the release [version 3.0.0 ](https://github.com/OpenSees/OpenSees/archive/v3.0.0.tar.gz). (`.zip` or `.tar.gz` any one is fine.)
3. Create two folders with names ***bin*** and ***lib*** in the *Home* directory. This *Home* is not necessarily the UBUNTU home directory, you can set any directory as *Home* directory for OPS. However, you have to specify the path for this *Home* directory in ***line-91*** of make file, which will be discussed in Step. 6.2.
4. Extract the downloaded OPS `.zip` or `.tar.gz` in the *Home* direcotry discussed in Step. 3 and rename it to ***OpenSees*** (O and S are capital letter - directory name is case-sensitive).
5. Goto ***MAKES*** folder inside the *OpenSees* directory and open the file ***Makefile.def.EC2-UBUNTU***.
6. Change the following lines and save the file,
	1. ***Line-90*** - `./usr/local` to `/usr/local` (i.e. just remove the dot)
	2. ***Line-91*** - `./home` to `/home/vijay` (i.e. just remove the dot and add your computer login-name, all small letters), if you are compiling in the Ubuntu *Home*. (or) `/home/vijay/Desktop/OPS_Compile` (example path for **HOME =** If you have created the folder elsewhere). Check - In this folder there will be three sub-folders **bin**, **lib** and **OpenSees**
7. Open the **Terminal** from the OpenSees folder and type the command `cp ./MAKES/Makefile.def.EC2-UBUNTU ./Makefile.def` and then type the command `make`. Wait untill the compilation is over (it took roughly about 15-20 minutes in my computer).
8. After the compilation finished, go to the bin folder (i.e. created in step 3). You will find a file named `OpenSees`.
9. Open the Terminal in ***bin*** and type `OpenSees`, thats all OPS will load and you can input any `tcl` file to it. Also you can copy this **OpenSees** file to whatever the directory you want.

An example showing, running the `Truss.tcl`([link](http://opensees.berkeley.edu/wiki/images/8/8e/Truss.tcl)) is as follows, (Just Hit the Enter, you will get the response of truss)

![opensees-ubuntu-example]({{ '/images/OPS_Ubuntu_Example.png' | absolute_url }}){: .align-center}