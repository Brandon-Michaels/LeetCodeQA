# Problem Summary:
# Given two jugs, with capacities x liters and y liters
# Have infinite water supply (we can keep pouring more water into x or y)
# Can only reach target by filling jug COMPLETELY with water
# emptying WHOLE jug or pouring water from one jug to another

# Approach:


class Solution:
    def canMeasureWater(self, x: int, y: int, target: int) -> bool:
        # If target exceeds total capacity, impossible
        if target > x + y:
            return False
        # If target is zero, trivially possible
        if target == 0:
            return True
        # If one jug is zero, only exact fills of the other or zero work
        if x == 0 or y == 0:
            return target == x or target == y

        # Helper to compute gcd using Euclidean algorithm
        def gcd(a: int, b: int) -> int:
            # Repeatedly reduce (a, b) until b becomes zero
            while b != 0:
                a, b = b, a % b
            return a

        # Bézout condition: target must be a multiple of gcd(x, y)
        g = gcd(x, y)
        return target % g == 0

        