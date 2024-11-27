immutable_var = 1, 'shirt', False, 5.03
print (immutable_var)
print (type (immutable_var))
# immutable_var [0] = 7    # это неизменяемая коллекция данных, в отличие от списка, чаще используется как хранилище

mutable_list = [3, 'potato', 17.5, 'mango']
print (mutable_list)
mutable_list [0] = False
mutable_list [1] = 'bbb'
mutable_list [2] = 'PiKa'
mutable_list [3] = 146.8
print (mutable_list)
mutable_list.append('dance')
mutable_list.extend('apple')
mutable_list.extend(['apple'])
mutable_list.remove('bbb')
print (mutable_list)