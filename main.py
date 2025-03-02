'''
This is a set of array functions that i made. The goal was to do opperations with arrays without using the built in functions of python.
'''

# 1. Find the length of an array
def arrayLen(arrayIn):
    check = False
    length = 0
    if not(type(arrayIn) == str):
        extraarray = arrayIn.copy()
    else:
        extraarray = list(arrayIn)
    while check == False:
        try:
            extraarray.pop(0)
            length += 1
        except IndexError:
            check = True
    return(length)



# 2. Sort an array
def sortarray(arrayIn):
    extraarray = arrayIn.copy()
    sortedarray = []
    while arrayLen(extraarray) > 0:
        sortedarray.append(arrayMin(extraarray))
        extraarray.remove(arrayMin(extraarray))
    return(sortedarray)



# 3. Find the smallest number in an array
def arrayMin(arrayIn):
    extraarray = arrayIn.copy()
    minInt = extraarray[0]
    check = True
    while check:
        try:
            if extraarray[0] < minInt:
                minInt = extraarray[0]
                extraarray.pop(0)
            else:
                extraarray.pop(0)
        except IndexError:
            check = False
    return(minInt)



# 3. Find the largest number in an array
def arrayMax(arrayIn):
    return(sortarray(arrayIn)[arrayLen(arrayIn)-1])



# 4. Find the sum of all numbers
def arraySum(arrayIn):
    sumOfarray = 0
    for i in range(arrayLen(arrayIn)):
        sumOfarray += arrayIn[i]
    return(sumOfarray)



# 5. Find the average
def average(arrayIn):
    return(arraySum(arrayIn)/arrayLen(arrayIn))



# 6. Find the length of each word in an array

def wordLenarray(arrayIn):
    wordLengths = []
    wordlen = 0
    for i in range(arrayLen(arrayIn)):
        for x in range (arrayLen(arrayIn[i])):
            wordlen +=1
        wordLengths.append(wordlen)
        wordlen = 0
    return wordLengths




