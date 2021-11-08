#####################################################################################################
#                                  First Order Formula visitor                                      #
#####################################################################################################


"""
TODO
====
    - 1. Implement RRI, FV (visitors).
    - 2. Renoval of Forall & handling Negation (Not) : put Not as low as possible in a formulae !
    - 3. Represent Datalog programs.
    - 4. Compile FOL to datalog.
    - 5. Unfolding in datalog. (unfold rules that have variables that are not range restricted ??)
    - 6. Test range restrection for datalog rules.
    - 7. Compute the right datalog program.
    - 8. Execution of the datalog program.

    Unfold those predicates which have a rule which is not range restricted !
    Check that every variable in the head has a positive occurrence in the body

"""

## import dependencies
from model import *
from visitor import VisitUnaryExpression


## 
class EvaluateFirstOrderFormolae(VisitUnaryExpression):

    """
    The EvaluateFirstOrderFormolae can run visitor operations over any set of elements without
    figuring out their concrete classes. The accept operation directs a call to
    the appropriate operation in the visitor object.
    """

    def __init__(self, model:Model, environment={}):
        ## initiate instances
        self.model = model
        self.environment = environment
        self.stack = []

    def visitAnd(self, phi:And):
        """Visitor visiting Conjunction"""
        l = phi.leftExpression.accept(self)
        r = phi.rightExpression.accept(self)
        return l and r

    def visitOr(self, phi:Or):
        """Visitor visiting Disjunction"""
        l = phi.leftExpression.accept(self)
        r = phi.rightExpression.accept(self)
        return l or r

    def visitNot(self, phi:Not):
        """Visitor visiting Negation"""
        e = phi.expression.accept(self)
        return not e

    def visitEqual(self, phi:Equal):
        """Visitor visiting Equality"""
        l = phi.leftExpression.accept(self)
        r = phi.rightExpression.accept(self)
        return l == r

    def visitVariable(self, var:Variable):
        """Visitor visiting variable"""
        return var.name

    def visitConstant(self, const:Constant):
        """Visitor visiting constant"""
        value = const.value.accept(self)
        return value

    def visitActor(self, actor:Actor):
        """Visitor visiting actors"""
        variable = actor.name.accept(self)
        value = self.environment[variable]
        return self.model.actor(value)

    def visitArtist(self, artist:Artist):
        """Visitor visiting artists"""
        variable = artist.name.accept(self)
        value = self.environment[variable]
        return self.model.artist(value)

    def visitDirector(self, director:Director):
        """Visitor visiting film directors"""
        variable = director.name.accept(self)
        value = self.environment[variable]
        return self.model.director(value)

    def visitFilm(self, film:Film):
        """Visitor visiting movies"""
        variable = film.title.accept(self)
        value = self.environment[variable]
        return self.model.film(value)

    def visitActs(self, acts:Acts):
        """Visitor visiting acts"""
        variable_1 = acts.actor.accept(self)
        value_1 = self.environment[variable_1]
        variable_2 = acts.movie.accept(self)
        value_2 = self.environment[variable_2]
        return self.model.acted(value_1, value_2)

    def visitDirects(self, directs:Directs):
        """Visitor visiting directs"""
        variable_1  = directs.director.name
        value_1 = self.environment[variable_1]
        variable_2 = directs.movie.name
        value_2 = self.environment[variable_2]
        return self.model.directed(value_1, value_2)

    def updateEnvironment(self, variable:str=None, value:str=None):
        """Update the environment !"""
        if variable:
            self.environment[variable.name] = value
            return True
        return False

    def copyEnvironment(self):
        """Create & append a copy of the environment in the stack"""
        env = self.environment.copy()
        self.stack.append(env)

    def endEnvironment(self):
        """End the environment"""
        self.environment = self.stack.pop()

    def visitForall(self, phi:Forall):
        """Visitor visiting phi"""

        ## create a copy of the environment
        self.copyEnvironment()
        ## get variable & predicate of forall
        var = phi.variable
        predicate = phi.predicate
        
        ## for each element of the model domain
        for x in self.model.domain:
            ## append x to the environment
            self.environment[x] = []
            self.updateEnvironment(var, x)

            ## evaluate predicate then do things depending on the returned truth-value
            truth_value = predicate.accept(self)
            if not truth_value:
                break
        ## end environment
        self.endEnvironment()
        return truth_value
        
    def visitExists(self, phi:Exists):
        """Visitor visiting phi"""

        ## create a copy of the environment
        self.copyEnvironment()
        ## get variable & predicate of exists
        var = phi.variable
        predicate = phi.predicate
        ## for each element of the model domain
        for x in self.model.domain:
            self.environment[x] = []
            ## associate x to var in environment
            self.updateEnvironment(var, x)
            truth_value = predicate.accept(self)
            ## evaluate predicate then do things depending on the returned truth-value 
            if truth_value:
                break
        ## end environment
        self.endEnvironment()
        return truth_value   



## Proposal testing: we will test our proposal on some simple queries

if __name__ == "__main__":

    ## create variables
    x = Variable('x')
    y = Variable('y')
    z = Variable('z')

    ## create a First Order Formulae representation
    FOL = EvaluateFirstOrderFormolae(model=Model(domain=domain))

    ## Evaluate different queries
    ## We test our proposal by evaluating the first-order formulas that correspond to the following sentences:
    print("Proposal Testing:")

    # 1. Each artist is either an actor or a film director
    print("\n\t 1. Each artist is either an actor or a film director:", end=' ')
    query_1 = Forall(x, Or(Not(Artist(x)), Or(And(Artist(x), Actor(x)), And(Artist(x), Director(x)))))
    result_1 = query_1.accept(FOL)
    print(result_1)

    # 2. Every actor acts in at least one movie
    print("\n\t 2. Every actor acts in at least one movie:", end=' ')
    query_2 = Forall(x, Or(Not(Actor(x)), Exists(y, And(Film(y), Acts(x, y)))))
    result_2 = query_2.accept(FOL)
    print(result_2)

    # 3. Every film director directs at least one movie
    print("\n\t 3. Every film director directs at least one movie:", end=' ')
    query_3 = Forall(x, Or(Not(Director(x)), Exists(y, And(Film(y), Directs(x, y)))))
    result_3 = query_3.accept(FOL)
    print(result_3)

    # 4. No actor acts in every movie
    print("\n\t 4. No actor acts in every movie:", end=' ')
    query_4 = Not(Exists(x, And(Actor(x), Forall(y, Or(Not(Film(y)), Acts(x, y))))))
    result_4 = query_4.accept(FOL)
    print(result_4)

    # 5. For each movie, at least two actors are involved
    print("\n\t 5. For each movie, at least two actors are involved:", end=' ')
    query_5 = Forall(x, Or(Not(Film(x)), And(Exists(y, And(Actor(y), Acts(y, x))), Exists(z, And(Actor(z), And(Acts(z, x), Not(Equal(z, y))))))))
    result_5 = query_5.accept(FOL)
    print(result_5)
