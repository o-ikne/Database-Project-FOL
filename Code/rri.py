########################################################################################################
#                                Range Restriction Interpretation                                      #
########################################################################################################


## import dependencies
from model import *
from visitor import VisitUnaryExpression
from free_variables import FreeVariables


##
class RangeRestrictedInterpretation(VisitUnaryExpression):

    """
    The RangeRestrictedInterpretation can run visitor operations over any set of elements without
    figuring out their concrete classes. The accept operation directs a call to
    the appropriate operation in the visitor object.
    """

    def __init__(self):
        ## initiate instances
        self.freeVars = set()

    def visitVariable(self, var:Variable)->set:
        """Visitor visiting variable"""
        return set([var.name])

    def visitEqual(self, phi:Equal)->set:
        """visitor visiting Equality"""
        l = phi.leftExpression.accept(self)
        r = phi.rightExpression.accept(self)
        return l.union(r)

    def visitAnd(self, phi:And):
        """visitor visiting Conjunction"""
        rriLeft = phi.leftExpression.accept(self)
        rriRight = phi.rightExpression.accept(self)
        return rriRight.intersection(rriLeft)

    def visitOr(self, phi:Or)->set:
        """visitor visiting Disjunction"""
        rriLeft = phi.leftExpression.accept(self)
        rriRight = phi.rightExpression.accept(self)
        return rriLeft.union(rriRight)

    def visitNot(self, phi:Not)->set:
        """visitor visiting Negation"""
        return set()

    def visitExists(self, phi:Exists)->set:
        """visitor visiting Exists"""
        rri = phi.predicate.accept(self)
        var = phi.variable.name
        try:
            if var in rri and len(rri) == 1:
                return set()
            return rri.remove(var)
        
        except Exception as e:
            raise ValueError("NOT RRI: Exists")

    def visitForall(self, phi:Forall)->set:
        """visitor visiting Forall"""
        rri = phi.predicate.accept(self)
        var = phi.variable.name
        try:
            if var in rri and len(rri) == 1:
                return set()
            return rri.remove(var)
        
        except Exception as e:
            raise ValueError("NOT RRI: Forall")

    def visitActor(self, actor:Actor)->Variable:
        """visitor visiting actors"""
        variable = actor.name.accept(self)
        return variable

    def visitArtist(self, artist:Artist)->Variable:
        """visitor visiting artists"""
        variable = artist.name.accept(self)
        return variable

    def visitDirector(self, director:Director)->Variable:
        """visitor visiting film directors"""
        variable = director.name.accept(self)
        return variable

    def visitFilm(self, film:Film)->Variable:
        """visitor visiting movies"""
        variable = film.title.accept(self)
        return variable

    def visitActs(self, acts:Acts)->set:
        """visitor visiting acts"""
        variable_1 = acts.actor.accept(self)
        variable_2 = acts.movie.accept(self)
        return variable_1.union(variable_2)

    def visitDirects(self, directs:Directs)->set:
        """visitor visiting directs"""
        variable_1  = directs.director.accept(self)
        variable_2 = directs.movie.accept(self)
        return variable_1.union(variable_2)
  



def is_range_restricted(query):
    """check whether a query is range-restricted or not"""
    ## get free variables & range-restricted of the query
    FV = FreeVariables()
    RRI = RangeRestrictedInterpretation()
    fv  = query.accept(FV)
    rri = query.accept(RRI)
    return fv == rri


## Proposal testing: we will test our proposal on some simple queries

if __name__ == "__main__":

    ## create a range restriction interpretation visitor
    RRI = RangeRestrictedInterpretation()

    ## create variables
    x = Variable('x')
    y = Variable('y')
    z = Variable('z')

    ## create some queries
    query_0 = And(Artist(x), Actor(x))
    query_1 = Not(Exists(x, And(Actor(x), Not(Exists(y, And(Film(y), Acts(x, y)))))))
    query_2 = Forall(x, Or(Not(Artist(x)), Or(And(Artist(x), Actor(x)), And(Artist(x), Director(x)))))
    query_3 = Or(Actor(x), Or(Film(y), Acts(x, y)))
    ## This request will fail because of Forall
    query_4 = Forall(x, Or(Not(Actor(x)), Exists(y, And(Film(y), Acts(x, y)))))

    queries = [query_0, query_1, query_2, query_3, query_4]
    ## for each query
    for e, query in enumerate(queries[:3]):
        print(f'\nQuery {e}: {query}')

        ## get rri of the query
        rri = query.accept(RRI)
        print(f'\t\t-rri: {rri}')


    ## check if some queries are range-restricted
    print("\n\n======== Range Restricted =========")
    queries = [Not(Actor(x)), Actor(x), query_1]
    for e, query in enumerate(queries):
        print(f'\nQuery {e}: {query}')

        print(f"\t-range-restricted: {is_range_restricted(query)}")