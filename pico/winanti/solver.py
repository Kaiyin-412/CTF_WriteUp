output = "kgxmwpbpuqtorzapjhfmebmccvwycyvewpxiheifvnuqsrgexl"
secret1 = 85
secret2 = 51
secret3 = 15
fix = 97
le = len(output)
input = 0
hold = 0
i =0

output = list(output)
while i<=2:
    for i_0 in range (0,le):
        random1 = (secret1 & (i_0 % 255)) + (secret1 & ((i_0 % 255) >> 1))
        random2 = (random1 & secret2) + (secret2 & (random1 >> 2))
        output_list[i_0] = chr(((ord(output_list[i_0]) - fix - (random2 & secret3) - (secret3 & (random2 >> 4))) % 26 + 26) % 26 + fix)


print("".join(output))
  