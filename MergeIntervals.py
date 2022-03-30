class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        #base case
        if len(intervals) < 2: return intervals
        
        #make sure it's sorted
        intervals.sort()
        
        #list of lists
        #this contains the first list in the list, i.e., => [[1, 3]]
        output = [intervals[0]]
        
        #start from the second element onward, i.e., [2,6]
        for start,end in intervals[1:]:
            #check if the start is greater than the previous one's end, start at the second element
            #here start = 2, output[-1][1]=3
            if start > output[-1][1]:
                #this isn't true, so don't execute
                output.append([start,end])
            #check if the end is greater than the previous, if so, update
            #here end = 6, output[-1][1]=3
            elif end > output[-1][1]:
                #this case is true, so output[-1][1] = 6 now
                #the interval is now [1,6]
                output[-1][1] = end
            
        return output
