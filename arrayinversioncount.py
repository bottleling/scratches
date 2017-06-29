import bisect as bs
def solution(arr): #63%
    x = sorted([(v,k) for k, v in enumerate(arr)])
    y = [s[1] for s in x]
    cnt= 0
    #print(y)
    for i in range(len(y)):
        cnt+= len(filter(lambda r: r> y[i], y[0:i] ))
    return cnt
def main():
    testcases = [[-1,6,3,4,7,4],[5,3,2,6],[4,1],[1,1],[1,2],[], [5,4,3,2,1]]

    for i in range(len(testcases)):
        tc = testcases[i]
        print(tc, solution(tc))
if __name__ == '__main__':
    main()