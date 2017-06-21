# coding: utf-8


def bubble_sort(a, n):
    # バブルソート

    cnt = 0
    flag = 1
    i = 0

    while flag:
        flag = 0

        for j in xrange(n-1, i, -1):
            if a[j] < a[j-1]:
                a[j], a[j-1] = a[j-1], a[j]
                flag = 1
                cnt += 1

        i += 1

    # ソート結果
    print " ".join(map(str, a))
    print cnt


if __name__ == '__main__':

    i_n = input()
    i_a = map(int, raw_input().split())

    bubble_sort(i_a, i_n)
