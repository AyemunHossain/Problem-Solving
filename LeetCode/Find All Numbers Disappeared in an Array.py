class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        length = len(nums)
        nums = set(nums)
        final_list = set()
        
        print(len(nums))
        for i in range(1,length+1):
            if i not in nums:
                print(i)
                final_list.add(i)
                
        return list(final_list)