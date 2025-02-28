---
layout: post
author: "Vijay Kumar Polimeru"
title: "Setting up IDE for Tcl Practice"
permalink: /ide-setup-tcl-programming-from-scratch/
tags:
  - Tcl Master Series
comments: true
more_updates_card: true
---

This post in the [Tcl Master Series](/Learn-Tcl-Programming-from-Scratch/) is dedicated to setup various online and offline IDE(s) for practicing Tcl.

# Komodo

In this series we primarily use ***Komodo*** as our IDE for practice. Komodo is an opensource project ([free](https://www.dropbox.com/s/oszg3ozq3lpk6o5/Tcl_komodo_free.PNG?dl=0)) from *Active-State*, along with Tcl it supports several other languages. However,
we use this for Tcl only in this course. The Latest version [Komodo-v12.0.1](https://www.activestate.com/products/komodo-ide/download-ide/) is throwing some [strange bug](https://www.dropbox.com/s/3t61lpbf3leif3h/Tcl_komodo_12_error.PNG?dl=0) in windows 7, which makes
it unable to use. Hence will be using **Komodo-v11** for this course, which can be downloaded from [here](https://forms.gle/Y6fcxHmognsrHS4m7).

Installation of **Komodo-v11** is straight forward, no complex steps involved in the process (list of steps provided below). However, you may need to register when you open the IDE for the first time, hence 
register yourself [here](https://platform.activestate.com/create-account?utm_campaign=create-account&utm_medium=website&utm_source=activestate.com&utm_term=create-account&utm_content=top-bar-menu)
and keep your user-id and password in hand.

## Steps

1. Download and install latest version of Tcl from [here](https://www.activestate.com/products/tcl/downloads/), this may work as expected. However, in the present 
series we will be using Tcl. 8.5 (64 Bit) version, which you can download from [here](https://forms.gle/Y6fcxHmognsrHS4m7).
2. Double click on the 'Komodo-IDE-11.1.1-91089.msi' and follow the regular steps (*next-->next--> etc*). After succesful installation, first look will be like this.

<img src="/images/komodo_firstlook.png" class="align-center" alt="" width="600">

To test, whether the IDE is working properly or not. Create a file and paste the following code in it

```tcl
set a 1;
set b 2;
set c [expr $a + $b]

puts "Hello World, the sum of a and b is $c"
```

and the ***run*** button in the top menus, you will be prompted following pop-up, check the `use default tclsh interpreter (for console applications)` and press ok

<img src="/images/komodo_config.png" class="align-center" alt="" width="300">

you will see the following output in the output window.

<img src="/images/komodo_output.png" class="align-center" alt="" width="450">

Thats simple it is. If you face any difficulties while installation, first refer [here](https://community.komodoide.com/) for potential solution. If you did not
found any solution, please comment in the comment section, I will try to resolve the issue.

# Tcl Inbuilt executable ***`tclsh.exe`***

Tcl has an inbuilt compiler called `tclsh.exe`, it will be in `C:\yourpath\Tcl\bin` folder. It also has another executable `tclsh85.exe` (since we installed Tcl8.5), you can use either one and just follow the steps to execute the code

1. Double click the `tclsh.exe` or `tclsh85.exe`.
2. Navigate to the `inputfile.tcl`  folder using `cd` commad
3. Just type `tclsh inputfile.tcl` and press enter

Komodo uses the same executable to run the `.tcl` scripts. We can execute the same without Komodo IDE. However, Komodo provides additional features
such as variable type viewer, debugging using break points etc.


# Other Online Compilers - for quick reference 

Following are some online tools (*I Prefer most*) to compile and cross verify the *.tcl* code given below

1. [Tutorials-Point IDE](https://www.tutorialspoint.com/execute_tcl_online.php)
2. [RexTester](https://rextester.com/l/tcl_online_compiler)

---

More details (if require) will be added soon...
   
Hope this information may be useful…

***Note*** - If any example is not working or any links are not working, please comment I will update with appropriate ones…
