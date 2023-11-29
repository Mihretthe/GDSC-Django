def sum(nums):
    s = 0
    for i in nums:
        if i > 0:
            s += i
    return s
n = list(map(int, input("Enter the list here: ").split()))
print(sum(n))
