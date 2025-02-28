---
layout: post
author: "Vijay Kumar Polimeru"
title: "Introduction to Nonlinear Finite Element Analysis"
permalink: /nlfea-introduction/
tags:
  - NLFEA Master Series
comments: true
more_updates_card: true
---
Finite Element Analysis (FEA) is one of the several methods avaibale to solve differential equations that describe many engineering problems. This method is
formally introduced to the engineering students at under-graduate level to solve material and geometrically linear problems. An advanced version of 
this subject called Nonlinear Finite Element Analysis (NLFEA) is often introduced in the curriculum for post-graduate students. Most of the time it left
as a subject for self-study. For researchers who are working in the field of computational mechanics, a thorough understanding on this subject is very
essential.

In this series of posts on Nonlinear Finite Element Analysis, I will try to cover different topics involved in NLFEA. As a starting point, I have taken 
the following outline of contents from the [Lecture Notes](https://www.researchgate.net/publication/269411458_Nonlinear_Finite_Element_Analysis_Notes) 
written by [Prof. Ioannis Koutromanos](https://www.researchgate.net/profile/Ioannis_Koutromanos), because the contents are almost exhaustive and they will serve
as a good signposts to learn NLFEA. However, the content provided in respective posts is purely my understanding on the subject and also depending on the topic, 
I will introduce new contents along with more examples and MATLAB/Python codes. 


***Table of Contents***


1. Nonlinear Finite Element Analysis–A Point of Departure
	1. Revisiting the concept of linear elasticity 
	1. Introduction to Nonlinear material behavior
	1. Interlude: Description of Elastic behavior – Generic Description of Elastoplastic Materials 
	1. Numerical Description of Nonlinear stress-strain laws – The discrete approach
		1. Example of a stress-strain law and of algorithmic implementation: Uniaxial elastic-hardening material with linear isotropic hardening 
		1. Kinematic Hardening 
	1. Stress-Strain models in total form 
	1. Tangent slope of stress-strain diagram 
	
1. Introduction to Nonlinear Analysis of Trusses and Beams
	1. Nonlinear Analysis of Truss Structures 
	1. Nonlinear Analysis of Beam Structures
	1. Generalized stress – generalized strain relation for Nonlinear Euler-Bernoulli beams based on uniaxial material laws – The layer (fiber) section model.
	1. Solution of nonlinear equations – The iterative Approach 
		1. Example 2.1: Iterative solution of scalar nonlinear equation
		1. Example 2.2: Iterative solution of system of nonlinear equations
	1. Application of Iterative Solution Procedure to Nonlinear Structural Analysis
		1. Discussion-Convergence behavior of Newton-Raphson method
		1. Tangent stiffness matrix for truss elements
		1. Tangent stiffness matrix for beam elements (in the local coordinate system)
	1. Types of Newton-Raphson Iterative Methods
	1. Incremental – Iterative Procedure for Nonlinear problems-Load control and displacement control – proportional loading.
		1. Example 2.3: Solution of nonlinear structure
	1. Interlude 1: Some necessary introduction – The BASIC system of a beam and the basic displacements/rotations.
	1. Interlude 2: Force-based (flexibility-based) beam elements 
		1. Weak form of Compatibility Equations – Principle of Virtual Forces 
		1. Force interpolation – Force-based elements
		1. Nonlinear Force-Based Elements
	1. Accounting for Geometric Nonlinearities in Structural Analysis – The corotational formulation

1. Finite Elements for Small-Strain Inelastic Solid Mechancis
	1. Introduction – Basic Definitions
	1. Governing equations in solid mechanics – The conservation (balance) laws
		1. Conservation of mass for small-strain problems 
		1. Conservation of linear momentum for small-strain problems
		1. Strong form of Conservation of Linear Momentum (equation of motion) 
		1. Conservation of angular momentum 
		1. Conservation of energy (1st law of thermodynamics)
	1. Weak form for 3D equations of motion 
	1. Piecewise Finite Element Approximation – Assembly Equations 
		1. Partition to unrestrained and restrained degrees of freedom 
		1. Accounting for the effect of viscous damping forces 
	1. Solution for General, Time-dependent solid mechanics problems
		1. Newmark Method for Step-by-step solution of equations of motion
		1. Explicit Central Difference Method for equations of motion
		1. Example 3.1: Explicit Central Difference Update 
		1. Example 3.2: Use of Explicit Analysis for Static Loading

1. Elastoplasticity and Numerical Implementation
	1. Introduction – Basic Definitions
	1. The yield condition for multiaxial elastoplasticity – Yield criteria
	1. The flow rule for elastoplasticity – Plastic Potential Function – Associative and Non-Associative flow rules 
		1. Example 4.1: Isochoric Plastic flow for von Mises criterion
		1. Example 4.2: Effective plastic strain and plastic multiplier
		1. Example 4.3: Plastic flow for uniaxial stress
	1. Perfect Plasticity and Hardening
	1. The consistency condition – Elastoplastic Material Tangent Stiffness Matrix
		1. Example 4.4: Calculations for non-associative flow rule in elastoplastic material
	1. Numerical Stress Update procedure 
		1. The Radial Return Algorithm for J2 plasticity
		1. Generalized Cutting Plane Algorithm 
		1. Algorithmic Tangent Moduli 
		1. Example 4.5: Calculations for von Mises model with mixed linear hardening.

1. Large Deformation Solid Mechanics
	1. Introduction – Reference/Current Configuration – The Motion Mapping
	1. Material and Spatial Descriptions – The material time derivative
		1. Example 5.1: Description using material and spatial coordinates 
	1. The deformation gradient of the motion and the polar decomposition theorem 
	1. Deformation Measures in the Current and in the Reference Configuration
		1. Example 5.2: Large deformation kinematics
	1. Stress Measures in the Current and in the Reference Configuration
	1. The Need for Objective Stress Rates
	1. Governing Equations with Respect to Reference Configuration – Total Lagrangian Formulation
	1. Governing Equations with Respect to CURRENT Configuration
	1. A “trick” to use the current configuration without convective terms: The updated Lagrangian formulation. 
	1. Weak form for total Lagrangian formulation: Principle of Virtual Work 
	1. Weak form for Updated Lagrangian formulation: Principle of Virtual Power 
	
1. Finite Element Solution For Large-Deformation Problems
	1. Introduction
	1. Finite Element Equations for Total Lagrangian Formulation
	1. Finite Element Equations for Updated Lagrangian Formulation
	1. Concluding Remarks on Updated Lagrangian formulation

1. Further Iterative Solution Strategies
	1. Introduction
	1. Alternative Convergence Criteria for Iterative Solutions
	1. Alternative Iterative Strategies – Quasi-Newton Methods
		1. Quasi-Newton method using rank-1 update – The Broyden method
		1. Quasi-Newton method using rank-2 update – The BFGS method
	1. Increasing the efficiency and robustness of iterative procedures 
		1. Subincrementation
		1. Using Line-search in iterative procedures 
		1. Further Note: efficient use of Newton-Raphson iteration
		
1. Vector-Tensor Calculus
	1. Introduction – Scalar and Tensor quantities - Vectors 
	1. Definition of Stress tensor – Second-order tensors
	1. Coordinate Transformation Rules for Vectors
	1. Summation Convention
		1. Example 8.1: Summation Convention
	1. Coordinate transformation law for 2nd order tensors
	1. Tensor Invariants
	1. Volumetric and deviatoric parts of stress and strain
	1. Principal Values and Principal Directions of a Tensor 
	1. The principal stress-space representation
	1. $$ \pi $$-plane and Haigh-Westergaard coordinates
	1. Derivatives of Invariants, deviatoric invariants and Haigh-Westergaard coordinates with stress components
		1. Example 8.2: Calculations with three-dimensional tensors
	1. Principal Values and Principal Directions of a Tensor

1. Standalone Program for Nonlinear Analysis
	1. Program Description
	1. Program Source Code 
	1. Sample Input File
	
---
Hope this information may be useful…

***Note*** - If any example is not working or any links are not working, please comment I will update with appropriate ones…

Last Updated: 2020-03-10	