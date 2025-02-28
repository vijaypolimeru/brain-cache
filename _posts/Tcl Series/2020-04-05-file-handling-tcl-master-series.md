---
layout: post
author: "Vijay Kumar Polimeru"
title: "File Management - Tcl Master Series"
permalink: /file-management-learn-tcl-programming-from-scratch/
tags:
  - Tcl Master Series
comments: true
more_updates_card: true
---

This post in the [Tcl Master Series](/Learn-Tcl-Programming-from-Scratch/) is dedicated to discuss various ***File Management*** operations.

Basic file management operations such as open file, read data from file, write data to file, etc, can be performed as follows

#### **Open File**

The syntax to open file is `set file_id [open file_name access_type]`. 

In which `[open file_name access_type]` opens the file with given access_type and returns a 
unique file identifier into `file_id` which can be used for further operations
such as read, write, append data etc.

| Access Type | Description |
| :-----------| :----------------|
| r   | This opens and reads an existing file (file must exist). This is the default mode when no access type is specified  |
| w  | This opens an existing file for writing, it will also delete the data in the existing file , if the file does not exist then a new file is created with the given file_name  |
| a   | This opens an existing file for writing (file must exist), and appends the new data to the existing data|
| r+   | This opens an existing file (file must exist) for both reading and writing purposes, it appends the new data to the existing data|
| w+  | This opens an existing file for both reading writing, it will also delete the data in the existing file , if the file does not exist then a new file is created with the given file_name   |
| a+   | It is similar to access type `r+`, the only difference is, if the file does not exist then a new file is created with the given file_name |

#### **Read From File** 

The syntax to read file as `set file_data [read $file_id]`.
This command reads and stores the data into a string type variable `file_data`.

#### **Write to File**

Writing data into a file is done using `puts` command as `puts $file_name "text to write"` or `puts $filename $data_to_store`

#### **Close File**

The syntax to close a file is `close $file_id`

#### **Examples**

1. Generate and store data in a file called `data.out`

	```tcl
	for {set i 0} {$i < 10} {incr i} {
		lappend data [expr rand()]
	}

	puts $data

	set fid [open "data.out" w]
	puts $fid $data
	close $fid
	```
	
	on each run, new data will be stored in `data.out` file.
	
2. Read the `data.out` file and store it into a variable `file_data`

	```tcl
	set fid [open "data.out"]
	set file_data [read $fid]
	puts $file_data
	close $fid
	```
	`file_data` is a string type variable
	
3. Write new data to `data.out` in addition to exisiting data

	```tcl
	set fid [open "data.out" r+]
	set file_data [read $fid]
	puts $file_data

	for {set i 0} {$i < 10} {incr i} {
		lappend data [expr rand()]
	}

	puts $fid $data
	close $fid
	```
	if we replace `r+` with `w+`, then everytime the new data is added to the file after deleting the old data
	
Though, these are some basic file management operations, we never use them in this simplest form. We mainly operate on vectors, matrices, lists etc, performing
file management operations on these type of variables is not that straight forward. Example codes for performing file management on
these data types has been added [here](/some-useful-codes-learn-tcl-programming-from-scratch/), please do check them and give your feedback


---

More details (if require) will be added soon...

Hope this information may be useful…

***Note*** - If any example is not working or any links are not working, please comment I will update with appropriate ones…

Last Updated: 2020-03-22