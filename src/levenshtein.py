from time import time


# Levenshtein Distance(Edit Distance Algorithm)
def levenshtein(ref, input):
    dist = list()
    for i in range(len(ref) + 1):
        temp = list()
        for j in range(len(input) + 1):
            temp.append(0)
        dist.append(temp)

    for i in range(len(ref) + 1):
        dist[i][0] = i
    for j in range(len(input) + 1):
        dist[0][j] = j

    for j in range(1, len(input) + 1):
        for i in range(1, len(ref) + 1):
            if ref[i-1] == input[j-1]:
                dist[i][j] = dist[i-1][j-1]
            else:
                dist[i][j] = min(dist[i - 1][j - 1] + 1, min(dist[i][j - 1] + 1, dist[i - 1][j] + 1))

    #for line in dist:
    #    print(line)

    return dist, dist[len(ref)][len(input)]


def scoring(ref, input, dist):
    N = len(ref)
    i = len(ref)
    j = len(input)

    D = 0
    I = 0
    S = 0

    # 일치 워드
    search_word = list()
    while not (i == 0 and j == 0):
        s = min(dist[i - 1][j], dist[i - 1][j - 1], dist[i][j - 1])
        if s == dist[i][j]:
            i -= 1
            j -= 1
            search_word.append(ref[i])
        else:   # I <==> D 변경했음
            if s == dist[i - 1][j]:  # I: 추가 (왼쪽)
                print("삭제:", ref[i - 1])
                D += 1
                i -= 1
            elif s == dist[i - 1][j - 1]:  # S: 변경 (왼쪽 위)
                print("수정:", ref[i - 1], input[j - 1])
                S += 1
                i -= 1
                j -= 1
            elif s == dist[i][j - 1]:  # D: 삭제 (위쪽)
                print("삽입:", input[j - 1])
                I += 1
                j -= 1
            search_word.append("  ")

    H = N - S - D

    corr = H / N * 100
    acc = (H - I) / N * 100

    print("일치하는 글자들")
    print(ref)
    print(input)
    print("".join(reversed(search_word)))

    print("-------------------------------------------------------------------------------")
    print("WORD: corr={:.2f}%, acc={:.2f}% [H:{}, D:{}, S={}, I={}, N={}]".format(corr, acc, H, D, S, I, N))
    print("===============================================================================")

    return corr, acc, H, D, S, I, N
