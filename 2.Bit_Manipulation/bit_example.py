x = 5
y = 8
z = 10

#d -> decimal
#b -> binary -> bin(n)
#o -> octal -> oct(n)
#x | X -> hexadecimal hex(n)


#Formas de como transformar un numero a binario, octal y hexadecimal. 

#AND

print(f'{x & y = :08b}')
print(f'{y & z = :08b}')
print(f'{255 = : 02X}')

#OR
print(f'{x | y = :08b}')
print(f'{y | z = :08b}')

#XOR
print(f'{x ^ y = :08b}')
print(f'{y ^ z = :08b}')

#NOT

print(f'{~x = }')
print(f'{~~y = }')

#SHL
# x << n = (2**n) * x
print(f'{x << 1 = }')
print(f'{x << 3 = }')

#SHR
# x >> n = x/(2**n)
print(f'{x >> 1 = }')
print(f'{x >> 3 = }')

def is_even(n : int) -> bool:
    return(n & 1) == 0

print(f'{is_even(5) = }')
