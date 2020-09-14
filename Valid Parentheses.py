Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
 

Example 1:

Input: s = "()"
Output: true
Example 2:

Input: s = "()[]{}"
Output: true
Example 3:

Input: s = "(]"
Output: false
Example 4:

Input: s = "([)]"
Output: false
Example 5:

Input: s = "{[]}"
Output: true
 

Constraints:

1 <= s.length <= 104
s consists of parentheses only '()[]{}'.

*****************************************************8

 def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        dic = {'(' : ')','[':']','{' : '}',')':'(',']':'[','}':'{'}
        st = set(('(','[','{'))
        List = []
        if len(s) == 0:
                return True
        for i in s:
            if i in st:
                List.append(i)
            elif len(List)>0 and List[-1] == dic[i]:
                del List[-1]
            else:
                return False
           
        return False if len(List) else True
                
