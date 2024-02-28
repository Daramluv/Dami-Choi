class Solution:
    def strStr(self, haystack, needle):
        length_needle=len(needle)
        for i in range(len(haystack)):
            test=haystack[i:length_needle+i]
            if test==needle:
                return i
        return -1