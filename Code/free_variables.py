######################################################################################
#                             Free Variables Visitor                                 #
######################################################################################
 

## import dependencies
from model import *
from visitor import VisitUnaryExpression


##
class FreeVariables(VisitUnaryExpression):

    """
    The FreeVariables can run visitor operations over any set of elements without
    figuring out their concrete classes. The accept operation directs a call to
    the appropriate operation in the visitor object.
    """

    def __init__(self):
        ## initiate instances
        self.freeVars = set()

    def visitVariable(self, var:Variable)->set:
        """visitor visiting variable"""
        return {var.name}

    def visitEqual(self, phi:Equal)->set:
        """visitor visiting Equality"""
        rriLeft = phi.leftExpression.accept(self)
        rriRight = phi.rightExpression.accept(self)
        return rriRight.union(rriLeft)

    def visitAnd(self, phi:And)->set:
        """visitor visiting Conjunction"""
        rriLeft = phi.leftExpression.accept(self)
        rriRight = phi.rightExpression.accept(self)
        if rriRight:
            return rriLeft.union(rriRight)
        return rriLeft

    def visitOr(self, phi:Or)->set:
        """visitor visiting Disjunction"""
        rriLeft = phi.leftExpression.accept(self)
        rriRight = phi.rightExpression.accept(self)
        if rriRight:
            return rriLeft.union(rriRight)
        return rriLeft

    def visitNot(self, phi:Not)->Variable:
        """visitor visiting Negation"""
        try:
            var = phi.expression.variable.accept(self)
        except Exception as e:
            try:
                var = phi.expression.name.accept(self)
            except Exception as e:
                var = phi.expression.title.accept(self)
        return var

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
    


## Proposal testing: we will test our proposal on some simple queries

if __name__ == "__main__":

    ## create a Free Variables Visitor
    FV = FreeVariables()

    ## create variables
    x = Variable('x')
    y = Variable('y')

    ## simple queries to set our proposal
    query_0 = Not(Actor(x))
    query_1 = Or(Not(Actor(x)), Exists(y, And(Film(y), Acts(x, y))))
    query_2 = Forall(x, Or(Not(Director(x)), Exists(y, And(Film(y), Directs(x, y)))))
    query_3 = And(Actor(x), Acts(x, y))
    
    queries = [query_0, query_1, query_2, query_3]
    
    ## test queries
    for e, query in enumerate(queries):
        print(f"\nQuery {e}: {query}")
        ## get free variables
        free_vars = query.accept(FV)
        ##
        print(f"\t\tFree variables: {free_vars}")