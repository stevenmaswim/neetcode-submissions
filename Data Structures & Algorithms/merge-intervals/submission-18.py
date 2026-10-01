class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0]) #sort by first index of each member of the list
        output = []
        for interval in intervals: # loops through intervals in intervals
            if not output or output[-1][1] < interval[0]: # checks if there is anything in output or if the last intervals last index is less than the current intervals first index.
                output.append(interval)
                #appends to the output
            else: #opposite of the first
                output[-1][1] = max(output[-1][1], interval[1])
                # output's last interval's last index is equal to whichever interval has the higher second index
        return output
        # returns the output
