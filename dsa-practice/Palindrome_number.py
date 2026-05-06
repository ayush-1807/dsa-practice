# Problem: Palindrome Number
# Platform: LeetCode
# Link: https://leetcode.com/problems/palindrome-number/

class Solution:
    def isPalindrome(self, x: int) -> bool:
        original = x
        reverse = 0

        if x < 0:
            return False

        while x > 0:
            ld = x % 10
            reverse = reverse * 10 + ld
            x = x // 10

        return original == reverse