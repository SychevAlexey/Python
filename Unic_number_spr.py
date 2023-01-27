ids = {
  'user1': [213, 213, 213, 15, 213],
  'user2': [54, 54, 119, 119, 119],
  'user3': [213, 98, 98, 35]
}

print(set(sum(ids.values(), [])))
# a, b, c = list(ids.values())
# set_a = set(a)
# set_b = set(b)
# set_c = set(c)

# # set_desc = c[::-1]
# # set_c = set(set_desc)

# total = set_a | set_b | set_c
# print(list(total))