''' 
[intervals, ]
sol 1. simply go through start~end and check if capacity exceeds


sol 2.

Input: trips = [[2,1,5],[3,3,7]], capacity = 4
Output: false
'''
class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        timestamp = []
        for trip in trips:
            timestamp.append([trip[1], trip[0]])
            timestamp.append([trip[2], -trip[0]])

        timestamp.sort()
        # print(timestamp)

        used_capacity = 0
        for time, passenger_change in timestamp:
            # print(used_capacity)
            used_capacity += passenger_change
            if used_capacity > capacity:
                return False

        return True