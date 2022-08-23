from map import calculate_distance



"""returns the score out of 100 of the salary of job
*salary - salary to be evaluated
*max - maximum salary possible
*min - minimum salary possible"""
def salary_score(salary, max, min):
    
    if salary >= min:
        domain = max - min
        one_percent = domain / 100

        base_salary_rating = min / one_percent
        current_salary_rating = salary / one_percent 

        perecentage_increase = current_salary_rating - base_salary_rating

        score = 1 + perecentage_increase

        return score 
    else:
        return 0

""" returns the score out of 100 of the destination of a job
    *goal_location - address of job to be evaluated
    *start_location - address of starting location
    *max_distance - maximum distance willing to travel
"""
def distance_score(goal_location, start_location, max_distance):

    distance_to_destination = calculate_distance(goal_location, start_location)
    
    if distance_to_destination <= max_distance:
        
        one_percent = max_distance / 100
        start_location_rating = 100
        goal_location_rating = distance_to_destination / one_percent
        score = start_location_rating - goal_location_rating + 1 
        return score 
    else:
        return 0

def distance_score_to_distance(score, max_distance):
    
    if score != 0:
        one_percent = max_distance / 100 

        start_location_rating = 100
        goal_location_rating = start_location_rating - score

        distance_to_destination = goal_location_rating * one_percent  

        return distance_to_destination
    else:
        return "no valid postcode"

"""calculates weighted mean of the job taking into accoung distance and salary
*salary_score - score of job salary
*distance_score - score of distance salary
*salary_weight - weighting of job salary
*distance_weight - weighting of distance salary"""

def total_score (salary_score, distance_score, salary_weight, distance_weight):

        return (salary_score * salary_weight) + (distance_score * distance_weight)

    
