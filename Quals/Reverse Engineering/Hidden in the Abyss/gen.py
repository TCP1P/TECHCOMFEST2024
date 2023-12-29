import hashlib

def md5(s):
    return hashlib.md5(s.encode('utf-8')).hexdigest()

flag = 'TCF2024{N0t_S0_H1dd3n_Aft3r_4ll}'
print(len(flag))
for s in flag:
    print(s)
    print(md5(s)[::-1])