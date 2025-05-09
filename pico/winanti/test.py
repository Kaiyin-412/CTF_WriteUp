i = 0
output = "kgxmwpbpuqtorzapjhfmebmccvwycyvewpxiheifvnuqsrgexl"
secret1 = 85
secret2 = 51
secret3 = 15
fix = 97
le = len(output)
input_str = "70'3&6(3$7 28#$03.,0+%0#)9 9&96\"&6$,.(,&\"18162'\"$/"

# Convert string to list for mutability
input_list = list(input_str)

while i <= 2:
    for i_0 in range(0,le):  
        random1 = (secret1 & (i_0 % 255)) + (secret1 & ((i_0 % 255) >> 1))
        random2 = (random1 & secret2) + (secret2 & (random1 >> 2))
        input_list[i_0] = chr(((random2 & secret3) + ord(input_list[i_0]) - fix + (secret3 & (random2 >> 4))) % 26 + fix)
    i += 1

# Convert list back to string
input_str = "".join(input_list)

print(input_str == output)