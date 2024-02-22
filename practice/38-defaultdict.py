from collections import defaultdict

my_dict_str= defaultdict(str)
print(my_dict_str) # defaultdict(<class 'str'>, {})
print(my_dict_str['key']) # ''

my_dict_list= defaultdict(list)
print(my_dict_list) # defaultdict(<class 'list'>, {})
print(my_dict_list['key']) # []

print('str- key: \'\' + hello')
my_dict_str['key']+= 'Hello'
print(my_dict_str['key'])

print('list- key: []+4')
my_dict_list['key'].append(4)
print(my_dict_list['key'])