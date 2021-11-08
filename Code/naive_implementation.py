############################################################################################################
##                  Databases Project: About First Order Logic as a query language                        ##
############################################################################################################


## I- Implementation of models
## ---------------------------
# We are now turning towards implementing simple data models in Python.
#
# A model is devided into several parts:
#   - A domain : the set of individuals forming the data
#   - Relations : sets of tuples of individuals or predicates (characteristic functions of these sets).
#
# There are several ways of implementing these sets:
#   - set data-structures (any sort of balanced trees, hash-maps, etc.)
#   - sequences without repetitions
#   - sequences possibly with repetitions
#   - streams (sequence whose elements are produced lazily on demand).
#
# /!\ But for the moment we will simply use sequences possibly with repetitions.


## Model Representation:
# In Python, we can represent the following model within as follows:
#   - domain : List
#   - artist : List
#   - actor : List
#   - film : List
#   - filmDirector : List
#   - acts : List of tuples (actor, film)
#   - directs : List of tuples (director, film)


## II- Naive implementation of the evaluation of first order formulae
## ------------------------------------------------------------------

## import data for our model
from data.data import *

##  Implement first order quantifiers & some other useful methods

def forall(pred:callable):
    """Universal quantifier"""
    return all([pred(x) for x in domain])

def exists(pred:callable):
    """Existential quantifier"""
    return any([pred(x) for x in domain])

def count(pred:callable):
    """Aggregate function to return the number of elements that verfiy pred"""
    return sum([pred(x) for x in domain])

def actor(x:str):
    """returns True if x is an actor, otherwise False"""
    return x in actors

def artist(x:str):
    """returns True if x is an artist, otherwise False"""
    return x in artists

def film(x:str):
    """returns True if x is a film, otherwise False"""
    return x in films

def director(x:str):
    """returns True if x is a film director, otherwise False"""
    return x in film_director

def acted(actor:str, movie:str):
    """returns True if actor has played in movie, otherwise False"""
    return (actor, movie) in acts

def directed(director:str, movie:str):
    """returns True if director has directed movie, otherwise False"""
    return (director, movie) in directs



## Testing Proposal on some queries

if __name__ == "__main__":

    ## We test our proposal by evaluating the first-order formulas that correspond to the following sentences:
    print("Proposal Testing :")

    # 1. Each artist is either an actor or a film director
    print("\n\t 1. Each artist is either an actor or a film director :", end=' ')
    result_1 = forall(lambda x: not artist(x) or (artist(x) and (actor(x) or director(x))))
    print(result_1)

    # 2. Every actor acts in at least one movie
    print("\n\t 2. Every actor acts in at least one movie :", end=' ')
    result_2 = forall(lambda x: not actor(x) or (actor(x) and exists(lambda y: film(y) and acted(x, y))))
    print(result_2)

    # 3. Every film director directs at least one movie
    print("\n\t 3. Every film director directs at least one movie :", end=' ')
    result_3 = forall(lambda x: not director(x) or (director(x) and exists(lambda y: film(y) and directed(x, y))))
    print(result_3)

    # 4. No actor acts in every movie
    print("\n\t 4. No actor acts in every movie :", end=' ')
    result_4 = not exists(lambda x: actor(x) and forall(lambda y: not film(y) or (film(y) and acted(x, y))))
    print(result_4)

    # 5. For each movie, at least two actors are involved
    print("\n\t 5. For each movie, at least two actors are involved :", end=' ')
    result_5 = forall(lambda x: not film(x) or (film(x) and count(lambda y: actor(y) and acted(y, x)) > 1))
    print(result_5)

    # 6. For every pairs of actors, each of them has played in a movie of the same director (not necessarily the same movie)
    print("\n\t 6. For every pairs of actors, each of them has played in a movie of the same director (not necessarily the same movie) :", end=' ')
    result_6 = forall(lambda x: not actor(x) or (actor(x) and exists(lambda y: actor(y) and y != x and exists(lambda m: film(m) and acted(x, m) and exists(lambda f: film(f) and acted(y, f) and exists(lambda d: director(d) and directed(d, m) and directed(d, f)))))))
    print(result_6)

    # 7. Write a predicate that corresponds to those artists who are both actors and film directors
    print("\n\t 7. Artists who are both actors and film directors :")
    artist_actor_and_director = lambda x: artist(x) and actor(x) and director(x)
    for x in domain:
        if artist_actor_and_director(x):
            print(f"\t\t-{x}")

    # 8. Write a predicate that corresponds to those film director who directed only one film
    print("\n\t 8. Film director who directed only one film :")
    directed_one_film = lambda x: director(x) and count(lambda y: directed(x, y)) == 1
    for x in domain:
        if directed_one_film(x):
            print(f"\t\t-{x}")

    # 9. Write a binary relation which contains the pairs of actors and of film directors so that the actors is acting in each movie directed by the director.
    print("\n\t 9. Pairs of actors and of film directors so that the actors is acting in each movie directed by the director :")
    acted_all_movies = lambda x, y : actor(x) and director(y) and forall(lambda m: (not film(m) or not directed(y, m))  or (film(m) and acted(x, m) and directed(y, m)))
    for x in domain:
        for y in domain:
            if acted_all_movies(x, y):
                print(f"\t\t-{x, y}")

