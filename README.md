# Impledge-Question
# Longest Compounded Word Finder
This project implements a Python program identifies the longest and second-longest compounded words from a sorted list of words. A compounded word is one that can be formed by concatenating shorter words in the same list. The program is optimized for performance using dynamic programming and memoization to handle large datasets efficiently.
## Design Decisions
- Input of the program as file having one word per line, sorted alphabetically.
- Dynamic Programming (table): Used to check if a word can be formed by shorter words. The DP table keeps track of valid prefixes of a word.
- Memoization: Avoids redundant calculations by storing results for previously processed words, significantly improving runtime for large inputs.
- Provide Output as : Longest compounded word , Second-longest compounded word , Time taken to process the file.
## Approach
1.  The program reads the input from text files (`Input_01.txt`, `Input_02.txt`), each containing one word per line, sorted alphabetically.
2.  For each word:
   - A DP-based approach verifies if it can be constructed from other words in the list, it occur as :
         -Define a boolean array dp of size len(word) + 1.
         -table[i] represents whether the substring word[0:i] can be constructed using words in the list.
         -dp[0] = True because an empty prefix (substring of length 0) is always valid.
         -For each position i in the word, check all possible prefixes word[j:i] (where j < i).
         -If dp[j] is True and the substring word[j:i] is in the word set, set dp[i] = True.
         -If dp[len(word)] is True, the entire word can be constructed using other words in the list.
           Taking ratcatdogcat
           >For i = 3 (substring rat):
            Prefix dp[0] is True, and rat is in word_set.
            table[3] = True.
           >For i = 6 (substring ratcat):
            Prefix dp[3] is True, and cat is in word_set.
            table[6] = True.
           >For i = 9 (substring ratcatdog):
            Prefix dp[6] is True, and dog is in word_set.
            table[9] = True.
           >For i = 12 (substring ratcatdogcat):
            Prefix dp[9] is True, and cat is in word_set.
            table[12] = True.
            so ratcatdogcat is a compounded word.
## Features
- Finds the longest and second-longest compounded words from input files.
- Uses dynamic programming and memoization for optimal performance.
- Measure the time taken to process the input.
- Handles large datasets efficiently.
## Files
- answer.py is the Main Python script.
- Input_01.txt and Input_02.tx are input files
