---
layout: post
author: "Vijay Kumar Polimeru"
title: "Lists - Tcl Master Series"
permalink: /lists-learn-tcl-programming-from-scratch/
tags:
  - Tcl Master Series
comments: true
more_updates_card: true
---

This post in the [Tcl Master Series](/Learn-Tcl-Programming-from-Scratch/) is dedicated to discuss various types of ***lists*** and their operations in Tcl. 

By default every variable in `.tcl` is a list. A list is similar to conventional array (only integers can be used to access the elements in the list).

1. First way

	```tcl
	set i 0;
	set temp_list1 {$i [expr $i + 1] [expr $i+2]}
	set temp_list2 {$i [expr $i + 1] [expr $i+2] sample text}

	puts "$temp_list1"
	puts "$temp_list2"
	```
	if the elements are defined in between `{ }` then they are treated as strings, when you compile the code you will get an output like this `$i [expr $i + 1] [expr $i+2]`

2. Second way

	```tcl
	set i 0;
	set temp_list1 "$i [expr $i + 1] [expr $i+2]"
	set temp_list2 "$i [expr $i + 1] [expr $i+2] sample_text"
	puts "$temp_list1"
	puts "$temp_list2"
	```
	if the elements are defined in between `" "` then the expersssions defined in the list elements are evaluated, i.e. when you compile the code you will get an output like this `0 1 2`. This can accept strings too

#### Accessing list elements

1. Using `for` loop
	```tcl
	set i 0;
	set temp_list "$i [expr $i + 1] [expr $i+2]"
	for {set i 0} {$i < [llength $temp_list]} {incr i} {
		puts "[lindex $temp_list2 $i]"
	}  
	```
	**Note** - `[llength $temp_list]` returns the length of the list

#### Appending elements to list

1. Using `for` loop
	```tcl
	set list1 {}
	for {set i 0} {$i < 5} {incr i} {
		set temp_list "$i [expr $i + 1] [expr $i+2]"
		lappend list1 $temp_list; # lappend is the key word to which the new list is appeneded
	} 

	puts "$list1"; # To print the whole list
	puts "[lindex $list1 3]"; # To print element of a list
	puts "[lindex [lindex $list1 3] 2]"; # To print the element in the element of a list
	```
	**Note** - `[lappend old_list $new_list]` is the key word to which the new list is appeneded

More concepts on arrays will be added soon...

Hope this information may be useful…

***Note*** - If any example is not working or any links are not working, please comment I will update with appropriate ones…

