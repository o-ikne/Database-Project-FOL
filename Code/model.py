###########################################################################
#               Deep Representation of First Order Formulae               #
###########################################################################

## dependencies
from typing import Union
from functools import partial
from data.data import *


## model classes

class UnaryExpression(object):

    """class for unary expressions"""

    def accept(self, visitor):
        """accept visitor"""
        ## create method name "visit + class name"
        method_name = f"visit{self.__class__.__name__}"
        ## create the visit method
        visit = getattr(visitor, method_name)
        return visit(self)


class BinaryExpression(object):

    """class for binary expressions"""

    def accept(self, visitor):
        """accept visitor"""
        ## create method name "visit + class name"
        method_name = f"visit{self.__class__.__name__}"
        ## create the visit method
        visit = getattr(visitor, method_name)
        return visit(self)


class Variable(UnaryExpression):
    """class for variables"""
    def __init__(self, name:str):
        """name: <str>: the name of the variable"""
        self.name = name

    def __eq__(self, other):
        """check if an other variable is equal to this variable
        other: <Variable>: variable to this variable with.
        """
        return self.name == other.name 

    def __repr__(self):
        """represent a variable by its name"""
        return self.name


class Constant(UnaryExpression):
    """Class for constants"""
    def __init__(self, value:Union[str, int, float]):
        """value: <str|int|float>: the value of the constant"""
        self.value = value

    def __eq__(self, other):
        """check if another constant is equal to this constant"""
        return self.value == other.value 

    def __repr__(self):
        """represent a constant by its value"""
        return str(self.value)


class Quantifier(UnaryExpression):
    """Class for quantifiers"""
    def __init__(self, variable:Variable, predicate:UnaryExpression):
        """variable : <Variable>       : the variable of the quantifier
           predicate: <UnaryExpression>: the predicate of the quantifier
        """
        self.variable = variable
        self.predicate = predicate
    

class Forall(Quantifier):
    """Class for Universal quantifier"""
    def __init__(self, variable: Variable, predicate:UnaryExpression):
        super().__init__(variable, predicate)

    def __repr__(self):
        """represent forall predicates"""
        predicate = self.predicate.__repr__()
        return f"∀{self.variable.name}, {predicate}"


class Exists(Quantifier):
    """Class for Existential quantifier"""
    def __init__(self, variable:Variable, predicate:UnaryExpression):
        super().__init__(variable, predicate)

    def __repr__(self):
        """represent exists predicates"""
        predicate = self.predicate.__repr__()
        return f"∃{self.variable.name}, {predicate}"


class UnaryLogicalConnector(UnaryExpression):
    """Class for unary logical connectors"""
    def __init__(self, expression:UnaryExpression):
        """expression: <UnaryExpression>: the expression of the logical connector"""
        self.expression = expression


class Not(UnaryLogicalConnector):
    """Class for Logical Negation"""
    def __init__(self, expression:UnaryExpression):
        super().__init__(expression)

    def __repr__(self):
        """represent negation"""
        return f"¬{self.expression.__repr__()}"


class BinaryLogicalConnector(BinaryExpression):
    """Class for binary logical connectors"""
    def __init__(self, leftExpression:UnaryExpression, rightExpression:UnaryExpression):
        """leftExpression : <unaryExpression>: the left expression"""
        """rightExpression: <unaryExpression>: the right expression"""
        self.leftExpression = leftExpression
        self.rightExpression = rightExpression


class And(BinaryLogicalConnector):
    """Class for Conjunction"""
    def __init__(self, leftExpression, rightExpression):
        super().__init__(leftExpression, rightExpression)

    def __repr__(self):
        """represent conjunction connector"""
        return f"{self.leftExpression.__repr__()} ∧ {self.rightExpression.__repr__()}"


class Or(BinaryLogicalConnector):
    """Class for Disjunction"""
    def __init__(self, leftExpression, rightExpression):
        super().__init__(leftExpression, rightExpression)

    def __repr__(self):
        """represent disjunction connector"""
        return f"{self.leftExpression.__repr__()} ∨ {self.rightExpression.__repr__()}"


