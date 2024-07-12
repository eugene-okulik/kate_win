my_dict = {
    'tuple': (1, 7, 8, 11, 12),
    'list': ['abc', '123', 'sun', 'moon', 1488],
    'set': {'Artem', 'Marsi', 78, 89, True, False},
    'dict': {'type1': 'Number',
             'type2': 'String',
             'type3': 'Boolean',
             'type4': 'Float',
             'type5': 'List',
             'type6': 'Dictionary',
             'type7': 'Set',
             8: 'Tuple'}
}

print(my_dict['tuple'][-1])

my_dict['list'].append('jupiter')
my_dict['list'].pop(1)

my_dict['set'].add('Victor')
my_dict['set'].remove('Artem')

my_dict['dict'][('i am a tuple',)] = {1: True }
my_dict['dict'].pop(8)
print(my_dict)
