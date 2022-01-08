# 解説見た。
# 「K番目に小さい」= 二分探索だと考えて固執してしまったのがだめだった。
# 問題の性質について深く考える癖をつけないとだめ。
k = int(input())
tmp = bin(k)
tmp = tmp.replace('0b', '')
tmp = tmp.replace('1', '2')

print(tmp)


# この問題は2分探索で解く問題じゃなかった。。
# 頭を捻って2進数に置き換えたらで解ける問題だったみたい。
# from bisect import bisect_right
# 
# k = int(input())
# # 0, 2のみからなる正整数を作成したいが、ここがうまくできない。。
# target = [2, 20, 22, 200, 202, 220, 222, 2000, 2002, 2020, 2022, 2200, 2202, 2222]
# 
# 
# def check(x: int) -> bool:
#     cnt = bisect_right(target, x)
#     return cnt >= k
# 
# 
# left = 0
# # right = 10**18
# right = 3000
# while (right - left) > 1:
#     mid = (right + left) // 2
#     print(mid)
#     
#     if check(mid):
#         right = mid
#     else:
#         left = mid
# 
#     print(left, right)
# 
# print(right)
