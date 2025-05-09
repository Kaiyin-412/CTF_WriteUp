def reverse_transformation(output):
    secret1 = 85
    secret2 = 51
    secret3 = 15
    fix = 97
    le = len(output)

    # Convert output to list (since strings are immutable)
    output_list = list(output)

    # Apply reverse transformation 3 times
    for _ in range(3):
        for i_0 in range(le):
            random1 = (secret1 & (i_0 % 255)) + (secret1 & ((i_0 % 255) >> 1))
            random2 = (random1 & secret2) + (secret2 & (random1 >> 2))
            
            # Reverse the transformation formula
            output_list[i_0] = chr(((ord(output_list[i_0]) - fix - (random2 & secret3) - (secret3 & (random2 >> 4))) % 26 + 26) % 26 + fix)

    # Convert list back to string
    return "".join(output_list)

# Given transformed output
encrypted_output = "kgxmwpbpuqtorzapjhfmebmccvwycyvewpxiheifvnuqsrgexl"

# Recover original input
original_input = reverse_transformation(encrypted_output)
print("Recovered Input:", original_input)
