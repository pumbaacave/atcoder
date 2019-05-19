from collections import Counter
class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        if not instructions: return True
        dirs = ["n", "w", "s", "e"]
        moves = Counter(dirs)
        def turn_left(d):
            return (d + 1) % 4
        def turn_right(d):
            return (d + 3) % 4
        def do(d, ins):
            for i in ins:
                if i == "G":
                    moves[dirs[d]] += 1
                elif i == "L":
                    d = turn_left(d)
                elif i == "R":
                    d = turn_right(d)
            
            return d
        d = 0
        for i in range(4):
            d = do(d, instructions)
        if moves["n"] == moves["s"] and moves["w"] == moves["e"]:
            return True
        else:
            return False

