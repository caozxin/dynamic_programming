class Solution:
    """
    @param s: the maximum length of s is 1000
    @return: the longest palindromic subsequence's length
    """
    def longest_palindrome_subseq(self, s: str) -> int:
        # write your code here
        """
        for loop in each char:
            if the char in dict, append the number of it
            if char not in dict, append char and add 1
        print out the most repeated number of char
        """
        # gather all char with their frequencys
        input_string = s
        char_counter = {}
        for idx, a_char in enumerate (input_string):
            # print(a_char)
            if a_char not in  char_counter:
                char_counter[a_char] = 1
            elif a_char in  char_counter:
                char_counter[a_char] += 1
        print(char_counter) 
        # result = sorted(char_counter.items(), key=lambda x:x[1], reverse=True)
        # print("result", result[0][1])

        return result[0][1]

new_solution = Solution()

input_string = "asdfasdvvaaadasdf"
input_string02 = "racecar"
new_solution.longest_palindrome_subseq(input_string02)

