K = int(input())

nums = [i for i in range(10)]
pre_nums = [i for i in range(10)]
cnt = 9
for d in range(2, 11):
    temp_nums = []
    for i in range(d-1, 10):
        for n in pre_nums:
            if n // (10**(d-2)) < i:
                temp_nums.append(n+(i*(10**(d-1))))
                cnt += 1
    pre_nums = temp_nums
    nums += temp_nums
    if cnt >= K:
        break

print(nums[K])
