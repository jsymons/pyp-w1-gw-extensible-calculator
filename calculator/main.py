from datetime import datetime

from calculator.operations import *
from calculator.exceptions import *


def create_new_calculator(operations={}):
    dictionary = {
            'operations': operations,
            'history': []
            }
    
    return dictionary

def perform_operation(calc, operation, params):
    """
    
    Executes given operation with given params. It returns the result of the
    operation execution.

    :param calc: A calculator.
    :param operation: String with the operation name. ie: 'add'
    :param params: Tuple containing the list of nums to operate with.
                   ie: (1, 2, 3, 4.5, -2)
                   
    def test_perform_operation(self):
        res = perform_operation(self.calc, 'add', (5, 3))
        self.assertEqual(res, 8)
    """
    # import ipdb; ipdb.set_trace() 
    return calc['operations'].get(operation)(*params)


def add_new_operation(calc, operation):
    """
    Adds given operation to the list of supported operations for given calculator.

    :param calc: A calculator.
    :param operation: Dict with the single operation to be added.
                      ie: {'add': add_function}
                       add_new_operation(self.calc, operation={'add': self.add})
    """
    # import ipdb; ipdb.set_trace()
    calc['operations'].update(operation)
    pass


def get_operations(calc):
    """
    Returns the list of operation names supported by given calculator.
    """
    pass


def get_history(calc):
    """
    Returns the history of the executed operations since the last reset or
    since the calculator creation.

    History items must have the following format:
        (:execution_time, :operation_name, :params, :result)

        ie:
        ('2016-05-20 12:00:00', 'add', (1, 2), 3),
    """
    # history = ()
    # return history
    pass


def reset_history(calc):
    # set calc history to = []
    # import ipdb; ipdb.set_trace()    
    # return []
    pass

def repeat_last_operation(calc):
    """
    Returns the result of the last operation executed in the history.
    """
    pass

