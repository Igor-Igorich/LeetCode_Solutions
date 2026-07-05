
def len_last_word_too_easy(
        s: str
        ) -> int:
    words = s.split()
    return len(words[-1])

def len_last_word_too_easy_too(
        s: str
        ) -> int:
    s = s.rstrip()
    last_word = s[s.rfind(' ') + 1:]
    
    return len(last_word)

def len_last_word(
        s: str
        ) -> int:
    cnt = 0
    for i in range(len(s)-1, -1, -1):
        if s[i] != ' ':
            cnt += 1
        elif cnt != 0:
            break
    return cnt