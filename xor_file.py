def str_xor(data, key):
    for i in range(len(data)):
        data[i] ^= key[i % len(key)]
    return data

key = bytearray.fromhex('f7176c0ffee555a4')
data = bytearray(open('in.jpeg', 'rb').read())

encoded = str_xor(data, key)
open("out.jpeg", "wb").write(encoded)