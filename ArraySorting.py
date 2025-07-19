#Allows the visualization of various array sorting methods using colourful numbers for easier tracking.

#Quick constants:
WHITE = '\033[97m'
RESET = '\033[0m' #To return to standard terminal text color


class colourfulNumber:
    """
    Class that associates a particular colour to a number.
    """
    unused = ['\033[91m', '\033[92m', '\033[93m','\033[94m', '\033[95m', '\033[96m', '\033[31m', '\033[32m', '\033[33m', '\033[34m', '\033[35m', '\033[36m', '\033[37m']
    def __init__(self, num):
        self.num = num
        if len(self.unused) == 0:
            print("There are more numbers than available colours. The number " + num + " will be " + WHITE + "white" + RESET + ".")
            self.colour = WHITE
        else:
            self.colour = self.unused.pop()
    def __str__(self):
        return (self.colour + str(self.num) + RESET)

class colourfulArray():
    """
    Remakes array so that each number in it is a colourfulNumber.
    """
    def __init__(self, array):
        self.array = []
        for i in range(len(array)):
            self.array.append(colourfulNumber(array[i]))
    def __str__(self):
        endString = ""
        for n in range(len(self.array)):
            endString += str(self.array[n]) + "   "
        return endString

def bubbleSort(colArray):
    print("Bubble Sort for array: " + str(colArray))
    print("Time complexity: O(n^2). Space complexity: O(1).")
    for n in range(len(colArray.array)):
        swapped = False         #to track if anything was swapped in inner loop
        for i in range(len(colArray.array)-1):
            if colArray.array[i].num > colArray.array[i + 1].num:
                print("Swapping " + str(colArray.array[i]) + " and " + str(colArray.array[i + 1]) + ". Result:")
                colArray.array[i], colArray.array[i + 1] = colArray.array[i + 1], colArray.array[i]         #swap elements if needed
                print(colArray)
                swapped = True
        if not swapped:
            print("Done! End result is: " + str(colArray))
            break

def selectionSort(colArray):
    print("Selection Sort for array: " + str(colArray))
    print("Time complexity: O(n^2). Space complexity: O(1).")
    for n in range(len(colArray.array)-1):
        minIndex = n
        print("Currently looking for the " + str(n) + "th smallest value.")
        for i in range(n+1, len(colArray.array)):
            if colArray.array[i].num < colArray.array[minIndex].num:
                minIndex = i
        colArray.array[n], colArray.array[minIndex] = colArray.array[minIndex], colArray.array[n]
        print(str(n) + "th smallest value determined to be " + str(colArray.array[n]) + ". With it in place, we have: ")
        print(colArray)
    print("Done! End result is: " + str(colArray))

def insertionSort(colArray):
    print("Insertion Sort for array: " + str(colArray))
    print("Time complexity: O(n^2). Space complexity: O(1).")
    for n in range(1,len(colArray.array)):
        key = colArray.array[n]
        keynum = key.num
        print("Currently looking where to place " + str(key) + ".")
        j=n-1
        while j >= 0 and colArray.array[j].num > keynum:
            colArray.array[j+1] = colArray.array[j]
            print("Because " + str(key) + " is smaller than " + str(colArray.array[j]) + ", " + str(colArray.array[j]) + " shifted right: " + str(colArray))
            j-= 1
        colArray.array[j+1] = key
        print(str(key) + " placed at position " + str(j+1) + ". Current array is: " + str(colArray))
    print("Done! End result is: " + str(colArray))

newArray = [34,244,249,776,414,932,388,223,7]
newCArray = colourfulArray(newArray)
insertionSort(newCArray)