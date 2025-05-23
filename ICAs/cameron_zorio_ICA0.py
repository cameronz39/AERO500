# Cameron Zorio ICA0
x = 5

l = []

for i in range(5):
    l.append(i)
print(l)

l = [item * x for item in l]
print(l)

D = {"C": 67, "A": 65, "B": 66, "E": 69, "D": 68}
D.update({"!": 33, "2": 50})

for key,val in sorted(D.items()):
    print(f"The decimal number, {key}, is the ASCII code for the character '{val}'")
