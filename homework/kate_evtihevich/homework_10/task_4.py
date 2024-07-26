# Дан такой кусок прайс листа:
# PRICE_LIST = '''тетрадь 50р
# книга 200р
# ручка 100р
# карандаш 70р
# альбом 120р
# пенал 300р
# рюкзак 500р'''
# При помощи дst comprehension и/или dict comprehension превратите этот текст в
# словарь такого вида:
# {'тетрадь': 50, 'книга': 200, 'ручка': 100, 'карандаш': 70, 'альбом': 120, 'пенал': 300, 'рюкзак': 500}
# В выполнении не должно быть циклов.
#
# Обратите внимание, что цены в словаре имеют тип int (они не в кавычках)
PRICE_LIST = '''тетрадь 50р
книга 200р
ручка 100р
карандаш 70р
альбом 120р
пенал 300р
рюкзак 500р'''
price_dict = {k: int(v[:-1]) for k, v in (x.split(' ') for x in PRICE_LIST.split('\n'))}
print(price_dict)
