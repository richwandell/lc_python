def sliding_windows(n, array):

    left = 0
    right = 0

    sum = 0
    max = -1
    while right < len(array):
        if left == right:
            sum = array[left]
            right += 1
        elif right - left == n:
            sum -= array[left]
            sum += array[right]
            right += 1
            left += 1
        else:
            sum += array[right]
            right += 1
        if sum > max:
            max = sum
    return max

print(sliding_windows(3, [2,3,4,1,5]))
print(sliding_windows(3, [2,3,4,1,5,2,7,1]))