# Boyer Moore's String Search Algorithm in Python

def bad_char_heuristic(pattern):
    bad_char = [-1]*256
    for i in range(len(pattern)):
        bad_char[ord(pattern[i])] = i
    return bad_char

def boyer_moore(text, pattern):
    m = len(pattern)
    n = len(text)

    bad_char = bad_char_heuristic(pattern)

    s = 0
    while s <= n - m:
        j = m - 1
        while j >= 0 and pattern[j] == text[s + j]:
            j -= 1
        if j < 0:
            print(f"Pattern found at index {s}")
            s += (m - bad_char[ord(text[s + m])] if s + m < n else 1)
        else:
            s += max(1, j - bad_char[ord(text[s + j])])

# Sample run
text = "ABAAABCD"
pattern = "ABC"
boyer_moore(text, pattern)
