![GitHub Contributors Image](https://contrib.rocks/image?repo=o-ikne/Database-Project-FOL)
[![Generic badge](https://img.shields.io/badge/Made_With-Python-<COLOR>.svg)](https://shields.io/)
[![Linux](https://svgshare.com/i/Zhy.svg)](https://svgshare.com/i/Zhy.svg)
![visitor badge](https://visitor-badge.glitch.me/badge?page_id=o-ikne.Database-Project-FOL)

## __Databases Project: First Order Logic into Non-recursive Datalog__

### __Overview__

This project is part of the course on databases taught by Mr. Sylvain Salvati, and it’s about
first order logic as a query language. Throughout this project, we will first propose a naive
representation of the evaluation of first order formulas in Python, and then, in order to push this approach further, we
will look for a deep representation and evaluation of these formulas by compiling FOL formulas to a Non-recursive Datalog program. A useful description can be found in [here](https://www.fil.univ-lille1.fr/~salvati/cours/bdd_M2_ds/fol/fo_evaluation.html).

Interesting concepts of fondations of databases can be found [here](http://webdam.inria.fr/Alice/)

### __Data__
The data used during this project can be found [here](https://www.fil.univ-lille1.fr/~salvati/cours/bdd_M2_ds/fol/fo_evaluation.html).

### __Naive implementation of the evaluation__

In this subsection we will try our first (’naive’) approach to represent and evaluate first order
formulas. In order to do that, we will use the fact that most of modern languages are higher-
order in the sense that they allow functions to take functions as argument. Therefore, we will
implement first order quantifiers using this feature so that we can write in our programming
language first order formulae as follow (this method is called shallow embedding. For example, the following query: 

```Python 
forall(lambda x: not artist(x) or (artist(x) and (actor(x) or director(x))))
```

refers to the statement: "Each artist is either an actor or a film director.", and this yields false, which means that there is an artist who is neither an actor nor a film
director.

### __Deep representation of first order formulae__
Rather than using simple function, the elements of the model will be represented as Python
classes, in other words, each of the elements in our model will be a Python object. Each
one of these objects will have a method accept, that will accept a visitor. In fact, we
will be using Design - Visitor Pattern to evaluate first order formulas as well as in other
processes, which we will see later, such as finding Free variables or Range-restricted variables
of a given formula. Each one of those visitors can run visitor operations over any set of
elements without figuring out their concrete classes. The accept operation directs a call to
the appropriate operation in the visitor object.

The main steps of this section are:

1. Implementation of Range Restricted Interpretation (RRI) and Free Variables (FV) visitors.
2. Renoval of Forall & handling Negation (Not) : put Not as low as possible in a formulae !
3. Represent Datalog programs.
4. Compile FOL to datalog.
5. Unfolding in datalog. (unfold rules that have variables that are not range restricted).
6. Test range restrection for datalog rules.
7. Compute the right datalog program.
8. Execution of the datalog program.

For more details check the project <a href="Report/DB Project Report - Ikne Omar.pdf" target="_blank"> report</a>.
