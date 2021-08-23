class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # two pointers i and j; one each for nums1 and nums2
        # k will keep track of the values in nums1 since we are overwriting
        i,j,k = 0,0,0
        # temporary array for nums1
        temp = nums1.copy()
        
        while i<m and j<n:
            if temp[i] < nums2[j]:
                nums1[k] = temp[i]
                i+=1
            else:
                nums1[k] = nums2[j]
                j+=1
            k+=1
        # if anything is left over, add that to nums1
        while i<m:
            nums1[k] = temp[i]
            i+=1
            k+=1
        while j<n:
            nums1[k] = nums2[j]
            j+=1
            k+=1
            
# could also do this
def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None
    del nums1[m:]
    nums.extend(nums2)
    nums1.sort()
