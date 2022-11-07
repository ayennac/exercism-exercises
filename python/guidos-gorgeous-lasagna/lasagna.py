"""Functions used in preparing Guido's gorgeous lasagna.

Learn about Guido, the creator of the Python language: https://en.wikipedia.org/wiki/Guido_van_Rossum
"""



EXPECTED_BAKE_TIME = 40

def bake_time_remaining(time):
    """Function that takes the actual minutes the lasagna has been in the oven as
     an argument and returns how many minutes the lasagna still needs to bake
     based on the `EXPECTED_BAKE_TIME"""
    time_remaining = EXPECTED_BAKE_TIME - time
    return time_remaining




def preparation_time_in_minutes(layers):
    """Preparation time of lasagna in mintes"""
    return layers * 2



def elapsed_time_in_minutes(number_of_layers, elapsed_bake_time):
    """Returns lapsed time of lasagna bakes"""
    return preparation_time_in_minutes(number_of_layers) + elapsed_bake_time
