class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        #starting pointer and middle pointer
        red, white = 0,0
        
        #right pointer
        blue = len(nums)-1
        
        while(white<=blue):
            #red case - 0
            if nums[white] == 0:
                #swap using the bucket method
                nums[white],nums[red] = nums[red],nums[white]
                white+=1
                red+=1
            #white case - 1
            elif nums[white] == 1:
                white+=1
            #blue case - 2
            else:
                nums[white],nums[blue] = nums[blue], nums[white]
                blue-=1
