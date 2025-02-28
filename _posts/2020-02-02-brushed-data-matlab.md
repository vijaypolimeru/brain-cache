---
layout: post
title: "Simple way to plot, interactively brush some data and automatically re-plot or to save the brushed/unbrushed data in a variable in Matlab"
author: "Vijay Kumar Polimeru"
tags: 
  - Matlab
permalink: /interactive-plotting-matlab/
comments: true
more_updates_card: true
---

Brushing or removing some noisy signal is often very much essential in signal processing, to uncover some valuable information from the total signal received. 
However, this brushing is often not an easy process when we have too many signals plotted in a single figure window. <!--more-->To easily identify and remove the noisy
signal from each plot and to save the indices of removed signal requires good software tools. 
Matlab offers some easy to tools such as `uicontrol`, `assignin` etc to interactively brush the data and get the indices of brushed data, using which we can re-plot the
total signal without noisy signal. 

Here in this post, we will plot three randomly generated signals, interactivley brush some signal and re-plot the brushed signal also save the indices
of brushed signal. The base code published [here]() for single singal has been taken and improved further to make it work for multiple signal

```matlab
function testbrushcode()

% Create signal
t = randn(1, 100);
x = sin(t);
y = tan(2.*t);
z = cos(2*t);

% Create figure with points (Ref. Figure. 1)
fig = figure();
m{1} = scatter(t, x);
hold on
m{2} = scatter(t, y);
m{3} = scatter(t, z);
hold off
brush on;
uicontrol('Parent', fig, ...
    'Style', 'pushbutton',...
    'String', 'Get selected points index',...
    'Position', [5, 5, 200, 30],...
    'Units', 'pixels',...
    'Callback', {@mycallback, m} ...
    );

% 1. (Ref. Figure. 2)
% 2. Select the data which you are intersted in or Brush the unwanted signal 
%    and slect the remaining signal in the figure window
% 3. Then press the "selectedPoints" button and close the figure window 

waitfor(fig)

% Once the figure window is closed, we are saving the selected data points
% to each each in index_vec, which will used to re-plot the brushed data in
% future

index_vec{1} = find(selectedPoints1 == 1);
index_vec{2} = find(selectedPoints2 == 1);
index_vec{3} = find(selectedPoints3 == 1);

save('index_vec.mat','index_vec')

% Ref. Figure. 3

fig = figure();
scatter(t(index_vec{1}), x(index_vec{1}));
hold on
scatter(t(index_vec{2}), y(index_vec{2}));
scatter(t(index_vec{3}), z(index_vec{3}));
hold off


end

function mycallback(~, ~, mylineseries)

% assingin function assigns the indices of selectedpoints to a variable
% called selectedPoints1 or 2 or 3 in the caller workspace, which is
% workspace of the function from which this function is called

assignin('caller', 'selectedPoints1', get(mylineseries{1},'BrushData'))
assignin('caller', 'selectedPoints2', get(mylineseries{2},'BrushData'))
assignin('caller', 'selectedPoints3', get(mylineseries{3},'BrushData'))

end
```

Figure.1
![image-center]({{ '/images/brush-data-1.jpg' | absolute_url }}){: .align-center}

Figure.2
![image-center]({{ '/images/brush-data-2.jpg' | absolute_url }}){: .align-center}

Figure.3
![image-center]({{ '/images/brush-data-3.jpg' | absolute_url }}){: .align-center}