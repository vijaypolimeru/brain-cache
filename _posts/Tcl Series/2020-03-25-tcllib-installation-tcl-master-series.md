---
layout: post
author: "Vijay Kumar Polimeru"
title: "Standard Tcl Library (Tcllib) - Installation - Tcl Master Series"
permalink: /tcllib-installation-learn-tcl-programming-from-scratch/
tags:
  - Tcl Master Series
comments: true
more_updates_card: true
---

This post in the [Tcl Master Series](/Learn-Tcl-Programming-from-Scratch/) is dedicated to discuss various packages 
available in the ***Standard Tcl Library (Tcllib)***. The emphasis is particularly laid upon
the packages related to mathamatical operations.

#### **Download**

The latest version of standard Tcl library (Tcllib) can be downloaded from [here](http://www.tcl.tk/software/tcllib/). 
The examples pertaining to Tcllib presented hereafter are written using Tcllib 1.20, since it is the latest version when I am writing this post. which can be
downloaded from [here](https://forms.gle/Y6fcxHmognsrHS4m7)

The detailed documentation of ***Tcllib*** can be found [here](https://core.tcl-lang.org/tcllib/doc/tcllib-1-20/embedded/md/toc.md).

#### **Installation**

Following are the steps involved in the installation of Tcllib,

1. Unzip the `tcllib-1.20.zip` file (or the latest version)
1. Add the path `C:\Tcl\bin` (or the path of `yourpath\Tcl\bin` where ever you have installed `Tcl`) 
to the `path` variable. (Normally, when installing the Tcl 
this path automatically added to windows `path` variable, if not please add this now).
1. Type `tclsh` in the command prompt which is opened from the unzipped *tcllib-1.20* folder. (just navigate to the folder *tcllib-1.20*, 
highlight the complete folder path in the top pane and type "cmd").
1. Then type `tclsh installer.tcl` and wait for some time, till the installation is over.

#### **Example**

To check whether the installation is succesfull or not, download the Tcl file ([download link](https://forms.gle/Y6fcxHmognsrHS4m7)) and run the `stdlib-test.tcl`
file from Komodo IDE. If you can get an image something similar to the one shown as below, then the ***installation is successfull***. 
Since the `rand()` is used to generate the data, you may not get an exact image like the one shown below, you will get something similar to this.

<img src="/images/tcl-master-series/tcllib-test-success.png" class="align-center" alt="" width="250">

---

More details (if require) will be added soon...

Hope this information may be useful…

***Note*** - If any example is not working or any links are not working, please comment I will update with appropriate ones…

Last Updated: 2020-03-22