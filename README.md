# Pharmacy-sort
Uses data from Oriel to Rank pharmacies acrosss the UK based off pay and location filters. Used by friends at University of Nottingham to select their placements and was very succesful!


## Motivation

A friend informed me that she had only 6 days left to decide her post-grad pharmacy placement through the website oriel. Unfortunately, the website did not have any filters and you would have to scroll down a list of pharmacies 3000 rows long. Furthermre, information was only shown on the pharmacy when it was clicked on so each indivdual pharmacy had to be clicked. The number of pharmacies they chose could be as long as the wanted, most people seemed to choose around 50. So as you can imagine this is a very long task which they were given 3 months to do, but as most universit students do she procrastinated and so my aim was to help het get it done much faster. 

## Goal
My goal was to generate the list for her automatically based off her preferences. The two things that concerned her were pay and distance. 


## Approach

First I had to decide which mattered more and how much more between pay or distance. I decided to use a weighted scoreing system which the user decides. 
a salary weight of 60% would mean distance has a weight of 40% which means salary matters more by 20%. Once that is decided A way to calculate them would be needed. Calculators.py does exactly this. 

# Calculators.py


