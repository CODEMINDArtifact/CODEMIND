alphabet = 'abcdefghijklmnopqrstuvwxyz'
s = 'uppercased # % ^ @ ! vz.'
a = [x for x in alphabet if x.upper() in s]
if s.upper() == s:
    a.append('all_uppercased')
print(a)