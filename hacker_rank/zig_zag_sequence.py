def findZigZagSequence(a, n):
    a.sort()
    mid = int((n + 1) / 2) - 1
    a[mid], a[n - 1] = a[n - 1], a[mid]

    st = mid + 1
    ed = n - 2
    while (st <= ed):
        a[st], a[ed] = a[ed], a[st]
        st = st + 1
        ed = ed - 1

    for i in range(n):
        if i == n - 1:
            print(a[i])
        else:
            print(a[i], end=' ')
    return


print(findZigZagSequence([2,3,5,1,4], 5))
print(findZigZagSequence([1, 2, 3, 4, 5, 6, 7], 7))
expected = [1, 2, 3, 7, 6, 5, 4]