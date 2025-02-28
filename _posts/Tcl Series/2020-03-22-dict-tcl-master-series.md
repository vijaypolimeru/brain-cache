---
layout: post
author: "Vijay Kumar Polimeru"
title: "Dictionary - Tcl Master Series"
permalink: /dict-learn-tcl-programming-from-scratch/
tags:
  - Tcl Master Series
comments: true
more_updates_card: true
---

This post in the [Tcl Master Series](/Learn-Tcl-Programming-from-Scratch/) is dedicated to discuss various operations on ***Dictionaries*** in Tcl. 

A Dictionary is an collection of *`key-value`* pairs. A `value` can be an integer or double or array or a list or it can be another dictionary and `key` is
simply a *name* or *id* which we assign for each value.

#### **Creating a `dict`**

1. Method 1

	`set dictname [dict create key1 value1 key2 value2 ....]`

	```
	set algorithms [dict create algo1 Newton algo2 KrylovNewton algo3 Broyden]
	puts $algorithms
	```

2. Method 2

	`dict set dictname key value` - for creating single key value pair. This is primariliy used for changing a `value` in a dictionary created using
	Method 1.

	```
	dict set algorithms algo1 Newton
	puts $algorithms
	```

#### **Getting a value in a `dict`**

Every `value` in a dictionary is paired with a `key`, which means without a `key` we cannot 
retrive a `value` from a `dict`. The syntax is, `[dict get $dictname key]` 

```
set algorithms [dict create algo1 Newton algo2 KrylovNewton]

set algo [dict get $algorithms algo1];
puts $algo
```

#### **Getting all `keys` and all `values` in a `dict`**

The syntax to get all keys in a `dict` is `[dict keys $dictname]`. This returns all the `keys` in the form of list.

```
set algorithms [dict create algo1 Newton algo2 KrylovNewton]

set allkeys [dict keys $algorithms];
puts $allkeys
```

in the same way we can get all `values` in a `dict` in the form of a list using `[dict values $dictname]`

```
set algorithms [dict create algo1 Newton algo2 KrylovNewton]

set allvalues [dict values $algorithms];
puts $allvalues
```

#### **Iteration through a `dict`**

1. Using `for` loop

```
set algorithms [dict create algo1 Newton algo2 KrylovNewton algo3 Broyden algo4 BFGS algo5 etc.]
set allkeys [dict keys $algorithms]

for {set i 0} {$i < [llength $allkeys]} {incr i 1} {
    puts "The Value of key [lindex $allkeys $i] is [dict get $algorithms [lindex $allkeys $i]]"
}
```

1. Using `foreach` loop

```
set algorithms [dict create algo1 Newton algo2 KrylovNewton algo3 Broyden algo4 BFGS algo5 etc.]
set allkeys [dict keys $algorithms]

foreach key_id [dict keys $algorithms] {
   puts "The Value of key $key_id is [dict get $algorithms $key_id]" 
}
```

---

More details (if require) will be added soon...

Hope this information may be useful…

***Note*** - If any example is not working or any links are not working, please comment I will update with appropriate ones…

Last Updated: 2020-03-22