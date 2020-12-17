def isBalanced (str):
    paran_count, bracket_count, curly_count =0,0,0
    if str[0] == ']' or str[0] == ')' or str[0] =='}':
        return 'syntax error'
    for i in str:
            if i == '{': curly_count += 1
            if i == '(': paran_count += 1
            if i == '[': bracket_count += 1
            if i == '}': curly_count -= 1
            if i == ')': paran_count -= 1
            if i == ']': bracket_count -= 1
    result = paran_count + bracket_count + curly_count
    return result == 0
if __name__ == "__main__":
    print(isBalanced('(([]))'))