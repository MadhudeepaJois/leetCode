class Solution:
    def reverse(self, x: int) -> int:
        rev=0
        if x>0:
            while(x!=0):
                rem= x%10
                x = x//10
                rev = rev*10 + rem
            if((rev <= (-2)**31) or (rev >=(2**31)-1)):
                return 0
            else:
                return rev
        else:
            x= abs(x)
            while(x!=0):
                rem= x%10
                x = x//10
                rev = rev*10 + rem
            if((rev <= (-2)**31) or (rev >=(2**31)-1)):
                return 0
            else:
                return 0-rev
#Condition - -231 <= x <= 231 - 1
