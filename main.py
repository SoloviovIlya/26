def step(a, b):
    if b == 0:
        return 1
    if b == 1:
        return a
    if b>1:
        return a*step(a,b-1)
print(step(2, 4))