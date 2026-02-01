class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        reverse = digits[::-1]
        carry = 1
        i = 0

        while carry > 0 and i < len(reverse):

            reverse[i] += carry
            carry -= 1

            if reverse[i] == 10:
                reverse[i] = 0
                carry += 1

            i += 1
            
        if carry:
            reverse.append(carry)
    
        return reverse[::-1]