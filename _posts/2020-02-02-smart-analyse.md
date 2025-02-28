---
layout: post
author: "Vijay Kumar Polimeru"
permalink: /osees-convergence-issues/
title: "Simply Simplest tool to overcome non-convergence issues in OpenSees"
tags:
  - OpenSees
comments: true
more_updates_card: true
---

Convergence issues are pretty common in any nonlinear finite element program, OpenSees, however is also not immune to these. 
In case of a convergence error, opensees throws a strange *error message* like this

```
WARNING: CTest*::test() - failed to converge
after * iterations
 current EnergyIncr: * Norm deltaX: *, Norm deltaR: *
*::solveCurrentStep() - The ConvergenceTest object failed in test()
StaticAnalysis::analyze() - the Algorithm failed at iteration: * with domain at load factor *
OpenSees > analyze failed, returned: -3 error flag
```

It is just telling that `ConvergenceTest` object failed in `test()` and does not give any information about the source of error. 

Then, How to resove this??

In general, convergence issues occur primariliy due to inappropriate step size (too large or too small), stringent tolerances, algorithms, convergence test criteria. 
These are some of the possible sources of convergence issues. In special cases (such as inappropriately defined material models, elements and FE Mesh) Its very difficult 
to zero-in the source of error by optimising the step sizes, tolerances, algorithms etc. In such special cases it is very essential to correct the material models or 
elements before updating step-sizes, tolerances, algorithms etc. 

In this post we will discuss about some tools to resolve the convergence issues in general cases. The idea behind these tools is simply adaptively trying varying step-size, tolerances, 
algorithms. The simplest example of such adaptive tool for performing static pushover analysis can be found in the opensees examples ([link](https://opensees.berkeley.edu/wiki/images/7/70/Ex3.Canti2D.analyze.Static.Push.tcl)), 

```tcl
#  ---------------------------------    perform Static Pushover Analysis
set Nsteps [expr int($Dmax/$Dincr)];        # number of pushover analysis steps
set ok [analyze $Nsteps];                # this will return zero if no convergence problems were encountered

if {$ok != 0} {      
	# if analysis fails, we try some other stuff, performance is slower inside this loop
	set ok 0;
	set controlDisp 0.0;
	set D0 0.0;		# analysis starts from zero
	set Dstep [expr ($controlDisp-$D0)/($Dmax-$D0)]
	while {$Dstep < 1.0 && $ok == 0} {	
		set controlDisp [nodeDisp $IDctrlNode $IDctrlDOF ]
		set Dstep [expr ($controlDisp-$D0)/($Dmax-$D0)]
		set ok [analyze 1 ]
		if {$ok != 0} {
			puts "Trying Newton with Initial Tangent .."
			test NormDispIncr   $Tol 2000  0
			algorithm Newton -initial
			set ok [analyze 1 ]
			test $TestType $Tol $maxNumIter  0
			algorithm $algorithmType
		}
		if {$ok != 0} {
			puts "Trying Broyden .."
			algorithm Broyden 8
			set ok [analyze 1 ]
			algorithm $algorithmType
		}
		if {$ok != 0} {
			puts "Trying NewtonWithLineSearch .."
			algorithm NewtonLineSearch .8
			set ok [analyze 1 ]
			algorithm $algorithmType
		}
				};	# end while loop
};      # end if ok !0

```

Similar algorithms can be found in the opensees examples database for static cyclic and transient analysis aswell. 

OpenSees consists of many algorithms (8 algortihms namely Linear, Newton, ModifiedNewton, Newton with line search, KrylovNewton, SecantNewton, BFGS and Broyden are primarily used) and each algorithm 
has various options. On top of that each algorithm can be coupled with variety of convergence test objects available in opensees, various combinatons of step-sizes etc.

This humongous task can be easily perfomed with the help of a simple open-source tool called `SmartAnalyze.tcl` developed by [Hanlin Dong](http://www.hanlindong.com/en/2019/opensees-converge/).
In this tool all the available algorithms in opensees are pre-defined with various combinations of alogrithm options, convergence tests and tolerances.
This tool has a simple interface to connect the nonlinear finite element model with `SmartAnalyze.tcl` and there by perform static, quasi-static and transient anlyses. 
A simple example of transient analysis using `SmartAnalyze.tcl` is as follows

```
source SmartAnalyze.tcl
dict set control testTol 1.0e-2; # Change test tolerance
dict set control tryAlterAlgoTypes True; # Try to change algorithm (default: False)
dict set control algoTypes {40 20}; # Config the algorithms to run by a list of tags (refer to the comments in the code)
dict set control tryForceConverge True; # force the model to converge.


while {$controlTime < $TmaxAnalysis && $ok == 0} { 

	SmartAnalyzeTransient $DtAnalysis 1 control
	#set ok [analyze 1 $DtAnalysis];			# actually perform analysis; returns ok=0 if analysis was successful
	set controlTime [getTime]
	puts "Current Time In the Domain = $controlTime ---------------------------------------------------------------";
}

```

Readers can download version 2.2 of the tool, from [here](https://forms.gle/xDTXbCzkvg2w1Rz1A). However, more information and latest updates on the tool
can be found [here](http://www.hanlindong.com/en/2019/opensees-converge/).
