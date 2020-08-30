class Solution(object):

    def findMedianSortedArrats(self, nums1, nums2):

        num1len = nums1.length()
        num2len = nums2.length()
        end = (num1len + num2len) / 2
        num1place = 0
        cursor = 0
        num2place = 0
        num1 = False
        while(cursor < end):
            if(num1place < num1len and nums1[num1place] < nums2[num2place]):
                num1 = True
                num1place += 1
                cursor += 1
            elif(num2place < num2len):
                num1 = False
                num2place += 1
                cursor += 1
