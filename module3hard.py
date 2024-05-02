
def calculate_structure_sum(data_structure):
    if isinstance(data_structure,int):
        return data_structure
    elif isinstance(data_structure,str):
        return len(data_structure)
    elif ( isinstance(data_structure,list) or
           isinstance(data_structure,tuple) or
           isinstance(data_structure,set) ):
        sum_ = 0
        for elem in data_structure:
            sum_ += calculate_structure_sum(elem)
        return sum_
    elif isinstance(data_structure,dict):
        sum_ = 0
        for key,value in data_structure.items():
            sum_ += calculate_structure_sum(key)
            sum_ += calculate_structure_sum(value)
        return sum_
    else:
        print('unsupperted type',type(data_structure),data_structure)

data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]

result = calculate_structure_sum(data_structure)
print(result)