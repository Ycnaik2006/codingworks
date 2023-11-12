dict=[{"name":"aryan","score":"2006"},
      {"name":"ramesh","score":"2007"},
       {"name":"lagan","score":"2008"},
       {"name":"paul","score":"2009"}]
key_to_find="score"
dictionary_with_max_value=max(dict,key=lambda x:x[key_to_find])
print("Dictionary with the highest value",key_to_find,":",dictionary_with_max_value)