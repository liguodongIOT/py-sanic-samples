


result = ['a', 'b', 'c']
temp = ['e', 'd', 'f']

result.append('f')
print(result)
result.extend(temp)
print(result)


dirs = "file:///Users/liguodong/work/data/temp/classify/one, file:///Users/liguodong/work/data/temp/classify/two ,file:///Users/liguodong/work/data/temp/classify/three,/Users/liguodong/work/data/temp/classify/two"
dirs = dirs.replace("file://", "")
dir_list = dirs.split(',')
dir_list = [ dir.strip() for dir in dir_list ]
print(dir_list)



