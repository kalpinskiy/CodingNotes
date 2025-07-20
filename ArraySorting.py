#Allows the visualization of various array sorting methods using colourful numbers for easier tracking.
#Note that none of the

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
            print("There are more numbers than available colours. The number " + str(num) + " will be " + WHITE + "white" + RESET + ".")
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
        endString = "[ "
        for n in range(len(self.array)):
            endString += str(self.array[n])
            if n < len(self.array) - 1:
                endString += "   "
            else:
                endString += " ]"
        return endString
    @property
    def __copy__(self):
        copyArr = colourfulArray([])
        for n in range(len(self.array)):
            copyArr.array.append(self.array[n])
        return copyArr
    def pop(self):
        if len(self.array) == 0:
            print("There are no numbers available.")
            return None
        return self.array.pop()

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
            return colArray

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
    return colArray

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
    print(colArray)

def mergeSort(colArray, recurs):
    if recurs == 0:         #keeps track if first recursion, to only print out below info once
        print("Merge Sort for array: " + str(colArray))
        print("Merge Sort is a recursive sort. It divides the array into two sections repeteadly until "
              "each array section only has a length of 1. At each step, current portion of array to be sorted will be shown. "
              "The arrays are then merged by comparing their elements sequantially.")
        print("Time complexity: O(nlogn). Space complexity: O(n).")
        recurs = len(colArray.array)
    if len(colArray.array) <= 1:
        return colArray
    tempR = colourfulArray([])           #will be used during recursions for easier showcasing
    tempL = colourfulArray([])
    mid = len(colArray.array) // 2
    leftArr = colArray.__copy__
    leftArr.array = leftArr.array[:mid]
    rightArr = colArray.__copy__
    rightArr.array = rightArr.array[mid:]
    print("Splitting the array " + str(colArray) + " into two parts: " + str(leftArr) + " and " + str(rightArr))
    left = mergeSort(leftArr, recurs)
    right = mergeSort(rightArr, recurs)
    answ = merge(left, right)
    if recurs == len(answ.array):
        print("Merging and sorting done. Answer is: " +str(answ))
        return answ
    else:
        return answ
def merge(left, right):
    output = colourfulArray([])
    i=0
    j=0
    print("Merging arrays " + str(left) + " with " + str(right))
    print("To do so, starting at index 0 for both.")
    tempR = right.__copy__
    tempL = left.__copy__
    while i < len(left.array) and j < len(right.array):
        if left.array[i].num < right.array[j].num:
            output.array.append(left.array[i])
            print("Because the left array at position " + str(i) + " is smaller than the right array at position " + str(j) + ", appending " + str(left.array[i]) + " to the output array: " + str(output))
            i += 1
            if i < len(left.array):
                tempL = left.__copy__
                tempL.array = tempL.array[i:]
                print("Remainder of left array: " + str(tempL) + ". Remainder of right array: " + str(tempR))
        else:
            output.array.append(right.array[j])
            print("Because the right array at position " + str(j) + " is smaller than the right array at position " + str(i) + ", appending " + str(right.array[j]) + " to the output array: " + str(output))
            j += 1
            if j < len(right.array):
                tempR = right.__copy__
                tempR.array = tempR.array[j:]
                print("Remainder of left array: " + str(tempL) + ". Remainder of right array: " + str(tempR))
    if i < len(left.array):
        output.array.extend(left.array[i:])
        temp = left.__copy__
        temp.array = temp.array[i:]
        print(
            "Now that we have reached the end of the right array, we'll append the remaining elements of the left array (" + str(temp) + ") to the output: " + str(
                output))
    else:
        output.array.extend(right.array[j:])
        temp = right.__copy__
        temp.array = temp.array[j:]
        print(
            "Now that we have reached the end of the left array, we'll append the remaining elements of the right array (" + str(
                temp) + ") to the output: " + str(
                output))
    return output


def runProgram(cArr):
    print("Perfect! The array to be sorted is " + str(cArr))
    print("Please choose a sorting algorithm:")
    print("(1) Bubble Sort")
    print("(2) Selection Sort")
    print("(3) Insertion Sort")
    print("(4) Merge Sort")
    print("(5) Exit")
    sortAlg = int(input("Enter your choice: "))
    if sortAlg < 1 or sortAlg > 5:
        print("Sorry, didn't get that. Please choose a sorting algorithm:")
        print("(1) Bubble Sort")
        print("(2) Selection Sort")
        print("(3) Insertion Sort")
        print("(4) Merge Sort")
        print("(5) Exit")
        sortAlg = int(input("Enter your choice: "))
    if sortAlg == 1:
        bubbleSort(cArr)
    elif sortAlg == 2:
        selectionSort(cArr)
    elif sortAlg == 3:
        insertionSort(cArr)
    elif sortAlg == 4:
        mergeSort(cArr)
    print("Thank you for using this program. Goodbye!")

newArray = [34,244,249,776,414,932,388,223,7]
newCArray = colourfulArray(newArray)
print("This program allows you to visualize various sorting algorithms.\n"
      "Currently, it supports Bubble Sort, Selection Sort, Insertion Sort, and Merge Sort.")
ownArr = input("Would you like to use a pre-made array or make your own? Enter \"m\" to use a pre-made array or enter \"o\" to make an array: ")
while ownArr != "m" and ownArr != "o":
    ownArr = input("Sorry, didn't get that. Enter \"m\" to use a pre-made array or enter \"o\" to make an array: ")
if ownArr == "m":
    runProgram(newCArray)
else:
    colourfulNumber.unused = ['\033[91m', '\033[92m', '\033[93m','\033[94m', '\033[95m', '\033[96m', '\033[31m', '\033[32m', '\033[33m', '\033[34m', '\033[35m', '\033[36m', '\033[37m']
    anotherCArr = colourfulArray([])
    num = input("Please enter an integer to be added to the array: ")
    while(len(anotherCArr.array) == 0):
        try:
            num = int(num)
            anotherCArr.array.append(colourfulNumber(num))
        except ValueError:
            num = input("Sorry, didn't get that. Please enter an integer to be added to the array: ")
    while num != "done":
        num = input("Please enter an integer to be added to the array, or enter \"done\" to exit: ")
        if num == "done":
            break
        try:
            num = int(num)
            anotherCArr.array.append(colourfulNumber(num))
        except ValueError:
            num = input("Sorry, didn't get that.")
    print("Perfect, your array is: " + str(anotherCArr))
    runProgram(anotherCArr)
