"""
Main
====================================
The core module of my example project
"""

def practice_func_ryan(user_name):
    """
    Return a statement from a person

    Args:
        user_name (str): Indicates the name of the person.

    Returns: 
        string_out (str): Message from input name
    """
    string_out = 'Hello Ryan, from' + user_name
    return string_out


def practice_func_leo(number_of_fish):
    """
    This function prints a number of fish
    
    Parameters
    ----------
    Inputs:
        number_of_fish [int]: How many fish you have
        
    Outputs:
        statement [str]: a statement of how many fish you have
    """
    
    return 'You have {} fish'.format(number_of_fish)