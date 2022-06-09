candidate = 100
armstrong = []
while candidate < 1000:
    s = str(candidate)
    sums = 0
    for n in s:
        m = int(n)
        sums += (m * m * m)
    if sums == candidate:
        armstrong.append(candidate)
    candidate += 1
print(armstrong)