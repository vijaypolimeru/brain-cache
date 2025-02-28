---
layout: post
author: "Vijay Kumar Polimeru"
title: "A Simple Algorithm to Define Cyclic Constitutive Material Model - with example code"
permalink: /cyclic-constitutive-material-model/
tags:
  - Advanced Mechanics of Reinforced Concrete
comments: true
usemathjax:     true
more_updates_card: true
---
Defining constitutive relationships ($$ \sigma - \epsilon $$) of the constituent materials is one of essential steps in the 
formulation of nonlinear finite element models. When the $$ \sigma - \epsilon $$ relationship is linear such as $$ \sigma = E\epsilon $$, it is very easy, one line of
code is enough. However, when the $$ \sigma - \epsilon $$ relationship is nonlinear ([like this](/images/amrc/steel01.jpg) - this is the simplest example)
it is very difficult to define. The number of load paths (unloading and reloading) will define the complexity of the code. 

Any wrong definition of load path results in erroneous results or will show convergence issues. This process requires an *easy to read* and *easy to debug* algorithm. In this post, an attempt have 
been made to provide such an algorithm for [steel01](https://opensees.berkeley.edu/wiki/index.php/Steel01_Material), which is shown in Figure. 1. 

Figure 1 

<img src="/images/amrc/steel01.jpg" class="align-center" alt="" width="400">

(Note - For simplicity purposes, the influence of parameters $$ a_1, a_2, a_3, a_4 $$ have been neglected and all the three load states involved in steel01, have been segregated into individual loadstates as shown in Figure. 2. However, creating such
individual load states will ease the process of implementation of cyclic constitutive relationship in a computer program) 

The basic idea (as shown in Figure. 2) is that, if at any instant the previous strain (OStrain, i.e. strain at step `(i-1)`) is in a load state (LoadState) 
represented by *solid black line* in Figure. 2, the current strain (CStrain, i.e. strain at step `i`) lies in any one of the load states 
represented by *dashed black line*. Our objevtive is identify that current load state and calculating the stress by using the equations of that load state. 

Figure 2 

<img src="/images/amrc/load-states.jpg" class="align-center" alt="" width="600">

This can be implemented in the program as follows,

```matlab
if (LoadState == 1)
	if (dStrain(i) > 0) % Represents change in direction
		if (CStrain < eps_y)
			LoadState = 1;
		else
			LoadState = 2;
		end
	else
		if (CStrain > 0)
			LoadState = 1;
		else
			if (CStrain > -eps_y)
				LoadState = 3;
			else
				LoadState = 4;
			end
		end
	end
elseif (LoadState == 2)
...
...
...
end	
```
A sample Matlab code for the load states of steel01 as shown in Figure. 2
for a random strain profile is provided [here](https://docs.google.com/forms/d/e/1FAIpQLSd7xTwaWpJH89Cx8kfjO-ab9w6d-mS-rF_HZX6-uyzp8Lpb0Q/viewform?usp=sf_link) for further understanding, please download and comment your feedback and errors (if any).
The equations involeved in every load path are available in the code. 

---
Hope this information may be useful…

***Note*** - If any example is not working or any links are not working, please comment I will update with appropriate ones…

