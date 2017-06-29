
def solution(arr): #25% performance
    pairs = 0
    if len(arr) <=1:
        return 0
    se = sorted([(i - arr[i], i + arr[i]) for i in range(len(arr))])
    print(se)
    for i in range(len(se)):
        if pairs > 10000000:
            return -1
        e = se[i][1]
        for j in range(i+1, len(se)):
                pairs = pairs + 1 if se[j][0] <= e else pairs


    return pairs

def solution2(arr): #12% performance
    #import numpy as np
    #which = lambda lst: list(np.where(lst)[0])
    pairs = 0
    if len(arr) <=1:
        return 0
    starts = sorted([(i - arr[i]) for i in range(len(arr))])
    se = sorted([(i - arr[i], i + arr[i]) for i in range(len(arr))])
    print(se)
    for i in range(len(se)):
        if pairs > 10000000:
            return -1
        e = se[i][1]
        pairs += sum(map(lambda x: x<=e, starts[(i+1):]))

    return pairs
def main():
    testCases = [[1,5,2,1,4,0],[],[1],[0.5,0.2],[1,1],[1,0,3]]
    for tc in testCases:
        print("result:", tc, solution2(tc))

if __name__ == '__main__':
    main()
    
