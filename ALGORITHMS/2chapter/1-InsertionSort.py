#Insertion sort


def sortNumber(array_A):
    for j in range (1, len(array_A)):
        key = array_A[j]
   
        i = j-1

        while i >= 0 and key < array_A[i]:
            array_A[i + 1] = array_A[i]
            i -= 1
        array_A[i+1] = key
    
array_A = [5,2,4,6,1,3]
sortNumber(array_A)

for i in range (len(array_A)):
    print(array_A[i])
