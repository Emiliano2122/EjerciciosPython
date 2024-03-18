d = [0,1]

d += [(d := [d[1], d[0] + d[1]]) and d[1] for k in range(30)]
print(d)
