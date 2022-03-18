import time
x = int(input())
y = int(input())
jumlah = 0
start = time.time()
while (y != 0) :
    r = x % y
    x = y
    y = r
    print(x,y)
    jumlah = jumlah + 1
print(x,jumlah)
end = time.time()
print("The time of execution of above program is :", end-start)