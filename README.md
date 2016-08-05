AI for Society Good
=======

This purpose of this repo is to explain how can the current state-of-the-art machine learning/AI algorithms help the society.

A Little Background
------------

The hottest technology in the field of machine learning is deep learning. 
Even though it is not straightforward to explain deep learning to people outside the field, the impact of it is obvious in both research and industry. 
Current performance of these algorihms excel even human performance on several hard AI tasks such as image recognition, document classification, etc.
<br>
<br>
With the help of large GPU computing resources (deep learning takes advantage of GPUs), top-level research and lots of data deep learning algorihms are becoming a standard for many natural language processing, audio recognition and computer vision tasks.

So What?
--------------

Obviously, and arguably thankfully, people communicate in the forms mentioned above, i.e., digital text, digital images and digital audio.
Given the opportunity of open data from companies, institutions and organizations, as an AI researcher, it is my duty to explain what can be done with our current knowledge for the good of the society.

Concept
---------

The concept is to provide a toolbox for enabling the application of state-of-the-art machine learning algorithms to the open datasets in Finland.
The ultimate goal is to create a machine learning platform/toolbox that can be used to mine all kinds of open datasets in Finland.

These datasets can be:
* Suomi24 (*https://korp.csc.fi/download/Suomi24/*)
* Wikipedia hit counts (*http://dumps.wikimedia.org/other/pagecounts-raw/*)
* Twitter (*https://twitter.com/*)
* Facebook (*https://www.facebook.com/*)
* Statistics Finland (*http://tilastokeskus.fi/index_en.html*)
* THL (*http://www.thl.fi/ttr/gen/rpt/tilastot.html*)
* Instagram (*https://instagram.com/*) (not completely open dataset though)
* ImageNet (*http://www.image-net.org/*)

Couple of examples:

#### Public Attention Analysis

Simple trend analysis and anomaly detection out of Wikipedia hit counts, Suomi24 etc. A simple example for hit counts of wikipedia pages is below.  
<br>
<a href="url"><img src="https://github.com/ogencoglu/OpenFinland/blob/master/images/wikitrends.png" align="left" width="800" ></a>

<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>

#### Disease Surveillance

I have already proved this to be working but unfortunately, the results can not be published before the scientific publication which is under review. Contact me for details.

#### Sentiment Analysis

A sentiment analyzer out of the IMDB movie reviews is already implemented in the "source" directory. Machine translation and language modeling can be implemented to apply it for Finnish language.

#### Detection of Trolls from Discussion Forums

Many forums suffer the presence of trolls. Troll activities include posting wrong or irrelevant information, insulting, posting irrelevant images (especially pornography). Automatic detection of such activities rely both on text analysis and image analysis algorithms. Here is a discussion about bugs on Suomi24:

http://keskustelu.suomi24.fi/t/5173609/lutikka-vieraana

One of the users posts the following post (which has an url to an image) on the forum:
<br>
<a href="url"><img src="https://github.com/ogencoglu/OpenFinland/blob/master/images/bug_post.PNG" align="left" width="800" ></a>

<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>

State-of-the-art image recognition algorithms are able to recognize objects from images thus serving as an automatic moderator for the forums. Here is the image and the 5 most probable outputs created by AI:
<br>
<a href="url"><img src="https://github.com/ogencoglu/OpenFinland/blob/master/images/dl4.png" align="left" width="800" ></a>

<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>

The user was posting a relevant image apparently. The source code is available for the image recognition part.

#### Monitoring the Effect of Economic Trends on Public Opinion
#### Analysis of Political Stands
#### Analysis of Consumer Behavior
#### Detection of Suicide Tendency
#### Analyzing the Most Influential Users in a Discussion Forum
#### Detection of Bots in Discussion Forums
#### Detection of Similar Topics in Discussion Forums
etc.



## Contact
oguzhan.gencoglu@tut.fi
