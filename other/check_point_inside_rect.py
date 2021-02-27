
p1 = (5, 4)
p2 = (10, 5)
p3 = (10, 10)
p4 = (5, 10)
f_set = [(7, 7), (7, 0), (7, 12), (12, 7), (0, 7), (5, 5)]
# cross = |pi pf| x |pi p|
for f in f_set:
    cross_p12 = (p2[0] - p1[0]) * (f[1] - p1[1]) - (f[0] - p1[0]) * (p2[1] - p1[1])
    cross_p23 = (p3[0] - p2[0]) * (f[1] - p2[1]) - (f[0] - p2[0]) * (p3[1] - p2[1])
    cross_p34 = (p4[0] - p3[0]) * (f[1] - p3[1]) - (f[0] - p3[0]) * (p4[1] - p3[1])
    cross_p41 = (p1[0] - p4[0]) * (f[1] - p4[1]) - (f[0] - p4[0]) * (p1[1] - p4[1])
    ans1234 = cross_p12 * cross_p34
    ans2341 = cross_p23 * cross_p41
    if ans1234 > 0 and ans2341 > 0:
        print(ans1234, ans2341, True)
    else:
        print(ans1234, ans2341, False)





