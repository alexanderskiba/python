key0 = 'eardrum.cpu'
value0 = 66.6
timestamp0 = 3336667778


data = f"put {key0} {value0} {timestamp0}\n".encode('utf-8')

resp = data.decode('utf-8').rstrip('\n')
valid = resp.split(' ')
print(valid)
if valid[0] != 'put' and valid[0] != 'get':
    print(valid)
    print(valid[0], 'put')
    print(valid[0] == 'put')
    print('Мы внутри')
elif valid[0] == 'put':
    print('все збс')

