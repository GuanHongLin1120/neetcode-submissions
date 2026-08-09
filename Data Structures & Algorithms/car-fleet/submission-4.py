class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        res = len(position)
        time = []
        sorted_pairs = sorted(list(zip(position, speed)), reverse = True)
        position, speed = zip(*sorted_pairs)


        for i in range(len(position)):
            t = (target - position[i]) / speed[i]
            if time and t <= time[-1]:
                res -= 1
            else:
                time.append(t)
        return res
        
