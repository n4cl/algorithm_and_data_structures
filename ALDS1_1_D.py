# coding: utf-8

n = input()
r = [input() for _ in xrange(n)]
l = len(r)

max_v = - 10 ** 9
min_v = r[0]

# 最大値と最小値の差を得る
for i in xrange(1, l):
    max_v = max(max_v, r[i] - min_v)
    min_v = min(min_v, r[i])

print max_v
