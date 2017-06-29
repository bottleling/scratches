import math
def solution(n):
    #print("{0:b}".format(n))
    m=0
    cnt= 0
    ingap =False
    p = 0
    r = n % 2
    q = int(math.ceil(n / 2))
    if q == 1:
        return 0
    if r == 1:
        ingap = True
    while q >=1:
        #print(q, r)
        if ingap and r == 1:
            ingap = False
            m = max(m, cnt)
        elif ingap and r == 0:
            cnt+=1
        elif not ingap and r == 1:
            ingap = True
            cnt = 0
        elif not ingap and r == 0:
            if p == 1:
                ingap = True
                cnt = 1
        p = r
        r = q % 2
        q = int(math.ceil(q / 2))

    return max(m,cnt)
def main():
    testcases = [1,3,4,5,41,1041]
    for i in range(len(testcases)):
        tc = testcases[i]
        print(tc, solution(tc))
if __name__ == '__main__':
    main()