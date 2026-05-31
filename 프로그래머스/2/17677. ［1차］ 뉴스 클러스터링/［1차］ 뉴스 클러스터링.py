from collections import Counter

def solution(str1, str2):
    def make_pairs(s):
        s = s.upper()
        result = []
        
        for i in range(len(s) - 1):
            pair = s[i:i+2]
            
            if pair.isalpha():
                result.append(pair)
        
        return result
    
    arr1 = make_pairs(str1)
    arr2 = make_pairs(str2)
    
    counter1 = Counter(arr1)
    counter2 = Counter(arr2)
    
    intersection = counter1 & counter2
    union = counter1 | counter2
    
    inter_count = sum(intersection.values())
    union_count = sum(union.values())
    
    if union_count == 0:
        return 65536
    
    return int(inter_count / union_count * 65536)