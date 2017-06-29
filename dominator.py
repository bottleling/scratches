
def solution(arr):
    if len(arr) == 0 :
        return -1
    elem = None
    cnt = 0
    for i in arr:
        if i == elem:
            cnt +=1
        elif i != elem:
            if cnt!=0:
                cnt -=1
            else:
                cnt = 0
                elem = i

    cnt = 0
    result = -1
    for k,v in enumerate(arr):
        if v == elem:
            cnt +=1
            result = k

    if cnt <= (len(arr) / 2):
        return -1
    return result

def main():
    testCases = [[3,4,3,2,3,-1,3,3],[],[1], [1,2],[1,3,3],[2,2,4,4], [1,2,3],[3,3,3],[2,2,4,4,6,6]]
    for tc in testCases[5:8]:
        print("result:", tc, solution(tc))

if __name__ == '__main__':
    main()
    
