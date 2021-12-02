def solution(n):

    if n==1:
        return '1'
    elif n==2:
        return '2'
    elif n==3:
        return '4'    

    return solution(n//3)+solution(n%3) if n%3!=0 else solution(n//3-1)+solution(3)
