def bubbleSort (myArray):
    for i in range(len(myArray)-2):
        print(f"Begin Step {i+1}")
        for x in range(len(myArray)-1):
            if(myArray[x] > myArray[x+1]):
                placeholder = myArray[x+1]
                myArray[x+1] = myArray[x]
                myArray[x] = placeholder
            print(myArray)
        print(f"End Step {i+1}")
    print(myArray)

bubbleSort([7,16,3,9,85,6,2,5, 32, 186, 12])



