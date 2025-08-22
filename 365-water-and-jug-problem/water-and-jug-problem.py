# Problem Summary:
# Given two jugs, with capacities x liters and y liters
# Have infinite water supply (we can keep pouring more water into x or y)
# Can only reach target by filling jug COMPLETELY with water
# emptying WHOLE jug or pouring water from one jug to another

# Approach:
# Use Greatest Common Denominator to determine if we can make some combination
# of x, y to reach target
# If we compute GCD with Euclidean Algorithm, we can repeatdely reduce, x, y until
# x or y becomes zero
# KEY IDEA: the target will ONLY EVER BE REACHED IF AND ONLY IF the target is a MULTIPLE
# of the GCD of (x, y)

class Solution:
    def canMeasureWater(self, x: int, y: int, target: int) -> bool:
        # Edge Cases
        if target > x + y:
            return False
        if target == 0:
            return True
        if x == 0 or y == 0:
            return (target == x or target == y)
        
        # all other cases, see if target is multiple of GCD
        def gcd(a: int, b: int) -> int:
            # reduce (a, b) until b becomes zero
            while b != 0:
                tmp = a
                a = b
                b = tmp % b
            
            return a

        res = gcd(x, y)
        return target % res == 0
