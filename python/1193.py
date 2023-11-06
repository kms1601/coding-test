x = int(input())
sum_ = 1
tmp = 1
while sum_ <= x:
    sum_ += tmp
    tmp += 1
sum_ -= tmp
if sum_ % 2 == 0:
    print(x - sum_, "/", sum_ + tmp - x, sep="")
else:
    print(sum_ + tmp - x, "/", x - sum_, sep="")
