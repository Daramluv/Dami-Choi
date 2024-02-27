class Solution:
    def removeElement(self, nums, val):
       nums[:] = [i for i in nums if i !=val] 
        