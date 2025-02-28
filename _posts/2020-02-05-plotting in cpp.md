---
layout: post
title: "Four Simple tools to draw beautiful plots in C++"
author: "Vijay Kumar Polimeru"
tags: Research
permalink: /plotting-in-cpp/
comments: true
sticky: true
more_updates_card: true
---
For people who are migrating from Matlab or Python (or some other well-developed scientific programming tools) to C++ (A primitive programming language),
plotting is a little bit tricky job, as there is no default plotting library available in any C++ IDE (not even in Visual Studio 2019). <!--more--> Its very strage but true, 
I still don't understand, why data visualistaion is not in the bucket list of C++ developers. However, there are many libraries (or third party tools)
 available online for making plotting possible in C++. Many of them are open source 

Following are some of the powerfull open source tools (except MATLAB), which I have tested, 

1.  [Koolplot][1] - A simple, elegant and easy to use tool for 2D plotting and may not be enough for your requirement. 
An example excerpt taken from the [website][2] is shown below, you can find more examples and the process of linking it with C++ IDE [here][1].

	```cpp
	#include "koolplot.h"
	int main()
	{
	   plotdata x(-6.0, 6.0);    
	   plotdata y = sin(x) + x/5;
	   plot(x, y);
	   return 0;
	}
	```
2. [GNUPlot][3] - It is a very robust opensource tool for plotting, with the help of an interface called [Gnuplot-iostream interface][4], 
calling the gnuplot commands from C++ is very easy process. If somebody is already experienced plotting in gnuplot and have to use C++ 
for their programming then this interface is very usefull. or if you want to create your own interface, this the information provided in [here][5] will 
be very useful. The process of linking this interface is veryeasy, just install gnuplot in your system and then link the include 
directory and lib directory of gnuplot to C++ IDE, and then you are ready to go. Examples on how to use Gnuplot from C++ using gnuplot-iostream 
interface are given [here][4], an excerpt of sample example is posted below.

	```cpp
	#include <vector>
	#include <cmath>
	#include <boost/tuple/tuple.hpp>
	#include "gnuplot-iostream.h"
	int main() {
		Gnuplot gp;
		std::vector<boost::tuple<double, double, double, double> > pts_A;
		std::vector<double> pts_B_x;
		std::vector<double> pts_B_y;
		std::vector<double> pts_B_dx;
		std::vector<double> pts_B_dy;
		for(double alpha=0; alpha<1; alpha+=1.0/24.0) {
			double theta = alpha*2.0*3.14159;
			pts_A.push_back(boost::make_tuple(
				 cos(theta),
				 sin(theta),
				-cos(theta)*0.1,
				-sin(theta)*0.1
			));

			pts_B_x .push_back( cos(theta)*0.8);
			pts_B_y .push_back( sin(theta)*0.8);
			pts_B_dx.push_back( sin(theta)*0.1);
			pts_B_dy.push_back(-cos(theta)*0.1);
		}
		gp << "set xrange [-2:2]\nset yrange [-2:2]\n";
		gp << "plot '-' with vectors title 'pts_A', '-' with vectors title 'pts_B'\n";
		gp.send1d(pts_A);
		gp.send1d(boost::make_tuple(pts_B_x, pts_B_y, pts_B_dx, pts_B_dy));
	} // very simple tool right???
	```
3. [MATLAB][6] (Yes, I am not kidding MATLAB can be called from C++) - 
If you are familiar with MATLAB, you can get the same functionality in C++ by calling, functions/toolboxes from MATLAB and vice versa. 
Since MATLAB is commercial software, first you have to acquire license (this is very costly). If you have an 
installed MATLAB software, then use the `engine.h` file and link the necessary MATLAB library files to C++ IDE, 
then the process is outright simple. A detailed step-by-step process of linking matlab to visual studio c++ is provided [here][7] and [here][8]. 
An example code is given here, an excerpt of an example is given below

	```cpp
	#include <stdlib.h>
	#include <stdio.h>
	#include <string.h>
	#include "engine.h"
	#define  BUFSIZE 256

	int main()

	{
		Engine *ep;
		mxArray *T = NULL, *result = NULL;
		char buffer[BUFSIZE+1];
		double time[10] = { 0.0, 1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0 };
		if (!(ep = engOpen(""))) {
			fprintf(stderr, "\nCan't start MATLAB engine\n");
			return EXIT_FAILURE;
		}
		T = mxCreateDoubleMatrix(1, 10, mxREAL);
		memcpy((void *)mxGetPr(T), (void *)time, sizeof(time));
		engPutVariable(ep, "T", T);
		engEvalString(ep, "D = .5.*(-9.8).*T.^2;");
		engEvalString(ep, "plot(T,D);");
		engEvalString(ep, "title('Position vs. Time for a falling object');");
		engEvalString(ep, "xlabel('Time (seconds)');");
		engEvalString(ep, "ylabel('Position (meters)');");

		printf("Hit return to continue\n\n");
		fgetc(stdin);

		printf("Done for Part I.\n");
		mxDestroyArray(T);
		engEvalString(ep, "close;");

		buffer[BUFSIZE] = '\0';
		engOutputBuffer(ep, buffer, BUFSIZE);
		while (result == NULL) {
			char str[BUFSIZE+1];
			printf("Enter a MATLAB command to evaluate.  This command should\n");
			printf("create a variable X.  This program will then determine\n");
			printf("what kind of variable you created.\n");
			printf("For example: X = 1:5\n");
			printf(">> ");

			fgets(str, BUFSIZE, stdin);
			engEvalString(ep, str);
			printf("%s", buffer);
			printf("\nRetrieving X...\n");
			if ((result = engGetVariable(ep,"X")) == NULL)
			  printf("Oops! You didn't create a variable X.\n\n");
			else {
			printf("X is class %s\t\n", mxGetClassName(result));
			}
		}
		printf("Done!\n");
		mxDestroyArray(result);
		engClose(ep);
		
		return EXIT_SUCCESS;
	}
	```
4. [Python][11] - For people who are familiar with matplotlib tool in Python, there is a very elegant interface available to call `matplotlib` of python from C++. a simple example may look like this ([source][12]) and 
the `matlabplotcpp.h` is available [here][13].

	```cpp
	#include "matplotlibcpp.h"
	namespace plt = matplotlibcpp;
	int main() {
		plt::plot({1,3,2,4});
		plt::show();
	}
	```

Hope this information may be useful...

**Note** - If any information is not cited appropriately or any links are not working, please comment I will update with appropriate ones…


  [1]: http://www.codecutter.net/tools/koolplot/byExample.html
  [2]: http://www.codecutter.net/tools/koolplot/koolplot_doc/index.html
  [3]: http://www.gnuplot.info/
  [4]: http://stahlke.org/dan/gnuplot-iostream/
  [5]: https://www.youtube.com/watch?v=UcYankkrIpw
  [6]: https://in.mathworks.com/help/matlab/cpp-mex-file-applications.html
  [7]: https://stackoverflow.com/questions/16258815/call-a-matlab-code-from-visual-studio-c
  [8]: https://www.youtube.com/watch?v=5pz1fpDE0nw
  [9]: https://i.stack.imgur.com/IQl1D.png
  [10]: https://www.researchgate.net/profile/Hazim_Tahir/post/How_can_I_convert_MATLAB_code_to_c_c_code/attachment/59d64455c49f478072eacce0/AS%3A273746584113162%401442277679173/download/cmex.pdf
  [11]: https://www.python.org/
  [12]: https://github.com/lava/matplotlib-cpp/blob/master/README.md
  [13]: https://github.com/lava/matplotlib-cpp
