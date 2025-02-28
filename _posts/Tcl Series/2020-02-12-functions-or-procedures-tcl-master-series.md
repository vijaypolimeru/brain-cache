---
layout: post
author: "Vijay Kumar Polimeru"
title: "Functions or Procedures - Tcl Master Series"
permalink: /procedures-learn-tcl-programming-from-scratch/
tags:
  - Tcl Master Series
comments: true
more_updates_card: true
---

This post in the [Tcl Master Series](/Learn-Tcl-Programming-from-Scratch/) is dedicated to discuss about various operations on ***Procedures*** in Tcl. 

---
### Creating ***functions (or procedures)*** 

Tcl Procedures are similar to the functions in other programming languages. They basically avoid repeating the same code
at multiple locations. Procedures are created using `Proc` command. A simple Procedure has the following syntax
```tcl
proc procedureName {arguments} {
   body of code
   return $var
}
```

1. ***Example - 1***, Definition of a simple `proc` to check `puts` command
	```tcl
	proc CheckPutsCommand {} { ;# No Input Arguments
	   puts "Hurray, Puts is working"
	   
	}
	CheckPutsCommand
	```
	Upon exection, following output will be printed in the console (*Note*, `proc` name is case-sensitive, both calling and defining names should be same)
	```
	Hurray, Puts is working
	```

2. ***Example - 2***, Definition of a `proc` with Multiple but single valued arguments
	```tcl
	proc AddNumbers { a b} { ;# Input Arguments
	   set sum [expr $a + $b]
	   return $sum;
	   
	}
	AddNumbers 10 30
	```
	Upon exection, following output will be printed in the console
	```
	40
	```

3. ***Example - 3***, Definition of a `proc` with ___Multiple Variable___ arguments (each argument is a vector)
	```tcl
	proc CalculateMean { InputData } { ;# Input Arguments
	   set Sum 0;
	   foreach InputData_i $InputData {
		 set Sum [expr $Sum + $InputData_i]
	   }
	   set Mean [expr $Sum/[llength $InputData]]; # llength is inbuilt command, which returns the number of elements in the argument
	   return $Mean; 
	}
	set Mean_1 [expr [CalculateMean {10 30}] + [CalculateMean {10 30 40 50 60}]]; 
	set Mean_2 [expr [CalculateMean {30 {[CalculateMean {10 30}]}}]]; # slightly difficult command *giving `proc` as an argument*
	puts "Mean_1 = $Mean_1 \t Mean_2 = $Mean_2"
	```
	Upon exection, following output will be printed in the console (*Note*, Be careful while using braces, `tcl` is very bad at exception handling)
	```
	Mean_1 = 58      Mean_2 = 25
	```

4. ***Example - 4***, Definition of a `proc` with ___Default arguments___
	```tcl
	proc Multiply_a_and_b { a {b 10} } { ;# Input Arguments
	set Product [expr $a*$b]
	   return $Product; 
	}

	puts [Multiply_a_and_b 10 20]
	puts [Multiply_a_and_b 10]
	```
	Upon exection, following output will be printed in the console (*Note*, Be careful while using braces, `tcl` is very bad at exception handling)
	```
	200
	100
	```
5. ***NOTES*** - 
	1. While calling the funtion, if the function is located elsewhere you have to call the file also using `source C:\bladdh\adfadsff\filename.tcl` before calling the function. (like we call the header files in `c` or `c++` languages). 
	2. You can define any number of `procs` in a file.
	
---

More concepts on arrays will be added soon...

Hope this information may be useful…

***Note*** - If any example is not working or any links are not working, please comment I will update with appropriate ones…

