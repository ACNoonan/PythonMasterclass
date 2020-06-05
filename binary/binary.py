# with open('binary', 'bw') as bin_file:
#     for i in range(17):
#         bin_file.write(bytes([i]))

with open('binary', 'bw') as bin_file:
        bin_file.write(bytes(range(17)))

with open('binary', 'br') as bin_file2:
    for b in bin_file2:
        print(b)

