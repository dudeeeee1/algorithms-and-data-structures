def Anagram(A, B):
    if len(A) != len(B):
        return False
    count = [0] * 36
    for i in range(len(A)):
        if 'a' <= A[i] <= 'z':
            count[ord(A[i]) - ord('a')] += 1
        else:
            count[26 + ord(A[i]) - ord('0')] += 1

        if 'a' <= B[i] <= 'z':
            count[ord(B[i]) - ord('a')] -= 1
        else:
            count[26 + ord(B[i]) - ord('0')] -= 1
    for x in count:
        if x != 0:
            return False

    return True


A = input()
B = input()

if Anagram(A, B):
    print("YES")
else:
    print("NO")