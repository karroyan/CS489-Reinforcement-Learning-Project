## Reinforcement Learning Assignment 3
## Comparing Sarsa and Q-learning

import random
import numpy as np

np.random.seed(0)

def sarsa(trans, Q, reward, alpha, gamma, e):
    action = random.randint(0, 3)
    for times in range(1000):
        state = [3, 0]
        newstate = [1, 1]
        if (times > 0):
            maxa = -100000
            for a in range(4):
                if (Q[state[0]][state[1]][a] > maxa):
                    maxa = Q[state[0]][state[1]][a]
                    action = a
            p = []
            for a in range(4):
                if (a == action):
                    p.append(e / 4 + 1 - e)
                else:
                    p.append(e / 4)
            p = np.array(p)
            action = np.random.choice([0, 1, 2, 3], p=p.ravel())
        while (newstate[0] != 3 or newstate[1] != 11):
            newstate = trans[state[0]][state[1]][action]
            #if (newstate[0] == 3 and newstate[1] == 11): # reach the terminal
                #break
            maxa = -100000
            for a in range(4):
                if (Q[newstate[0]][newstate[1]][a] > maxa):
                    maxa = Q[newstate[0]][newstate[1]][a]
                    newaction = a
            p = []
            for a in range(4):
                if (a == newaction):
                    p.append(e / 4 + 1 - e)
                else:
                    p.append(e / 4)
            p = np.array(p)
            newaction = np.random.choice([0, 1, 2, 3], p = p.ravel())
            Q[state[0]][state[1]][action] = Q[state[0]][state[1]][action] + \
                                            alpha * (reward[state[0]][state[1]][action] + \
                                                     gamma * Q[newstate[0]][newstate[1]][newaction] - \
                                                     Q[state[0]][state[1]][action])
            state = newstate
            action = newaction

    return

def qlearning(trans, Q, reward, alpha, gamma, e):
    action = random.randint(0, 3)
    for times in range(5000):
        state = [3, 0]
        newstate = [1, 1]

        while (newstate[0] != 3 or newstate[1] != 11):
            maxa = -100000
            for a in range(4):
                if (Q[state[0]][state[1]][a] > maxa):
                    maxa = Q[state[0]][state[1]][a]
                    action = a
            p = []
            for a in range(4):
                if (a == action):
                    p.append(e / 4 + 1 - e)
                else:
                    p.append(e / 4)
            p = np.array(p)
            action = np.random.choice([0, 1, 2, 3], p=p.ravel())
            if (times == 0 and newstate[0] == 3 and newstate[1] == 0):
                action = random.randint(0, 3)
            newstate = trans[state[0]][state[1]][action]
            # if (newstate[0] == 3 and newstate[1] == 11): # reach the terminal
            # break
            maxa = -100000
            for a in range(4):
                if (Q[newstate[0]][newstate[1]][a] > maxa):
                    maxa = Q[newstate[0]][newstate[1]][a]
                    newaction = a
            Q[state[0]][state[1]][action] = Q[state[0]][state[1]][action] + \
                                            alpha * (reward[state[0]][state[1]][action] + \
                                                     gamma * Q[newstate[0]][newstate[1]][newaction] - \
                                                     Q[state[0]][state[1]][action])
            state = newstate
    return

def drawroute(Q):
    route = [[0 for i in range(12)] for j in range(4)]
    state = [3, 0]
    while (state[0] != 3 or state[1] != 11):
        maxa = -100000
        for a in range(4):
            if (Q[state[0]][state[1]][a] > maxa):
                maxa = Q[state[0]][state[1]][a]
                action = a
        if (state[0] == 0 and state[1] != 11):
            action = 2
        if (state[0] == 0 and state[1] == 11):
            action = 1
        route[state[0]][state[1]] = action + 1
        state = trans[state[0]][state[1]][action]
        #print(state[0], state[1])
        

    for i in range(4):
        for j in range(12):
            if route[i][j] == 0:
                print('0', end = '\t')
            elif route[i][j] == 1:
                print('<-', end  = '\t')
            elif route[i][j] == 2:
                print('.', end  = '\t')
            elif route[i][j] == 3:
                print('->', end  = '\t')
            else:
                print('^', end = '\t')
        print('')
        

# some parameters
e = 0.0005
gamma = 1
alpha = 0.5

# Initiate the policy. policy[i][j][k] means the possibility of [i, j] to go 'k'
# The sequence of the action is w, s, e, n
policy = [[[0.25 for i in range(4)]for j in range(12)]for k in range(4)]

# Initiate the transport matrix of all the grid
trans = [[[[k, j] for i in range(4)]for j in range(12)]for k in range(4)]
for i in range(4):
    for j in range(12):
        trans[i][j][0][1] = j - 1
        trans[i][j][1][0] = i + 1
        trans[i][j][2][1] = j + 1
        trans[i][j][3][0] = i - 1
for i in range(4):# west
    trans[i][0][0][1] = 0
trans[3][11][0][1] = 0
for i in range(10):# south
    trans[2][i + 1][1][0] = 3
    trans[2][i + 1][1][1] = 0
trans[3][0][1][0] = 3
trans[3][11][1][0] = 3
for i in range(4):# east
    trans[i][11][2][1] = 11
trans[3][0][2][1] = 0
for i in range(12):# north
    trans[0][i][3][0] = 0

# Initiate the reward for all the actions
reward = [[[-1 for i in range(4)]for j in range(12)]for k in range(4)]
# Set the cliff reward
for i in range(10):
    reward[2][i + 1][1] = -100
reward[3][0][2] = -100
reward[3][11][0] = -100
# Set the terminal reward
reward[2][11][1] = 100

# Initiate the Q-value
# Q[i][j][k] means Q((i, j), k)
Q = [[[0 for i in range(4)] for j in range(12)] for k in range(4)]

sarsa(trans, Q, reward, alpha, gamma, e)
print("The route of Sarsa")
drawroute(Q)
#for line in Q:
    #print(line)
###########################################################################################
# Initiate the policy. policy[i][j][k] means the possibility of [i, j] to go 'k'
# The sequence of the action is w, s, e, n
policy = [[[0.25 for i in range(4)]for j in range(12)]for k in range(4)]

# Initiate the transport matrix of all the grid
trans = [[[[k, j] for i in range(4)]for j in range(12)]for k in range(4)]
for i in range(4):
    for j in range(12):
        trans[i][j][0][1] = j - 1
        trans[i][j][1][0] = i + 1
        trans[i][j][2][1] = j + 1
        trans[i][j][3][0] = i - 1
for i in range(4):# west
    trans[i][0][0][1] = 0
trans[3][11][0][1] = 0
for i in range(10):# south
    trans[2][i + 1][1][0] = 3
    trans[2][i + 1][1][1] = 0
trans[3][0][1][0] = 3
trans[3][11][1][0] = 3
for i in range(4):# east
    trans[i][11][2][1] = 11
trans[3][0][2][1] = 0
for i in range(12):# north
    trans[0][i][3][0] = 0

# Initiate the reward for all the actions
reward = [[[-1 for i in range(4)]for j in range(12)]for k in range(4)]
# Set the cliff reward
for i in range(10):
    reward[2][i + 1][1] = -100
reward[3][0][2] = -100
reward[3][11][0] = -100
# Set the terminal reward
reward[2][11][1] = 100

# Initiate the Q-value
# Q[i][j][k] means Q((i, j), k)
Q = [[[0 for i in range(4)] for j in range(12)] for k in range(4)]

qlearning(trans, Q, reward, alpha, gamma, e)
print("\nThe route of Q-learning")
drawroute(Q)
#for line in Q:
    #print(line)


