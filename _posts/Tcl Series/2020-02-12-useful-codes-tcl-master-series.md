---
layout: post
author: "Vijay Kumar Polimeru"
permalink: /some-useful-codes-learn-tcl-programming-from-scratch/
title: "Some Useful Practice Codes or Procedures - Tcl Master Series"
tags:
  - Tcl Master Series
comments: true
more_updates_card: true
---

This post in the [Tcl Master Series](/Learn-Tcl-Programming-from-Scratch/) is dedicated to discuss about various useful codes in Tcl. 

---
### **File Management Operations**

1. File with single vector of values
	```tcl
	set filename "Abc_123_Cde.out"; # Keep this file in the folder or if it is elsewhere provide location (set filename "C:\badfba\asdf\Abc_123_Cde.out";)
	set File_ID [open $filename r]; #Load the File (Abc_123_Cde.out) and read the values i
	set Variable_1 [read $File_ID]
	close $File_ID
	```
	*Example*, using the above varaible `Variable_1` in a `foreach` loop
	```tcl
	foreach counter $Variable_1 {
		set Temp_Var $counter
		puts "Print the value of Temp_Var = $Temp_Var"
	}
	```
	The use the vector `Variable_1` like anyother vector in `tcl`

2. File with Multiple vectors of values
	```tcl
	set filename "Abc_123_Cde.out"; # Keep this file in the folder or if it is elsewhere provide location (set filename "C:\badfba\asdf\Abc_123_Cde.out";)
	set File_ID [open $filename r]; #Load the File (Abc_123_Cde.out) and read the values i 

	for {set i 1} {$i < 100} {incr i 1} { # Say, 100 lines are there in the files with 5 Columns of equal Lengths
		gets $File_ID line
		scan $line "%i %i %i %f %f" Data_1($i) Data_2($i) Data_3($i) Data_4($i) Data_5($i) ; # Data_1,2,3,4 and 5 are vectors of equal length
	}
	```
	That's it, we have loaded a file and stored its contents in different vectors. Now you can used the vectors like anyother vector in the program.
	```
	foreach i $Data_1 {
		puts "Data_1($i) \t Data_2($i) \t Data_3($i) \t Data_4($i) \t Data_5($i)"	
	}  
	```
[Link](https://www.tutorialspoint.com/tcl-tk/tcl_file_io.htm), For more information on Tcl - File I/O,

### **Miscellaneous...**

#### ***Proc to Generate a Random Number between `MinValue` and `MaxValue`***
```tcl
proc RandomValueGenerator { MinValue MaxValue} {
    set RandValue [expr $MinValue + rand()*($MaxValue - $MinValue)];
	return $RandValue;
}

puts [RandomValueGenerator -10 -10.5];
puts [RandomValueGenerator  0.1 0.2];
puts [RandomValueGenerator  10 -10.5];
```
	
---

More concepts on arrays will be added soon...

Hope this information may be useful…

***Note*** - If any example is not working or any links are not working, please comment I will update with appropriate ones…

