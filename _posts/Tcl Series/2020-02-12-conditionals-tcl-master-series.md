---
layout: post
author: "Vijay Kumar Polimeru"
title: "if..elseif..else... - Tcl Master Series"
permalink: /conditionals-learn-tcl-programming-from-scratch/
tags:
  - Tcl Master Series
comments: true
more_updates_card: true
---

This post in the [Tcl Master Series](/Learn-Tcl-Programming-from-Scratch/) is dedicated to discuss various types of ***conditional statements*** and their operations in Tcl. 

---
***If...else if ... else***, syntax in Tcl language is

1. Syntax

	```tcl
	if {boolean_expression 1} {
	   # Executes when the boolean expression 1 is true
	} elseif {boolean_expression 2} {
	   # Executes when the boolean expression 2 is true 
	} elseif {boolean_expression 3} {
	   # Executes when the boolean expression 3 is true 
	} else {
	   # executes when the none of the above condition is true 
	}
	```
	Example
	```tcl
	set Time_Step 0.005;
	set 
	set ok [analyze 1 $Time_Step]
	if {$ok == 0} { 
		puts "i = $i \t Time_Step = $Time_Step -----------------------------"
	} elseif {$ok < 0} {
		puts "i = $i \t OK value = $ok -----------------------------"
	} else {
		break; # It breaks a for loop
	}
	```
	If the Boolean expression evaluates to true, then the if block of code will be executed, otherwise the elseif block of code will be executed, otherwise the else block of code will be executed.
	
2. Multiple Conditions in ***If*** statement (Make sure the if condition starts with a  *curly braces `{}`*)

	```tcl
	if {($i == 0) || ($i == 4)} {
		set node_num [expr $nodeStartID + $j];
		set node_x [expr $deltaL*$j];
		set node_y [expr $deltaH*$i];
		lappend node_data "$node_num $node_x $node_y"
	}
	```

2. List of Qualified Operators in Tcl (**Note** - use `expr` and `$` while evaluating the following expressions)

	1. Arithmetic operators (`set A 3` and `set B 10`) 

		| Operator | What it does? | Example |
		| :------| :-----------|:-----|
		| +   | Adds two numbers | A + B will retun `13` |
		| -   | Substract two numbers (second from first) | A - B will return `-7` |
		| *   | Multiplies two numbers | A*B will return `30` |
		| /   | Divides Numberator by Denominator. (Note, to return a float value either one of A or B must be a float value) | A/B will return `0` and `3./10` will retrun `0.3`|
		| %   | Returns the remainder after division of two integer numbers (For `%` to work A and B must be integers )| A % B will return `3` |

	2. Relational operators (`set A 3` and `set B 10`)

		| Operator | What it does? | Example |
		| :------| :-----------|:-----|
		| ==   | Checks equality of two numbers | (A == B) will retun `0` |
		| !=  | Checks inequality of two numbers | (A != B) will return `1` |
		| > and <   | Checks if the (strictly) left value is less than the right value (similiarly for greater than) | (A > B) will return `0` and (A < B) will return `1` |
		| >= and =<   | Checks if the left value is Less than or equal to the right value (similiarly for greater than) | (A >= B) will return `0` and (A =< B) will return `1`|
		
	3. Logical operators (`set A 1` and `set B 0`)

		| Operator | What it does? | Example |
		| :------| :-----------|:-----|
		| &&   | AND operator | (A && B) will retun `0` |
		| \|\|  | OR operator | (A \|\| B) will return `1` |
		| !   | NOT operator | !(A && B) will return `1` |
		
		

---

More concepts on arrays will be added soon...

Hope this information may be useful…

***Note*** - If any example is not working or any links are not working, please comment I will update with appropriate ones…