class Equal(BinaryLogicalConnector):
    """class for Equal connector"""
    def __init__(self, leftExpression, rightExpression):
        super().__init__(leftExpression, rightExpression)

    def __repr__(self):
        """represent equal connector"""
        return f"{self.leftExpression.__repr__()} = {self.rightExpression.__repr__()}"

    
class Actor(UnaryExpression):
    """class for actors"""
    def __init__(self, name:str):
        """name: <str>: the name of the actor"""
        self.name = name

    def __repr__(self):
        """represent an actor by his name"""
        return f"actor({self.name})"


class Artist(UnaryExpression):
    """class for artists"""
    def __init__(self, name:str):
        """name: <str>: the name of the artist"""
        self.name = name

    def __repr__(self):
        """represent an artist by his name"""
        return f"artist({self.name})"


class Director(UnaryExpression):
    """class for directors"""
    def __init__(self, name:str):
        """name: <str>: the name of the director"""
        self.name = name

    def __repr__(self):
        """represent an director by his name"""
        return f"director({self.name})"


class Film(UnaryExpression):
    """class for movies"""
    def __init__(self, title:str):
        """title: <str>: the title of the film"""
        self.title = title

    def __repr__(self):
        """represent an actor by its title"""
        return f"film({self.title})"


class Acts(BinaryExpression):
    """class for acts"""
    def __init__(self, actor:Actor, movie:Film):
        """
        actor: <Actor>: the actor that acts.
        movie: <Film> : the film where the actor acts.
        """
        self.actor = actor
        self.movie = movie

    def __repr__(self):
        """represent an acts by its actor and movie"""
        return f"acts({self.actor}, {self.movie})"


class Directs(BinaryExpression):
    """class for directs"""
    def __init__(self, director:Director, movie:Film):
        """
        director: <Director>: the director that directs the movie.
        movie   : <Film>    : the movie directed by the director.
        """
        self.director = director
        self.movie = movie

    def __repr__(self):
        """represent a directs by the director & the movie"""
        return f"directs({self.director}, {self.movie})"


def arity(predicate:callable)->int:
    """return the arity of a given predicate"""
    partial_predicate = predicate
    arty = 0
    while True:
        try:
            partial_predicate()
        except TypeError:
            partial_predicate = partial(partial_predicate, '')
            arty += 1
        else:
            return arty



class Model:
    """ 
        Model Representation:
        In Python, we can represent the model as follows:
           - domain : List
           - artist : List
           - actor : List
           - film : List
           - filmDirector : List
           - acts : List of tuples (actor, film)
           - directs : List of tuples (director, film)
    """
    def __init__(self, domain:list):
        """domain :<list>: List of individuals forming the data"""
        self.domain = domain
        ## set of actors
        self.actors = actors
        ## set of artists
        self.artists = artists
        ## set of film directors
        self.directors = film_director
        ## set of movies
        self.films = films
        ## set of acts : tuples (actor, movie) 
        self.acts = acts 
        ## set of directs : tuples (director, movie)
        self.directs = directs

    def actor(self, name:str)->bool:
        """returns True if the given name corresponds to an actor's name, otherwise returns False"""
        return name in self.actors

    def artist(self, name:str)->bool:
        """returns True if the given name corresponds to an artist's name, otherwise returns False"""
        return name in self.artists

    def director(self, name:str)->bool:
        """returns True if the given name corresponds to an film director's name, otherwise returns False"""
        return name in self.directors

    def film(self, title:str)->bool:
        """returns True if the given title corresponds to an movie's title, otherwise returns False"""
        return title in self.films

    def acted(self, actor:str, movie:str)->bool:
        """returns True if the given actor played in the given movie, otherwise returns False"""
        return (actor, movie) in self.acts

    def directed(self, director:str, movie:str)->bool:
        """returns True if the given director directed the given movie, otherwise returns False"""
        return (director, movie) in self.directs
