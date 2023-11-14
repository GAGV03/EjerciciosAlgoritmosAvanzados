from typing import Optional

def word_break(s: str, words: set[str]) -> Optional[str]:
    result: Optional[list[str]] = find(s,words)
    if result is not None:
        return " ".join(result)
    return None
    
def find(s:str, words: set[str], answer: list[str] = []) -> Optional[list[str]]:
    if s == '':
        return answer
    index: int = 0
    word: str = ''
    while index < len(s):
        word += s[index]
        if word in words:
            new_answer: Optional[list[str]] = find(s[index+1:],words,answer + [word])
            if new_answer is not None:
                return new_answer
        index += 1
    return None
    


if __name__ == '__main__':
    
    words: set[str] = {"the","a","an","boy","girl","dog","ran","ate","homework","table","them","my"}
    
    print(word_break('thedogatemyhomework',words))
    