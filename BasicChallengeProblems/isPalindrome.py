def isPalindrome(userInput):
    return (userInput == userInput[::-1])
# userInput = input("\nEnter the string you want to check palindrome for : ")
print(isPalindrome('viv'))