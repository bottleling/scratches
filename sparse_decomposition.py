from math import ceil, pow

def isSparse(N):
    return (N & N << 1) ==0

def solution(N):

    if isSparse(N):
        #print(N, "{0:b}".format(N) + " is sparse")
        return N

    # for i in range(N//2+1):
    #     if isSparse(i) and isSparse(N-i):
    #         #print("{0:b}".format(i), "{0:b}".format(N-i), "are sparse")
    #         return i
    i = N//2
    while i >=1:
        s = isSparse(i)
        if s and isSparse(N - i):
            return i
        if not s:
            print(i, "{0:b}".format(i))
            i /=2
        else:
            i-=1
    return -1
def main():
    #testcases = [x for x in range(100000)]
    testcases = [26]#,int(1e6),int(1e7), int(1e8), int(1e9)]
    for i in range(len(testcases)):
        tc = testcases[i]
        x= solution(tc)
        #if x== -1:
        print(tc, x)
if __name__ == '__main__':
    main()