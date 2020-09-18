Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

Example 1:

Input: ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.

*******************************************************************

def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        column_slices, common_prefix = zip(*strs), ''
        
        for current_column in column_slices:
            
            if len(set(current_column)) == 1:
				# current column-wise slice's character is the same
				# update common prefix
                common_prefix += current_column[0]
            
            else:
				# current column-wise slice's character is different
                break
                
        return common_prefix
                
