A = 1.023987456
B = 9
C = 'my_string'
print(f"A rounded to 3 decimal places: {A:.3f} yes")
print("three variables are {} , {} , {}".format(A, B, C))
print("{0} - {0} - {0}".format(B))  # same value multiple times
print("%.2f , %d , %s" % (A,B,C))  # outdated style