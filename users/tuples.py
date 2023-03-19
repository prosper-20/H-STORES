# ids = {"001", "002", "003", "004", "001"}

# ids2 = ("008", "009")

# ids.update(ids2)
# ids.discard("001")
# print(min(ids))

# b = sorted(ids)
# print(b)



# new2 = any(ids)
# print(new2)

# new_set = {3, 4, 5, 6}
# print(sum(new_set))



# A = {2, 3, 5}

# B = {3, 5, 2}

# print(A==B)

s = {1, 2, 3, 4, 5}
b = {1, 2, 3}

print(b.issubset(s))
s.difference_update({1, 2})
print(s)



# print(A.difference(B))
# print(A.symmetric_difference(B))