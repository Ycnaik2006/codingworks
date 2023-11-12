from array import array
orig_array=array('i',[1,2,3,4,5,6])
print(orig_array)
new_item=int(input("Enter a number:"))
orig_array.append(new_item)
print("appended array",orig_array)