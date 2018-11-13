with open("binary",'bw') as bin_file:
    for i in range(17):
        bin_file.write(bytes([i]))

with open("binary",'br') as binfile:
    for b in binfile:
        print(b)