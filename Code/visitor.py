############################################################################################
#                                Abstract Visitor                                          #
############################################################################################


class VisitUnaryExpression:
    """Abstract visitor class for concrete visitor classes:
       the methods defined in this class will be inherited by all concrete visitor classes.
    """

    def visitAnd(self, expr):
        pass

    def visitOr(self, expr):
        pass

    def visitNot(self, expr):
        pass

    def visitForall(self, expr):
        pass

    def visitExists(self, expr):
        pass

    def visitActor(self, expr):
        pass

    def visitArtist(self, expr):
        pass

    def visitFilm(self, expr):
        pass

    def visitDirector(self, expr):
        pass

    def visitActs(self, expr):
        pass

    def visitDirects(self, expr):
        pass

    def visitVariable(self, expr):
        pass

    def visitConstant(self, expr):
        pass

    def visitEqual(self, expr):
        ...