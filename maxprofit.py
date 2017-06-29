
def solution(arr):
    if len(arr) <=1:
        return 0
    profit = 0
    buy = arr[0]
    sell = buy
    for i in range(1, len(arr)):
        sell = arr[i]
        profit = max(profit,sell-buy)
        buy = min(buy, arr[i])
    if profit < 0:
        return 0
    return profit

def main():
    testCases = [[23171,21011,21123,21366,21013,21367],[],[0],[0,0],[1,0],[0,10],[5,10,15]]
    for tc in testCases:
        print("result:", tc, solution(tc))

if __name__ == '__main__':
    main()
    
