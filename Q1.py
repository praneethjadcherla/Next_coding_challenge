class Solution:

    def print_fizz_buzz(self, input):
        # Your code goes here
        if(input%3==0 and input%5==0):
            return "FizzBuzz"
        elif(input%3==0):
            return "Fizz"
        elif(input%5==0): 
            return "Buzz"
        else:
            return str(input)

s1=Solution()
print(s1.print_fizz_buzz(15))                   