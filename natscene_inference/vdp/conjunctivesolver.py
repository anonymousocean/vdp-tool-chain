from z3 import *
from vdp.vdppuzzle import *


class ConjunctiveSolver:
    """
    This is a solver that looks for an FO formula in prenex form. The matrix is a conjunction of 
    relations over objects and the number of quantifiers is predetermined. 
    """

    def __init__(self, num_vars=2, num_conjuncts=None):
        self.num_vars = num_vars
        self.num_conjuncts = num_conjuncts
        self.additional_constraints = []

    # Setter methods for solver attributes
    def __set_num_vars(self, num_vars):
        self.num_vars = num_vars

    def __set_num_conjuncts(self, num_conjuncts):
        self.num_conjuncts = num_conjuncts

    def solve(self, vdppuzzle):
        """
        This represents the core functionality of the ConjunctiveSolver class. It takes a VDPPuzzle
        """

