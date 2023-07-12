def calc_minimum_budget(green_ballon, purple_baloon, participants): 
    results = {}
    results["r1"] = 0 
    results["r2"] = 0
    for _ in range(participants):
        a, b = [int(x) for x in input().split()]
        results["r1"] += a 
        results["r2"] += b

    minimum_budget =((min(green_ballon, purple_baloon) * 
                    max(results.values())) +
                    (max(green_ballon, purple_baloon) * 
                    min(results.values())))
    return minimum_budget                


def main():
    test_cases = int(input())
    
    for _ in range(test_cases):
        green_ballon, purple_baloon = [int(x) for x in input().split()] 
        participants = int(input())    
        print(calc_minimum_budget(green_ballon, purple_baloon, participants))


if __name__ == '__main__':
    main()    