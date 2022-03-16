
x = {'key1': 'value1', 'key2': 'value2', 'key3': 'value3', 'key4': 'value4', 'key5': 'value5', 'key6': 'value6'}

invert_dict={}
{invert_dict.setdefault(v,k) for k, v in x.items()}
print (invert_dict)

for k,v in x.items():
    invert_dict.setdefault(v,k)
print (invert_dict)