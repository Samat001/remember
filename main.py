# file = open('test1.txt', 'a')
# # # file.write('Hello\n')
# # file.writelines('World')
# # file.close()
# file.write('Hello')


# with open('test1.txt') as file:
#     x = 2
#     print(file.read())
# print(x)
# print(file.read())

import json
# json -> JAVA SCRIPT OBJECT NOTATION
# Сериализация (с пайтона в жсон) -> dump , dumps
# десериализация (с жейсона в пайтон-> load , loads
# d = {'hello' : True, 'age' :2 , 'name': None}
# json_obj = json.dumps(d) 
# print(json_obj)
# python_obj = json.loads(json_obj)
# print(python_obj)

# with open('data.json', 'r')as file:
#     # python_obj = json.loads(file.read())работает с объектами
#     python_obj = json.load(file) # load - работает с файлами 
#     print(python_obj)


"name char(20) unique"