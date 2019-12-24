## reinforcement
## MC
import random

def generateepisode(V, policy):
    for oristate in range(15):
        if oristate == 0:
            continue
        for times in range(10000):
            state = oristate
            S = []
            S.append((state, 0))
            for i in range(100):
                action = random.randint(0, 3)
                nextstate = A[action][statepos[state][0]][statepos[state][1]]
                S.append((nextstate, -1))
                #print(nextstate)
                if nextstate == 0:
                    break
                if nextstate == 15:
                    break
                state = nextstate
            #print(S)
            seperate_episode = set([eps[0] for eps in S])

            for s_eps in seperate_episode:
                for i, x in enumerate(S):
                    if x[0] == s_eps:
                        first_visit_pos = i
                G = sum([e[1] for e in S[first_visit_pos + 1:]])

                return_sum[s_eps] += G
                #print(s_eps, G)
                return_count[s_eps] += 1.0

    for state in range(16):
        if (return_count[state] != 0):
            V[statepos[state][0]][statepos[state][1]] = return_sum[state] / return_count[state]
        
            


policy = [[[0.25 for i in range(4)]for j in range(4)]for k in range(4)]
V = [[0 for i in range(4)]for j in range(4)]
A = [[[0, 1, 2, 3], [0, 1, 2, 3], [4, 5, 6, 7], [8, 9, 10, 11]], [[1, 2, 3, 3], [5, 6, 7, 7], [9, 10, 11, 11], [13, 14, 15, 15]], [[4, 5, 6, 7], [8, 9, 10, 11], [12, 13, 14, 15], [12, 13, 14, 15]], [[0, 0, 1, 2], [4, 4, 5, 6], [8, 8, 9, 10], [12, 12, 13, 14]]]
return_sum = [0 for i in range(16)]
return_count = [0 for i in range(16)]
statepos = [[0, 0], [0, 1], [0, 2], [0, 3], [1, 0], [1, 1], [1, 2], [1, 3], [2, 0], [2, 1], [2, 2], [2, 3], [3, 0], [3, 1], [3, 2], [3, 3]]

generateepisode(V, policy)
for line in V:
    print(line)
