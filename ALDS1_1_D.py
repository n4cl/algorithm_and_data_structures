# coding: utf-8

n = input()
r = [input() for _ in xrange(n)]
l = len(r)

max_v = - 10 ** 9

# 入力した順に差を求め、差の最大値を得る
for i in xrange(l - 1):
    for j in xrange(i + 1, l):
        diff = r[j] - r[i]
        if diff > max_v:
            max_v = diff

print max_v
