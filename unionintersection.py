array1=[1,2,3,4,5,6]
array2=[1,4,5,6,7,8]

set1=set(array1)
set2=set(array2)

union=set1.union(set2)
intersection=set1.intersection(set2)

union_array=list(union)
intersection_array=list(intersection)

print("Array1:",array1)
print("Array2:",array2)
print("Union",union_array)
print("Intersection",intersection_array)