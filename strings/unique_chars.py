# O(1) space
# O(nlogn)10
def unique_chars(s: str) -> bool:
    s = sorted(s)
    i,j = 0,1
    while i < len(s) and j < len(s):
        if s[i] == s[j]:
            return False
        else:
            i = j 
        j = j + 1
    return True

if __name__=="__main__":
    print(unique_chars("adbcd"))