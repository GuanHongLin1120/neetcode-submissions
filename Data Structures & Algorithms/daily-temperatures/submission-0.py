class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        t = temperatures
        stack = []
        res = [0] * len(t)

        for i in range(len(t)):
            while stack and t[i] > t[stack[-1]]:
                last = stack.pop()
                res[last] += (i - last)
            stack.append(i)
        
        return res
            