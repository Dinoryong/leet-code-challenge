''' 
[intervals, ]
sol 1. simply go through start~end and check if capacity exceeds
=> O(Nlog(N))

sol 2. Bucket Sort
=> O (max(N,1001))

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
    
# sol 2
# class Solution:
#     def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
#         timestamp = [0] * 1001
#         for trip in trips:
#             timestamp[trip[1]] += trip[0]
#             timestamp[trip[2]] -= trip[0]

#         used_capacity = 0
#         for passenger_change in timestamp:
#             used_capacity += passenger_change
#             if used_capacity > capacity:
#                 return False

#         return True