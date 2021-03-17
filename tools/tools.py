'''
LAB 1 - ELE-33
ALUNOS:
    Ana Paula Lopes Schuch
    Artur Assis Alves

Hamming Code Simulation
'''

#Import libs:
import numpy as np
import random


#Auxiliary Functions:

def _validate_positive_integer(var, name):
    '''
    Description: This function checks if 'var' is a positive int. If it is not,
    then a TypeError or a ValueError is raised. If 'var' is not int, TypeError
    is raised. If 'var' is int but negative or 0, then ValueError is raised.
    The error message is customized using the name 'name' of the variable 'var'.

    Input: var --> object that will be validated.
           name --> the name that will be used in the error message.

    Output: void
    '''
    if not isinstance(var, int):
        raise TypeError("{} must be an int.".format(name))

    if var <= 0:
        raise ValueError("{} must be a positive int.".format(name))

def _hamming_weight(word):
    '''
    Description: This function calculates the Hamming weight of the numpy array
    'word'. 'word' contains only 0's and 1's. The Hamming weight is equal to
    the number of 1's in the array.

    Input: word --> numpy array with 1's and 0's.

    Output: int --> The Hamming Weight of 'word'.

    Time Complexity: O(n)

    Space Complexity: O(1)
    '''
    return sum(word)

def _hamming_distance(w1, w1):
    '''
    Description: This function calculates the Hamming distance between the numpy
    array 'w1' and the numpy array 'w2'. The Hamming distance is equal to the 
    number of positions that they differ. 'w1' and 'w2' must have the same length.

    Input: w1, w2 --> numpy arrays of 0's and 1's with the same length.

    Output: int --> Hamming distance between 'w1' and 'w2'.

    Time Complexity: O(n)

    Space Complexity: O(1)
    '''
    if (len(w1) != len(w2)):
        raise ValueError("w1 and w2 must have the same length")

    return _hamming_weight((w1 + w2) % 2)

#Function definitions:

def generate_words(n, k = 4, extra_bits = 3):
    '''
    Description: This function randomly generates n information words with 
    k + extra_bits bits each. The extra bits are not information bits,
    they can be used to encode the words later. Each bit (including extra bits) 
    has a probability of 50% to become 1.  The function returns a numpy array 
    with (k + extra_bits)*n bits. The index of each word starts at 
    i*(k + extra_bits), 0 >= i <= n - 1.

    Input: n --> integer that represents the number of information words that
                 will be generated.
           k --> The size of each information word.
           extra_bits --> the number of extra bit that will be generated for
                          each information word.

    Output: numpy array --> Array with n information words ((k + extra_bits) * n).

    Time Complexity: O(n*(k + extra_bits)) 

    Space Complexity: O(n*(k + extra_bits))
    '''
    #Check inputs:
    _validate_positive_integer(n, 'n')
    _validate_positive_integer(k, 'k')
    _validate_positive_integer(extra_bits, 'extra_bits')

    #Return the result:
    return np.array([random.randint(0, 1) for _ in range(n * (k + extra_bits))])

def encoder(information_words):
    '''
    Description: An encoder that transforms N information words with 4 bits each 
    into codewords with 7 bits each (3 additional bits used for error correction). 
    This encoder is based on Hamming code technique. 

    Input: information_words --> numpy array with len(information_words)/4 
                                 information words (or len(information_words) bits). 

    Output: codewords --> numpy array with 7*len(information_words)/4 bits (or
                          len(information_words)/4 codewords).

    Time Complexity: O(n)

    Space Complexity: O(1)

    '''
    pass


def binary_symmetric_channel(bit_array, p):
    '''
    Description: This function simulates the transmission of the bits from 
    'bit_array' through a binary symmetric channel. The original array is 
    changed in such a way that each bit has a probability 'p' to change its
    value. 

    Input: bit_array --> numpy array with bits that will be transmitted through
                         the channel.
           p --> parameter that gives the probability of changing each bit.

    Output: void

    Time Complexity: O(n)

    Space Complexity: ------
    '''
    pass


def decoder(codewords):
    '''
    Description: An decoder that transforms N  codewords with 7 bits each 
    into information words with 4 bits each. This decoder is based on Hamming 
    code technique. 

    Input: codewords --> numpy array with N codewords (7 * N bits).

    Output: numpy array --> numpy array with N information words (4 * N bits).

    Time Complexity: O(?)

    Space Complexity: O(?)
    '''
    pass


def comparator(array1, array2):
    '''
    Description: This function compares 'array1' with array2'. It returns the
    ratio between the number of different corresponding elements and the total 
    number of elements. len(array1) must be equal len(array2).

    Input: array1 --> first numpy array.
           array2 --> second numpy array.

    Output: float --> ration between the number of different corresponding 
                      elements and the total number of elements.

    Time Complexity: O(n)

    Space Complexity: O(1)
    '''
    pass
