
test = "id titeldel1 titeldel2 dato"

x, *y, z = test.split()
print(f"{x}, {" ".join(y)}, {z}")

