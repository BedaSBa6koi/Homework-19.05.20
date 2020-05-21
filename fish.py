def solution(A, B):
    dstrm = []
    ustrm = []
    counter = 0
    n = len(A)
    for i in range(n):
        if B[i] == 0:
            ustrm.append(A[i])
        elif B[i] == 1:
            dstrm.append(A[i])
        if len(ustrm) > 0 and len(dstrm) == 0:
            counter += len(ustrm)
            ustrm.clear()

        while len(dstrm) > 0 and len(ustrm) > 0:
            if dstrm[-1] > ustrm[-1]:
                ustrm.pop()
            elif ustrm[-1] > dstrm[-1]:
                dstrm.pop()

    return len(dstrm) + len(ustrm) + counter
    pass