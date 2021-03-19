'''
LAB 1 - ELE-33
ALUNOS:
    Ana Paula Lopes Schuch
    Artur Assis Alves

Hamming Code Simulation
'''

# Import libs:
import numpy as np
import random


# Auxiliary Functions:
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


def _hamming_distance(w1, w2):
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


def _get_nth_word(array, nth, word_size=4, extra_bits=3):
    '''
    Description: This function returns the slice that corresponds to the nth word
    in the 'array'. The default is used for arrays of information words with 4 
    information bits and 3 extra bits. To use this function with codewords, 
    set extra_bits=0 and word_size=7.

    Input: array --> An array with len(array)/(word_size + extra_bits) words.
           nth --> The position of the selected word. Goes from 0 to len(array)/(word_size + extra_bits) - 1.

    Output: np.array --> The slice array[(word_size + extra_bits)*nth : (word_size + extra_bits)*nth + word_size]

    Time Complexity: O(word_size)

    Space Complexity: O(word_size)
    '''
    # Basic input checking:
    if(len(array) % (word_size + extra_bits)):
        raise ValueError(
            "len(array) must be a multiple of word_size + extra_bits ({}).".format(word_size + extra_bits))

    # Get the slice:
    i0 = (word_size + extra_bits)*nth
    return array[i0: i0 + word_size]


def _store_nth_word(bit_word, array, nth, size=4, offset=0):
    '''
    Description: This function copies the bits from 'bit_word' to the respective bits
    of array, starting at index nth * (size + offset) + offset and finishing at 
    nth * (size + offset) + offset + size - 1. 

    Input: bit_word --> numpy array with 'size' bits.
           array --> numpy array.
           nth --> integer.
           size --> len(bit_word) must be equal to size.
           offset --> integer. 

    Output: void

    Time complexity: O(size)

    Space Complexity: O(1)
    '''
    # Check if len(bit_word) != size:
    if len(bit_word) != size:
        raise ValueError("The size of 'bit_word' and 'size' must be equal.")

    # Change array:
    i0 = nth*(size + offset) + offset
    for i in range(size):
        array[i0 + i] = bit_word[i]

# Function definitions:


def generate_words(n, k=4, extra_bits=3):
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
    # Check inputs:
    _validate_positive_integer(n, 'n')
    _validate_positive_integer(k, 'k')
    if not isinstance(extra_bits, int):
        raise TypeError("{} must be an int.".format("extra_bits"))
    if extra_bits < 0:
        raise ValueError("extra_bits must be non-negative.")

    # Return the result:
    return np.array([random.randint(0, 1) for _ in range(n * (k + extra_bits))])


def encoder(information_words):
    '''
    Description: This function receives as input an np.array with 4 information
    bits and 3 extra bits for each word. There are len(information_words)/7 words.
    The function calculates the values of p1, p2, and p3 (the extra bits) to generate
    the codewords (4 information bits + 3 extra bits) based on Hamming Code. Then,
    it stores the values of p1, p2, and p3 in each corresponding extra bits for each
    information word in the array 'information_words'.

    To generate each extra bit p1, p2, and p3, we do:
                     p1 p2 p3
    [b1 b2 b3 b4] @ [1  1  1] b1   =   [p1 p2 p3]
                    [1  0  1] b2
                    [1  1  1] b3
                    [0  1  1] b4

    Input: information_words --> numpy array with len(information_words)/7 
                                 information words (or len(information_words) bits). 

    Output: void

    Time Complexity: O(n)

    Space Complexity: O(1)
    '''
    # Validate the size of information_words:
    length = len(information_words)
    if (length == 0 or length % 7 != 0):
        raise ValueError(
            "The length of 'information_word' must be multiple of 7 and not 0.")

    # Create the generator matrix (G):
    generator_matrix = np.array([
        # p1 p2 p3
        [1, 1, 1],  # b1
        [1, 0, 1],  # b2
        [1, 1, 0],  # b3
        [0, 1, 1]  # b4
    ])

    # Create codewords array:
    number_of_words = int(length/7)

    # Encode each word from information_words and store it in codewords:
    for i in range(number_of_words):
        information_word = _get_nth_word(information_words, i)
        extra_bits = information_word @ generator_matrix  # v = uG
        extra_bits %= 2  # mod 2 sum
        _store_nth_word(extra_bits, information_words, i, size=3, offset=4)


def binary_symmetric_channel(bit_array, p):
    '''
    Description: This function simulates the transmission of the bits from 
    'bit_array' through a binary symmetric channel. A copy of the original array 
    is changed in such a way that each bit has a probability 'p' to change its
    value. The copy is returned.

    Input: bit_array --> numpy array with bits that will be transmitted through
                         the channel.
           p --> parameter that gives the probability of changing each bit. Must be
                 in the range [0, 1].

    Output: numpy array --> new array with some bits changed.

    Time Complexity: O(n)

    Space Complexity: O(n)
    '''
    # Check the value of p:
    if p < 0 or p > 1:
        raise ValueError("p must be in the range [0, 1].")

    new_bit_array = bit_array.copy()
    if p != 0:
        random_number_generator = random.SystemRandom()
        for i in range(len(new_bit_array)):
            if random_number_generator.random() <= p:
                new_bit_array[i] = (new_bit_array[i] + 1) % 2

    return new_bit_array


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
    # Validate the size of the array received:
    length = len(codewords)
    if (length == 0 or length % 7 != 0):
        raise ValueError(
            "The length of the array must be multiple of 7 and canoot be zero.")

    # Gets syndrome:
    # H matrix transpose:
    Ht = np.array([
        [1, 1, 1],
        [1, 0, 1],
        [1, 1, 0],
        [0, 1, 1],
        [1, 0, 0],
        [0, 1, 0],
        [0, 0, 1]
    ])
    number_of_words = int(length/7)

    result = np.full(0, 0, np.int)

    # Decode each group of seven bits:
    for i in range(number_of_words):
        word = _get_nth_word(codewords, i, 7, 0)
        syndrome = word @ Ht
        error = get_minimum_error(syndrome)
        received = (word + error) % 2
        result = np.concatenate((result, received[0:4]), axis=None)
    return result


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
    if (len(array1) != len(array2)):
        raise ValueError("The arrays must have the same length")
    total = 0
    for i in range(len(array1)):
        if array1[i] != array2[i]:
            total += 1
    return total/len(array1)


def get_minimum_error(syndrome):
    '''
    Description: This function returns the error that has the
    least Hamming weight for a syndrome.

    Input: syndrome --> numpy array (size = 3).

    Output: error --> numpy array (size = 7)

    Time Complexity: O(1)
    '''

    if len(syndrome) != 3:
        raise ValueError("Syndrome must have length 3")

    errors = np.array([[1, 0, 0, 0, 0, 0, 0], [0, 0, 0, 1, 0, 0, 0],
              [0, 1, 0, 0, 0, 0, 0], [0, 0, 1, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 1], [0, 0, 0, 0, 0, 1, 0],
              [0, 0, 0, 0, 1, 0, 0], [0, 0, 0, 0, 0, 0, 0]])

    binary_value = 4*syndrome[2] + 2*syndrome[1] + syndrome[0]

    return errors[binary_value]
