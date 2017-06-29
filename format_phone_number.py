
def solution(S):
    S = S.replace("-", "").replace(" ", "")
    if len(S) == 2:
        return S

    nThree = len(S) // 3  # number of 3 digit blocks
    nThree = nThree - 1 if len(S) % 3 == 1 else nThree

    result = []
    j = nThree * 3
    for i in range(0, j, 3):
        result.append(S[i:i + 3])
    for i in range(j, len(S),2):
        result.append(S[i:i + 2])
    return "-".join(result)
  
def main():
    testcases = ["00-44  48 5555 8361","0 - 22 1985--324","555372654","00","0-0","00 1"]

    for i in range(len(testcases)):
        tc = testcases[i]
        print(tc, solution(tc))
if __name__ == '__main__':
    main()