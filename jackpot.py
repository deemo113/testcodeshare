def testjack(arr):
    ans = False
    num = arr[0]
    count = 0
    len(num)
    for i in range(len(arr)):
        if num == arr[i]:
            count += 1
    if count == len(arr):
        ans = True

    return ans

print(testjack(["n","n","n","n","n"]))
