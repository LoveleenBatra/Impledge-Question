import time
memo={}
def word_check(w, wordset):
    if w in memo:
        return memo[w]
    if w in wordset:
        wordset.remove(w)
    table = [False] * (len(w) + 1)
    table[0] = True
    for i in range(1, len(w) + 1):
        for j in range(i):
            if table[j] and w[j:i] in wordset:
                table[i] = True
                break
    wordset.add(w)
    memo[w] = table[-1]
    return table[-1]
def checking_longest_word(file):
    with open(file, 'r') as f:
        words = sorted(f.read().splitlines(), key=len, reverse=True)
    wordset = set(words)
    compounded = []
    start = time.time()
    for i in words:
        if word_check(i, wordset):
            compounded.append(i)
        if len(compounded) >= 2: 
            break
    elapsed_time = (time.time() - start) * 1000
    if compounded:
        print("Longest Compounded Word:", compounded[0])
        if len(compounded) > 1:
            print("Second Longest Compounded Word:", compounded[1])
    else:
        print("No compounded words found.")
    print(f"Time taken to process file {file} {elapsed_time:.2f} milliseconds")
checking_longest_word('Input_01.txt')
checking_longest_word('Input_02.txt')