class Solution:
    def distanceBetweenBusStops(self, distance, start, destination):
        s = min(start, destination)
        d = max(start, destination)
        if s == d:
            return 0
        #路线1
        d1 = sum(distance[s:d])
        #路线2
        d2 = sum(distance) - d1
        return min(d1, d2)
