def solution(s):
    answer = 0
    n = len(s)

    def is_valid(string):
        stack = []
        pair = {
            ')': '(',
            ']': '[',
            '}': '{'
        }

        for ch in string:
            if ch in '([{':
                stack.append(ch)
            else:
                if not stack:
                    return False

                if stack[-1] != pair[ch]:
                    return False

                stack.pop()

        return len(stack) == 0

    for i in range(n):
        rotated = s[i:] + s[:i]

        if is_valid(rotated):
            answer += 1

    return answer