def solution(T): #tree needs tree object
    left = 0  # No height, only node
    right = 0
    if T.l != None:
        left = 1 + solution(T.l)  # current height + height of subtrees
    if T.r != None:
        right = 1 + solution(T.r)

    return max(left, right)

def main():
    testcases = [[-1,3,-4,5,1,-6,2,1]]
    for i in range(len(testcases)):
        tc = testcases[i]
        print(tc, solution(tc))
if __name__ == '__main__':
    main()