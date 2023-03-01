# swea 1970 쉬운 거스름돈

# money = [50000, 10000, 5000, 1000, 500, 100, 50, 10]

# for t in range(1,int(input())+1):
#     chg = []
#     price = int(input())
#     for m in money:
#         chg.append(price//m)
#         price %= m
#     print(f'#{t}')
#     print(*chg)

print(*['long' for _ in range(int(input())//4)],'int')