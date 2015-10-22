def dot_product(list1, list2):
    if (len (list1) != len(list2)):
        return float("NaN")
    else:
        suma = 0
        for i in range (len(list1)):
            x= list1[i] * list2[i]
            suma = suma + x
        return suma

list1= [1,2,3]
list2= [4,2,1]
print(dot_product(list1, list2))
