# セット

s = { 'a', 'b', 'c', 'd' }
t = {'c', 'd', 'e', 'f'}

u = s | t # s.union(t)
print(u) # {'a', 'b', 'c', 'd', 'e', 'f'}

x = s & t # s.intersection(t)
print(x) # {'c', 'd' } 

y = s - t # s.difference(t)
print(y) # {'a', 'b'}

z = s ^ t # s.symmetric_difference(t)
print(z) # {'a', 'b'. 'e', 'f'}

s |= t
print(s)

# issubset, issupperset, isdisjoint
s = {'apple', 'lemon'}
t = {'apple', 'banana', 'lemon'}
u = {'cherry'}

print(s.issubset(t)) # True
print(s.issuperset(t)) # False sはtの要素をすべて含んでいるか
print(t.issuperset(s)) # True tはsの要素をすべて含んでいるか

print(t.isdisjoint(s)) # False：重なっている要素が一つ以上あるのでFalse
print(t.isdisjoint(u)) # True：重なっている要素が一つもない場合True 