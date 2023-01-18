from readheader import read_header

f = open('C:\\Users\\Matthew\\Downloads\\died.mp2', 'rb')

header = read_header(f)

print(header)
