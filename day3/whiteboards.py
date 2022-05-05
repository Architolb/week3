# The question asks the following: Write a function that takes an integer flight_length
#  (in minutes) and a list of integers movie_lengths (in minutes) and returns a boolean
#  indicating whether there are two numbers in movie_lengths whose sum equals flight_length.
movie_lengths1=[20, 30, 110, 40, 50] #true
movie_lengths2=[80, 110, 40]  #false
flight_length=160


def canIWatch2Movies(flight, movies):
    for i, length in enumerate(movies):
        diff = flight - length
        other_movie_lengths = list(filter(lambda x: movies.index(x) != i, movies))
        if diff in other_movie_lengths: 
            return True
    return False
    
print(canIWatch2Movies(flight_length,movie_lengths2))

def twoMovies(flight, movies):
    # make empty set
    some_empty_list = set()
    # loop through movies
    for length in movies:
    # if length of flight - movie length is in set, return true
        if flight - length in some_empty_list:
            return True
        some_empty_list.add(length)
    return False



    # Electric Company
# Create a function that given a list which represents street lights given as a parameter(l_street), 
# determine if an outage has occurred. A street with a total number of "F" greater than or equal to 2 
# returns "Outage", anything below returns "Power"
l_street = ['T', 'F', 'F', 'F']
# Example Output: "Outage"










# Given a string of space separated integers - "32 27 83 25 5 -5 0 32"
# Return the highest and lowest as a space separated string "-5 83"
# bonus challenge: do so for strings of numbers with random extra whitespace

string1 = "32 27 83 25 5 -5 0 32"
bonus = "     82  1 0  -5 32  7  14  22   "