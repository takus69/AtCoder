H, W, T = map(int, input().split())
A = []
for _ in range(H):
    A.append(list(input().split()))

# 幅優先でGまでT以下かどうかを判定
# お菓子18個のため、取る取らないで全探索可能？
# DP? (i, j, 歩数, お菓子)=300×300×2×10^6×18