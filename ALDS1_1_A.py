# coding: utf-8


def insertion_sort(a, n):
    # 挿入ソート

    for i in xrange(1, n):

        # 途中経過の出力
        print " ".join(map(str, a))

        v = a[i]
        j = i - 1

        while j >= 0 and a[j] > v:
            a[j+1] = a[j]
            j -= 1

        a[j+1] = v

    # ソート結果
    print " ".join(map(str, a))


if __name__ == '__main__':

    i_n = input()
    i_a = map(int, raw_input().split())

    insertion_sort(i_a, i_n)
