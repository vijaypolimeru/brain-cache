---
layout: post
author: "Vijay Kumar Polimeru"
title: "Arrays - Tcl Master Series"
permalink: /arrays-learn-tcl-programming-from-scratch/
tags:
  - Tcl Master Series
comments: true
more_updates_card: true
---

This post in the [Tcl Master Series](/Learn-Tcl-Programming-from-Scratch/) is dedicated to discuss various types of ***arrays*** and their operations in Tcl. 

Tcl supports two types of arrays, 

2. ***Associative Array*** - In which a group of elements (numbers or strings) are systematically arranged using *Indices* which are not necessarily a number.
1. ***Conventional Array*** - In which a group of elements (numbers) are systematically arranged using *Indices*. In Tcl every array is associative.
However, by using only positve integer indices, we can make an associative array behave like a conventional array.  


#### ***Associative Arrays***

1. The syntax for a *creating* Associative array is `set ArrayName(Index_ID) Value` (Value - can be a number or string, Index_ID - can also be a number or string). 
2. The syntax for a *calling* conventional array is `$ArrayName(Index_ID)`, if you know the Index_ID then you can use it directly to get value in that index,
else first you must know all the Index_IDs. To know the index_ids use `set Index_ID_List [array names ArrayName];` this sets all the index_ids in a list named `Index_ID_List` (you can use any name here) in a random order.
3. The syntax for finding the Array Size is `set Size_Variable_Name [array size ArrayName]`- It is a type of expression whose output is an integer and must be stored in a variable.


Examples on *Associative arrays*

1. Basic Operations

	```tcl
	set Ass_Array(Age) 1;
	set Ass_Array(Height) 1.5;
	set Ass_Array(1) [expr 2.0/3.0]; # Index ID can also be a number
	set Ass_Array(3.5) [expr 10/5]; # Index ID can also be a floating point number
	set Ass_Array(Name) My_Name; # No Spaces
	set Ass_Array(Full_Name) "My Full Name"; 

	puts "$Ass_Array(Full_Name)"

	set Size_Ass_Array [array size Ass_Array]; # it returns 5
	set A [array names Ass_Array]; # or simply use
	puts [array names Ass_Array]; to print the index_ids

	```
 
2. Array Iteration

	```tcl
	foreach index_ids [array names Ass_Array] {
	   puts "Ass_Array($index_ids): $Ass_Array($index_ids)"
	}
	```
	
#### ***Conventional Arrays***

As said before, Tcl does
not know the difference between associative and conventional arrays, by using *+ve integer* indices we are making an associative array
behave like a one dimensional and multi dimensional conventional arrays.

##### ***One Dimensional Arrays (aka Vectors)***

Syntaxes

1. The syntax for a *creating* conventional array is `set ArrayName(Index) Value` (Value - can be a number or string, Index - Is a +Ve Integer starting from `0`). 
2. The syntax for a *calling* conventional array is `$ArrayName(Index_Value)` (you must know the index value). If index value is stored in another varaible then `$ArrayName($Index_Value)`.
3. The syntax for finding the Array Size is `set Size_Variable_Name [array size ArrayName]`- 
It is a type of expression whose output is an integer and must be stored in a variable.


Examples

1. Basic Operations
	```tcl
	set Num_Array(0) 1;
	set Num_Array(1) 1.5;
	set Num_Array(2) [expr 2.0/3.0];
	set Num_Array(3) Vijay; # No Spaces
	set Num_Array(4) "Vijay Kumar"; # With Spaces, double quotes are necessary otherwise it is an error (wrong # args: should be "set varName ?newValue?")

	set Size_Num_Array [array size Num_Array]; # it returns 5


	puts "Num_Array(0) = $Num_Array(0) \n";
	puts "Num_Array(1) = $Num_Array(1) \n";
	puts "Num_Array(2) = $Num_Array(2) \n";
	puts "Num_Array(3) = $Num_Array(3) \n";
	puts "Num_Array(4) = $Num_Array(4) \n";
	puts "Size_Num_Array = $Size_Num_Array \n"; # $Size_Num_Array(0) is an error (can't read "Size_Num_Array(0)": variable isn't array)
	``` 
	or
	```tcl
	set Index_Value 0;
	puts "Num_Array($Index_Value) = $Num_Array($Index_Value) \n";
	```
2. Array Iteration

	If you use indices starting from `0,1,2,3....n` then you can query them using a any looping technique (for, foreach, while etc.), else if you
	use non-continuous numbers `10,4, 5, 5.5....n` then the querying process is similar to associative arrays.

	```tcl
	for { set Index_Value 0 }  { $Index_Value < [array size Num_Array] }  { incr Index_Value } {
		puts "Num_Array($Index_Value) = $Num_Array($Index_Value) \n";
	}
	```
	
##### ***Multi Dimensional Arrays (aka Matrices)***

Syntaxes

1. The syntax for a *creating* conventional multi dimensional array is `set ArrayName(Index_i,Index_j) Value` (Value - can be a number or string, Index_i and Index_j 
- are +Ve Integers starting from `0`). ***Note-***, 
	1. `set ArrayName(Index_i,Index_j) Value` is correct
	2. `set ArrayName(Index_i, Index_j) Value` is error, becuase ***space*** is not allowed in index.
2. The syntax for a *calling* multi dimensional array is `$ArrayName(Index_i,Index_j)` (you must know the index values). 
If index value is stored in another varaible then `$Array_i_Name($Index_Value_i),$Array_j_Name($Index_Value_j)`.
3. The syntax for finding the Array Size is `set Size_Variable_Name [array size ArrayName]`- 
It is a type of expression whose output is an integer and must be stored in a variable. You will only get the total number of elements
in the matrix, getting a number of columns and number of rows saperately is not possible.

Examples

1. Basic Operations
	```tcl
	set nd_Array(0,0) 1;
	set nd_Array(0,1) 1.5;
	set nd_Array(0,2) [expr 2.0/3.0];
	set nd_Array(1,0) Vijay; # No Spaces
	set nd_Array(1,1) "Vijay Kumar"; # With Spaces, double quotes are necessary otherwise it is an error (wrong # args: should be "set varName ?newValue?")
	set nd_Array(1,2) [expr rand()];
	```
2. Array Iteration

	If you use indices starting from `0,1,2,3....n` then you can query them using a any looping technique (for, foreach, while etc.), else if you
	use non-continuous numbers `10,4, 5, 5.5....n` then the querying process is similar to associative arrays.

	```tcl
	for { set i 0 }  { $i < 2 }  { incr i } {
		for { set j 0 }  { $j < 3 }  { incr j } {
			puts "nd_Array($i,$j) = $nd_Array($i,$j) \n";
		}
	}
	```
	
A more general approach to create and perform operations on matrices (such as creation, addition, substraction, multiplication, determinant, inversion etc.)
are presented using [here](/tcllib-examples-learn-tcl-programming-from-scratch/) using ***Standard Tcl Library (Tcllib)***

***Note*** - Use `for` loop for conventional arrays and `foreach` loop for associative arrays, becuase it is easy to play with indices using `for` loop.

More concepts on arrays will be added soon...

Hope this information may be useful…

***Note*** - If any example is not working or any links are not working, please comment I will update with appropriate ones…

