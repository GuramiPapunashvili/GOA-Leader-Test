def Anagram_Detection(st1, st2):
    if len(st1) != len(st2):
        return False
    st1_letters = [i.lower() for i in st1]
    st2_letters = [i.lower() for i in st2]
    Anagram_test = []
    for i in st1_letters[::]:
        if i.lower() in st2_letters:
            st1_letters.remove(i)
        elif i.lower() not in st2_letters:
            Anagram_test.append(i)
    if len(Anagram_test) != 0:
        return False
    return True   

print(Anagram_Detection("Buckethead", "DeathCubeK"))    