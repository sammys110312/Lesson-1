secret_code = 45
access_key = 27

def bits(n):
    return format(n, "08b")

print("=== Secret Code and Access Key ===")
print("Secret Code:", secret_code, "Binary:", bits(secret_code))
print("Access Key: ", access_key, "Binary:", bits(access_key))

and_result = secret_code & access_key
or_result = secret_code | access_key

print("\n=== AND and OR ===")
print("AND:", and_result, "Binary:", bits(and_result))
print("OR: ", or_result, "Binary:", bits(or_result))

not_mask = 0xFF
not_result = secret_code ^ not_mask
xor_result = secret_code ^ access_key

print("\n=== NOT and XOR ===")
print("NOT Secret Code:", not_result, "Binary:", bits(not_result))
print("XOR:", xor_result, "Binary:", bits(xor_result))

left_result = secret_code << 1
right_result = secret_code >> 1

print("\n=== Left Shift and Right Shift ===")
print("Left Shift:", left_result, "Binary:", bits(left_result))
print("Right Shift:", right_result, "Binary:", bits(right_result))

parity_result = secret_code ^ 1

print("\n=== Odd or Even ===")
print("Secret Code XOR 1:", parity_result)

if parity_result < secret_code:
    print("The secret code is odd.")
else:
    print("The secret code is even.")

print("\n=== Count Set Bits ===")
print("Number of 1 bits in secret code:", secret_code.bit_count())

print("\n=== Final Summary ===")
print("Secret Code:", secret_code, bits(secret_code))
print("Access Key: ", access_key, bits(access_key))
print("AND:        ", and_result, bits(and_result))
print("OR:         ", or_result, bits(or_result))
print("NOT:        ", not_result, bits(not_result))
print("XOR:        ", xor_result, bits(xor_result))
print("Left Shift: ", left_result, bits(left_result))
print("Right Shift:", right_result, bits(right_result))
print("Set Bits:   ", secret_code.bit_count())