---
layout: post
author: "Vijay Kumar Polimeru"
title: "Loops - Tcl Master Series"
permalink: /loops-learn-tcl-programming-from-scratch/
tags:
  - Tcl Master Series
comments: true
more_updates_card: true
---

This post in the [Tcl Master Series](/Learn-Tcl-Programming-from-Scratch/) is dedicated to discuss various types of ***loops*** and their operations in Tcl. 

---
Though there exists several kinds of looping systems available in Tcl. Primarily, `for`, `foreach` and `while` are very popular in Tcl. 
Each of them can be defined in the following ways 

1. `for` Loop
	``` tcl
	set N 100;
	for {set i 1} {$i < $N} {incr i 1} {
		puts "The Value of i = $i";
	}
	```

2. `foreach` Loop
	```tcl
	set Variable_Vector "1 2 3 4 5 6 7 8 9";

	foreach i $Variable_Vector {
		puts "The Value of i = $i";
	}  	
	```

3. `while` Loop
	```tcl
	set i 0;
	set N 100;
	while {$i < $N} {
		puts "The Value of i = $i";
		set i [expr ($i + 1)];
	} 	
	```
	or
	```tcl
	set i 0;
	set N 100;
	while {$i < $N} {
		puts "The Value of i = $i";
		incr i; # incr is equivalent to (set i [expr ($i + 1)])
	} 	
	```

---

More concepts on arrays will be added soon...

Hope this information may be useful…

***Note*** - If any example is not working or any links are not working, please comment I will update with appropriate ones…

