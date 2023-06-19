'''
A sentence is a list of words that are separated by a single space with no leading or trailing spaces.

You are given an array of strings sentences, where each sentences[i] represents a single sentence.

Return the maximum number of words that appear in a single sentence.

Input: sentences = ["alice and bob love leetcode", "i think so too", "this is great thanks very much"]
Output: 6
Explanation: 
- The first sentence, "alice and bob love leetcode", has 5 words in total.
- The second sentence, "i think so too", has 4 words in total.
- The third sentence, "this is great thanks very much", has 6 words in total.
Thus, the maximum number of words in a single sentence comes from the third sentence, which has 6 words.
'''

# Solution-1 - Using len function
class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        max_no_words = 0
        for sentence in sentences:
            split_sentence = sentence.split(" ")
            sen_len = len(split_sentence)
            if sen_len > max_no_words:
                max_no_words = sen_len
        return max_no_words

# Solution-2 - Using count function. Optimized solution
class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        max_no_words = 0
        for sentence in sentences:
            space_count = sentence.count(" ")
            if (space_count+1) > max_no_words:
                max_no_words = space_count + 1
        return max_no_words
