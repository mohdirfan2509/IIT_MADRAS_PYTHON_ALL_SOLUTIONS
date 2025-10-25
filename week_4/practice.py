# # lists
# l1=[]
# l2=list()
# print(type(l1))
# print(type(l2))
# # tuples
# tup1=()
# tup2=tuple((1,))
# print(type(tup1))
# print(type(tup2))
# # sets 
# s1={1}
# s2=set()
# print(type(s1))
# print(type(s2))

# print(min([1,2,3,4,-1,4]))
# add=lambda x,y,z: x+y+z
# print(add(1,2,3))

m=3
print([[1 if i==j else 0 for j in range(m)] for i in range(m)])
print([[1 if j<=i else 0 for j in range(m)] for i in range(m)])
