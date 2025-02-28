---
layout: post
author: "Vijay Kumar Polimeru"
title: "Exception Handling - Tcl Master Series"
permalink: /exception-handling-learn-tcl-programming-from-scratch/
tags:
  - Tcl Master Series
comments: true
more_updates_card: true
---

This post in the [Tcl Master Series](/Learn-Tcl-Programming-from-Scratch/) is dedicated to discuss various ***Exception Handling*** operations.

In this post we will understand tackling a very specific set of ***exceptions*** called ***errors*** using `error` and `catch` commands. 

The `error message` and `error location` are two important features essential for users to resolve the error. 

1. Error Message - gives description about the error, for example when I execute `puts "print this`, Komodo, throws an error message as follows

	```
	missing "
		while executing
	"puts "print this
	```
	it gives us an idea about what is wrong with the code, in this case it shound be `puts "print this"`

2. Error Location - The complete stack trace with line numbers, i.e. all the nested functions starting from the from the file which we executed. In the above
example the stack trace will `(file "error-file-1.tcl" line 1)`. Since it has only one line of code.

A more detailed example is as follows,

```
proc fun3 {a b} {
    return [fun2 $a $b]
}
proc fun2 {a b} {
    return [fun1 $a $b]
}
proc fun1 {a b} {
   return [expr tan($a/$b)]
}
puts "Result = [fun1 10 0]"
```

In this case the error message will be `divide by zero` and the stack trace will be

```
    while executing
"expr tan($a/$b)"
    (procedure "fun1" line 2)
    invoked from within
"fun1 10 0"
    invoked from within
"puts "Result = [fun1 10 0]""
    (file "error-file-1.tcl" line 13)
```

`Tcl` will take care of all the error handling mechanism, however, if the developer wants to show a custom error messages for some specific type of 
calculations, in that case this can be done using the `error` and `catch` commands, in their simplest form, these commands can be implemented as follows

1. `error errorMsg`
2. `catch {command} variable`

For example, the above code can be re-written as follows

```
proc fun3 {a b} {
    return [fun2 $a $b]
}
proc fun2 {a b} {
    return [fun1 $a $b]
}
proc fun1 {a b} {
   if {$b == 0} {
      error "Division not possible, because b = $b"
   } else {
      return [expr tan($a/$b)]
   }
}

catch {puts "Result = [fun3 24 2]"} errormessage
puts $errormessage

```

1. If we execute this using `[fun3 24 2]`, it outouts `Result = -0.6358599286615808` 
2. Else if we execute this using `[fun3 24 0]` it outputs error message `Division not possible, because b = 0` but does not provide stack trace, to get stack trace
we have to explicitly ask `errorInfo` using `puts` as follows

	```
	proc fun3 {a b} {
		return [fun2 $a $b]
	}
	proc fun2 {a b} {
		return [fun1 $a $b]
	}
	proc fun1 {a b} {
	   if {$b == 0} {
		  error "Division not possible, because b = $b"
	   } else {
		  return [expr tan($a/$b)]
	   }
	}

	if {[catch {puts "Result = [fun3 24 0]"} errormessage]} {
	   puts $errormessage
	   puts $errorInfo
	}
	```
	if we execute this we get
	```
	Division not possible, because b = 0
	stack trace is ....
		(procedure "fun1" line 1)
		invoked from within
	"fun1 $a $b"
		(procedure "fun2" line 2)
		invoked from within
	"fun2 $a $b"
		(procedure "fun3" line 2)
		invoked from within
	"fun3 24 0"
	```
	
***Note -*** Sometimes both Komodo IDE and `tclsh.exe` will provide stack trace in different formats, I suggest to use both to get to 
appropriate error location.

---

More details (if require) will be added soon...

Hope this information may be useful…

***Note*** - If any example is not working or any links are not working, please comment I will update with appropriate ones…

Last Updated: 2020-03-22
