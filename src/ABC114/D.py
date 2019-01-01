def run(N):
  '''
  a^x*b^y*c^yの約数の数が75となるのは(x,y,z)が以下の場合
  (74,0,0), (2,4,4), (24,2,0), (14,4,0)
  N!の素因数分解を行い、各素数のうち上記の取得方法の数を数える
  '''
  # N!を素因数分解
  primes = {1: 1}
  for i in range(2, N+1):
    tmp = i
    for j in range(2, N+1):
      while tmp%j == 0:
        if j in primes.keys():
          primes[j] += 1
        else:
          primes[j] = 1
        tmp /= j
  cnt = 0

  # (74,0,0)
  for i in primes.values():
    if i >= 74:
      cnt += 1

  # (2,4,4)
  cnt4 = 0
  cnt2 = 0
  for i in primes.values():
    if i >= 4:
      cnt4 += 1
    if i >= 2:
      cnt2 += 1
  if cnt4 >= 2:
    cnt += (cnt4*(cnt4-1)//2)*(cnt2-2)

  # (24,2,0)
  cnt24 = 0
  cnt2 = 0
  for i in primes.values():
    if i >= 24:
      cnt24 += 1
    if i >= 2:
      cnt2 += 1
  if cnt24 >= 1:
    cnt += cnt24*(cnt2-1)

  # (14,4,0)
  cnt14 = 0
  cnt4 = 0
  for i in primes.values():
    if i >= 14:
      cnt14 += 1
    if i >= 4:
      cnt4 += 1
  if cnt14 >= 1:
    cnt += cnt14*(cnt4-1)
  return cnt


def main():
    N = int(input())
    print(run(N))


if __name__ == '__main__':
    main()