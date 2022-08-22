# Pharmacy-sort
Uses data from Oriel to Rank pharmacies acrosss the UK based off pay and location filters. Used by friends at University of Nottingham to select their placements and was very succesful!


## Motivation

A friend informed me that she had only 6 days left to decide her post-grad pharmacy placement through the website oriel. Unfortunately, the website did not have any filters and you would have to scroll down a list of pharmacies 3000 rows long. Furthermre, information was only shown on the pharmacy when it was clicked on so each indivdual pharmacy had to be clicked. The number of pharmacies they chose could be as long as the wanted, most people seemed to choose around 50. So as you can imagine this is a very long task which they were given 3 months to do, but as most universit students do she procrastinated and so my aim was to help het get it done much faster. 

## Goal

My goal was to generate the list for her automatically based off her preferences. The two things that concerned her were pay and distance. 


## The Data 

The postcode is stored within the pharmacy title. So postcode had to be extracted from the name. Using get_postcode in choice.py.
The salary was stored in salary column

![image](https://user-images.githubusercontent.com/79328765/186035049-d8c554a3-bbc0-4cd4-8fef-0bf59e14dca1.png)

![image](https://user-images.githubusercontent.com/79328765/186035112-be666582-5e16-4337-9432-055481fbadad.png)




## Approach

First I had to decide which mattered more and how much more between pay or distance. I decided to use a weighted scoreing system which the user decides. 
a salary weight of 60% would mean distance has a weight of 40% which means salary matters more by 20%. Once that is decided A way to calculate them would be needed. Calculators.py does exactly this. 

## Calculators.py

salary_score(salary, max, min) -> returns a score out of 100 bases off the users minumun accepted salary and the maximum available. If the salary is less than the minimum 0 is returned

distance_score(goal_location, start_location, max_distance) -> returns a score based of max distance. Uses google api to take in two post codes and calculates distance.

distance_score_to_distance(score, max_distance) -> if distance score is greater than 0 the distance of the pharmacy is returned. 

def total_score (salary_score, distance_score, salary_weight, distance_weight) -> calculates weighted mean of the job taking into accoung distance and salary

## Map.py

Uses google maps API to calculated distance between two postcodes in miles. Need google API key.

## Choice.py 

main file that generates list as new sheet

## Outcome

The program was succeful and was very popular amongst her peers. It cut the time of selecting pharmacies down from month to just a few minutes. Head of deparment was also interested in the code. 

## Future improvements 

May work on improving later 
Pandas could have been used to read data files instead.
Concurrency programming could have been used as it take arouf 10min to generate list 

