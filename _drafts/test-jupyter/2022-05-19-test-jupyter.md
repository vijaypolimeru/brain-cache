---
layout: post
title: "Write Jekyll Post Using Jupyter"
author: "Vijay Kumar Polimeru"
tags: Research
permalink: /jupyter-jekyll/
comments: true
more_updates_card: true
---


```python
%%cmd
where python
```

    Microsoft Windows [Version 10.0.19042.1645]
    (c) Microsoft Corporation. All rights reserved.
    
    C:\Users\vkumarpo\Python-Notebooks>where python
    C:\ProgramData\Anaconda3\python.exe
    C:\Users\vkumarpo\AppData\Local\Microsoft\WindowsApps\python.exe
    
    C:\Users\vkumarpo\Python-Notebooks>

# Trying to convert this into a Jekyll Post


```python
import numpy as np
A = np.array(([1,3,3],[1,4,3],[1,3,4]))
A_inv = np.linalg.inv(A)
A_inv
```




    array([[ 7., -3., -3.],
           [-1.,  1.,  0.],
           [-1.,  0.,  1.]])




```python
# importing matplotlib module
from matplotlib import pyplot as plt

# x-axis values
x = [5, 2, 9, 4, 7]

# Y-axis values
y = [10, 5, 8, 4, 2]

# Function to plot
plt.plot(x, y)

# function to show the plot
plt.show()

```


    
![png](/images/jpost_files/jpost_4_0.png)
![mountains-190055.jpg](/images/mountains-190055.jpg)
    

