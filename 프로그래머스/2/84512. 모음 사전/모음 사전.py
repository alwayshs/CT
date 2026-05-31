def solution(word):
    vowels = ["A", "E", "I", "O", "U"]
    words = []
    
    def dfs(current):
        if len(current) > 5:
            return
        
        if current:
            words.append(current)
        
        for vowel in vowels:
            dfs(current + vowel)
    
    dfs("")
    words.sort()
    
    return words.index(word) + 1