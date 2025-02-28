---
layout: post
author: "Vijay Kumar Polimeru"
title: "Standard Tcl Library (Tcllib) - Examples - Tcl Master Series"
permalink: /tcllib-examples-learn-tcl-programming-from-scratch/
tags:
  - Tcl Master Series
comments: true
more_updates_card: true
---

This post in the [Tcl Master Series](/Learn-Tcl-Programming-from-Scratch/) is dedicated to discuss various packages 
available in the ***Standard Tcl Library (Tcllib)***. The emphasis is particularly laid upon
the packages related to mathamatical operations.

The detailed documentation of ***Tcllib*** can be found [here](https://core.tcl-lang.org/tcllib/doc/tcllib-1-20/embedded/md/toc.md)

## namespaces and packages

Before going to discuss about the usage of various libraries in ***tcllib***, it is very essential to know about a concept called `namespace`. 
In a computer program, the names of all program elements (such as variables, function names, memory addresses etc.) must be unique. 
A namespace is an container created to hold the names of all program elements. The elements in a namespace are accessed using `::` called 
*scope resolution operator*. Examples are as follows

1. If `add` is a function residing in `math` namespace, then `add` can be accessed as `::math::add`
2. If `mean` is a function residing in `statistics` namespace which is nested in `math` namespace, then `mean` can be accessed as `::math::statistics::mean`

Packages are reusable units of code, in general these are also called as *libraries*. Usually, every package comes with its own `namespace` or sometimes have multiple 
`namespaces`. *Tcllib*  has plethora of packages available for every purpose. To use a function from a package, we must first add it to our program using
the command `package require packagename version_number` (`version_number` is optional).

Lets discuss some examples to understand using *Tcllib*

## Vectors and Matrices

Various operations on vectors and matrices are explained through the following examples.

#### *Example 1* - Creating vectors and matrices

Tcllib provides `mkVector ndim value` and `mkMatrix nrows ncols value` to create vectors and matrices. In matrix each row is arranged as a ***list***.
However, these matrices or vectors are initialised with a `value`, which have to be modified later.

```tcl
package require math::linearalgebra

namespace eval mm namespace import ::math::linearalgebra::*

set mat1 [mm::mkMatrix 2 3 0]; # a 2X3 matrix, with elements as zeros
set mat2 [mm::mkMatrix 4 4 1]; # a 4X4 Square matrix, with elements as ones

set vec1 [mm::mkVector 5 0]; 

puts $mat1
puts $mat2

puts $vec1
```

#### *Example 2* - Getting size (number of rows and columns)

To iterate through various indices of a matrix, it is essential to know the number of rows and columns upfront. *tcllib* does not have special functions for
this purpose. However, since each row of a matrix is a *list* and number of elements in each row
is equal to the number of columns, we can use functions of *lists* (such as `llength` and `lindex`) for this purpose,

```tcl
package require math::linearalgebra

namespace eval mm namespace import ::math::linearalgebra::*

set mat1 [mm::mkMatrix 2 3 0]; # a 2X3 matrix, with elements as zeros

puts "no. of rows in mat1 = [llength $mat1]"
puts "no. of columns in mat1 = [expr {[llength [lindex $mat1 0]]}]"
```

#### *Example 3* - Getting and Setting elements in a matrix

To set and get elements in a matrix, *Tcllib* provides, two special functions `getelem matrix row col` and `setelem matrix row ?col? newvalue`. `newvalue` can be a number or string.
However, matrix operations such as inverse, determinant, addition, substraction, etc can be performed only on numbers

```tcl
package require math::linearalgebra

namespace eval mm namespace import ::math::linearalgebra::*

set mat1 [mm::mkMatrix 2 3 0]; # a 2X3 matrix, with elements as zeros

puts $mat1

for { set i 0 }  { $i < [llength $mat1] }  { incr i } {
    for { set j 0 }  { $j < [expr {[llength [lindex $mat1 0]]}] }  { incr j } {
        mm::setelem mat1 $i $j [expr rand()]
    }
}

puts $mat1
puts [mm::getelem $mat1 1 1]
```

#### *Example 4* - Addition, Substraction, Multiplication, Determinant and Inverse

Addition, Substraction, Multiplication and Determinant have straight forward procs for evaluation in *tcllib*. However, there are
several functions (such as Gauss, PGauss, Triangular etc.) for evaluating inverse 


```tcl
package require math::linearalgebra

namespace eval mm namespace import ::math::linearalgebra::*

set mat1 [mm::mkMatrix 5 5 0]; # a 4X4 matrix, with elements as zeros
set mat2 [mm::mkMatrix 5 5 0]; # a 4X4 matrix, with elements as zeros

for { set i 0 }  { $i < [llength $mat1] }  { incr i } {
    for { set j 0 }  { $j < [expr {[llength [lindex $mat1 0]]}] }  { incr j } {
        mm::setelem mat1 $i $j [expr rand()]
        mm::setelem mat2 $i $j [expr rand()]
    }
}

puts $mat1
puts $mat2

# Addition, Substraction, Multiplication and Determinant

set sum_mats [mm::add_mat $mat1 $mat2]
set diff_mats [mm::sub_mat $mat1 $mat2]
set Multip_mats [mm::matmul $mat1 $mat2]
set det_mat2 [mm::det $mat2]

# Inverse

set matID [mm::mkIdentity [llength $mat2]]
set mat2_inv [mm::solvePGauss  $mat2 $matID]

puts "Check Inverse = [mm::matmul $mat2_inv $mat2]"

```

---

More examples will be added soon...

Hope this information may be useful…

***Note*** - If any example is not working or any links are not working, please comment I will update with appropriate ones…

Last Updated: 2020-03-24