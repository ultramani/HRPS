import sys

# https://www.hackerrank.com/challenges/python-print/problem?isFullScreen=true
def printWithNoStringMethod ():
    value = int(input().strip())
    value = [i for i in range(1,value+1)]
    print(*value, sep='', file=sys.stdout)
    

    

