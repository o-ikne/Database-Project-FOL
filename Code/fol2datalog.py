#######################################################################################
#                   First Order Logic to Datalog Program                              #
#######################################################################################


## import dependencies
from model import *
from free_variables import FreeVariables
from visitor import VisitUnaryExpression


class FOL2Datalog(VisitUnaryExpression):

    """
    The FOL2Datalog can run visitor operations over any set of elements without
    figuring out their concrete classes. The accept operation directs a call to
    the appropriate operation in the visitor object.
    """

    def __init__(self):
        ## initiate instances
        self.predicates = set()

    def visitVariable(self, var:Variable):
        """visitor visiting variable"""
        return var

    def visitEqual(self, phi:Equal):
        """visitor visiting Equality"""
        return phi

    def visitAnd(self, phi:And):
        """visitor visiting Conjunction"""
        #left = phi.leftExpression.accept(self)
        #right = phi.rightExpression.accept(self)
        #self.predicates.add(phi)
        return phi

    def visitOr(self, phi:Or):
        """visitor visiting Disjunction"""
        left = phi.leftExpression.accept(self)
        right = phi.rightExpression.accept(self)
        
        if isinstance(left, set):
            for element in left:
                self.predicates.add(element)
        else:
            self.predicates.add(left)
        if isinstance(right, set):
            for element in right:
                self.predicates.add(element)
        else:
            self.predicates.add(right)
        return self.predicates
        

    def visitNot(self, phi:Not):
        """visitor visiting Negation"""
        return phi#.expression.accept(self)
        

    def visitExists(self, phi:Exists):
        """visitor visiting Exists"""
        return phi.predicate.accept(self)
        

    def visitForall(self, phi:Forall):
        """visitor visiting Forall"""
        return phi.predicate.accept(self)

    def visitActor(self, actor:Actor):
        """visitor visiting actors"""
        return actor

    def visitArtist(self, artist:Artist):
        """visitor visiting artists"""
        return artist

    def visitDirector(self, director:Director):
        """visitor visiting film directors"""
        return director

    def visitFilm(self, film:Film):
        """visitor visiting movies"""
        return film

    def visitActs(self, acts:Acts):
        """visitor visiting acts"""
        return acts

    def visitDirects(self, directs:Directs):
        """visitor visiting directs"""
        return directs

        
## Proposal testing: we will test our proposal on some simple queries !

if __name__ == "__main__":

    ## create a First Order Logic to Datalog transformer
    fol2datalog = FOL2Datalog()

    ## create variables
    x = Variable('x')
    y = Variable('y')

    ## simple queries to set our proposal
    query_0 = Exists(x, And(Actor(x), Artist(x)))
    query_1 = Forall(x, Or(Not(Artist(x)), Or(And(Artist(x), Actor(x)), And(Artist(x), Director(x)))))
    query_2 = Forall(x, Or(Not(Actor(x)), Exists(y, And(Film(y), Acts(x, y)))))
    query_3 = Forall(x, Or(Not(Director(x)), Exists(y, And(Film(y), Directs(x, y)))))
    
    queries = [query_0, query_1, query_2, query_3]
    
    ## test queries
    for e, query in enumerate(queries):
        ## re-initialize predicates
        fol2datalog.__init__()

        print(f"\nQuery {e}: {query}")
        ## get its predicates
        predicates = query.accept(fol2datalog)
        
        ## create the corresponding datalog
        print("\tsub-predicates:")
        ## if there are multiple predicates
        if isinstance(predicates, set):
            for e, predicate in enumerate(predicates):
                ## get predicates free variables
                freeVars = predicate.accept(FreeVariables())
                print(f"\t\tq_{e}({', '.join(freeVars)}):- {predicate}")
        else:
            ## get predicates free variables
            freeVars = predicates.accept(FreeVariables())
            print(f"\t\tq_0({', '.join(freeVars)}):- {predicates}")
        