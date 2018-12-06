# -*- coding: utf-8 -*-

d = {
    'Michael': 95,
    'Bob': 75,
    'Tracy': 85
}
print('d[\'Michael\'] =', d['Michael'])
print('d[\'Bob\'] =', d['Bob'])
print('d[\'Tracy\'] =', d['Tracy'])
print('d.get(\'Tracy\', -2) =', d.get('Tracy', -2))
print('d.get(\'Thomas\', -3) =', d.get('Thomas', -3))
#print('d[\'Thomas\'] =', d['Thomas'])   KeyError: 'Thomas'

'''
print:
d['Michael'] = 95
d['Bob'] = 75
d['Tracy'] = 85
d.get('Tracy', -2) = 85
d.get('Thomas', -3) = -3
'''