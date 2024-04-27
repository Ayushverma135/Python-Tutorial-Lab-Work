L1 = [1, 2, 3, 4]
L2 = L1
L3 = L1.copy()
L4 = L3
L1[0] = [5]
print(L1, L2, L3, L4)
