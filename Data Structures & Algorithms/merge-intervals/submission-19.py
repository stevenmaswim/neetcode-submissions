class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x:x[0])
        
        outputs = []

        for interval in intervals:
            if not outputs or outputs[-1][1] < interval[0]:
                outputs.append(interval)
            else: 
                outputs[-1] = [outputs[-1][0],max(outputs[-1][1], interval[1])]
        return outputs
                    
            


