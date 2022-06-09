class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        answer = []
        
        def div_3(n):
            return n % 3 == 0
        
        def div_5(n):
            return n % 5 == 0
        
        for i in range(1, n+1):
            if div_3(i) and div_5(i):
                answer.append("FizzBuzz")
            elif div_3(i) and not div_5(i):
                answer.append("Fizz")
            elif div_5(i) and not div_3(i):
                answer.append("Buzz")
            else:
                answer.append(str(i))
       
        return answer