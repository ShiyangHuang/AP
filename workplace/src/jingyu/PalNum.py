def isPalindrome(x):
        length=len(str(x))
        if x<0:
            return False
        for i in range(length/2):
            if (x/10**i)%10!=(x/10**(length-1-i))%10:
                return False
        return True
