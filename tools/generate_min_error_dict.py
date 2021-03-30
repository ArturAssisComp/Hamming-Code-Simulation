'''
Lab. 1
'''
import numpy as np

def generate_min_error_dict():
    '''
    Description: This function returns a dictionary with each key:value corresponding
    to key==[binary number represented by the syndrome] and value==[the associated error
    with minimum weight].

    Input: void

    Output: dict

    Time Complexity: O(1)

    Space Complexity: O(1)
    '''
    result_dict = {}

    Ht = np.array([
            #s1 s2 s3 s4 s5 s6
            [1, 1, 1, 0, 0, 0], #b1
            [1, 1, 0, 1, 0, 0], #b2
            [1, 0, 1, 0, 1, 0], #b3
            [0, 1, 1, 0, 0, 1], #b4
            [0, 0, 0, 1, 1, 1], #b5
            [1, 0, 0, 1, 1, 0], #b6
            [0, 1, 0, 1, 0, 1], #b7
            [0, 0, 1, 0, 1, 1], #b8
            [1, 0, 0, 0, 0, 0], #p1
            [0, 1, 0, 0, 0, 0], #p2
            [0, 0, 1, 0, 0, 0], #p3
            [0, 0, 0, 1, 0, 0], #p4
            [0, 0, 0, 0, 1, 0], #p5
            [0, 0, 0, 0, 0, 1]  #p6
        ])

    #Iterate through syndromes:
    for i in range(64):
        #Calculate the syndrome:
        s = np.array([0, 0, 0, 0, 0, 0])
        num = i
        for j in range(6):
            if (num % 2):
                s[len(s) - 1 - j] = 1
            num = num // 2

        #Find the error with the minimum weight that satisfy the syndrome:
        min_weight = 15 #Maximum weight + 1
        min_error = None

        ##Loop through possible errors.
        for k in range(16384): #2^14 --> number of possible errors.
            e = np.array([0 for _ in range(14)])
            weight = 0
            num = k
            for t in range(14):
                if (num % 2):
                    e[len(e) - 1 - t] = 1
                    weight += 1
                num = num // 2

            #Check if the error satisfy the syndrome:
            if(all((e @ Ht) % 2 == s)):
                #Check if the weight is less than the min weight:
                if(weight < min_weight):

                    #update the minimum weight:
                    min_weight = weight
                    min_error = e

        #Update the result dictionary:
        result_dict[i] = min_error.copy()

    #Return the resultant table with minimum weight error for each syndrome.
    return result_dict



