## reinforcement
## TD0
import random

def generateepisode(V, policy):
    for oristate in range(15):
        if oristate == 0:
            continue
        for times in range(10000):
            state = oristate
            S = []
            S.append((state, 0))
            nextstate = 1
            while (nextstate != 0 and nextstate != 15):
                action = random.randint(0, 3)
                nextstate = A[action][statepos[state][0]][statepos[state][1]]
                V[statepos[state][0]][statepos[state][1]] = \
                    V[statepos[state][0]][statepos[state][1]] + \
                    alpha * (-1 + V[statepos[nextstate][0]][statepos[nextstate][1]] - \
                    V[statepos[state][0]][statepos[state][1]])

                state = nextstate

policy = [[[0.25 for i in range(4)]for j in range(4)]for k in range(4)]
V = [[0 for i in range(4)]for j in range(4)]
A = [[[0, 1, 2, 3], [0, 1, 2, 3], [4, 5, 6, 7], [8, 9, 10, 11]], [[1, 2, 3, 3], [5, 6, 7, 7], [9, 10, 11, 11], [13, 14, 15, 15]], [[4, 5, 6, 7], [8, 9, 10, 11], [12, 13, 14, 15], [12, 13, 14, 15]], [[0, 0, 1, 2], [4, 4, 5, 6], [8, 8, 9, 10], [12, 12, 13, 14]]]
return_sum = [0 for i in range(16)]
return_count = [0 for i in range(16)]
statepos = [[0, 0], [0, 1], [0, 2], [0, 3], [1, 0], [1, 1], [1, 2], [1, 3], [2, 0], [2, 1], [2, 2], [2, 3], [3, 0], [3, 1], [3, 2], [3, 3]]
alpha = 0.5

generateepisode(V, policy)
for line in V:
    print(line)
