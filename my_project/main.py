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
        (tuple): tuple containing:
            (str): Message from person

            (str): Name of person
    """
    string_out = 'Hello Ryan, from' + user_name
    return string_out, user_name


def practice_func_leo(number_of_fish):
    """
    This function prints a number of fish
    
    Args:
        number_of_fish [int]: How many fish you have
        
    Returns:
        str: a statement of how many fish you have
    """
    
    return 'You have {} fish'.format(number_of_fish)


