encrypted = input()
final = ''
encrypted_lst = list(encrypted)
encrypter = encrypted_lst[0:2]
remaining = encrypted_lst[2:len(encrypted_lst) + 1]
for remain in remaining:
    final += remain
for encrypt in encrypter:
    final += encrypt
print(final)
