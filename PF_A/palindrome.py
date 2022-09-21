def is_palindrome(str):
    for i in range(0,int(len(str)/2)):
        if str[1] !=str[len(str)-i-1]:
            return False
        return True
ans = is_palindrome("rotator")
if(ans):
    print("False")
else:
    print("True")