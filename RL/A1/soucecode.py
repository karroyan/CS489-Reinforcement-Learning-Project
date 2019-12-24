# -*- coding: UTF-8 -*-
MINX = -10000

def valueUpdateOnce(V, policy):
    # update the v to Vs
    delta = 0
    v = []
    for line in V:
        tmpv = []
        for Vs in line:
            tmpv.append(Vs)
        v.append(tmpv)


    #calculate new V
    for i in range(4):
        for j in range(4):
            if (i == 0 and j == 0 or (i == 3 and j == 3)):
                V[i][j] = 0.0
                continue
            im = i - 1
            ip = i + 1
            jm = j - 1
            jp = j + 1
            if (im < 0): im = 0
            if (ip > 3): ip = 3
            if (jm < 0): jm = 0
            if (jp > 3): jp = 3
            V[i][j] = -1.0 + v[im][j] * policy[2][i][j] + v[ip][j] * policy[3][i][j] + v[i][jm] * policy[0][i][j] + v[i][jp] * policy[1][i][j]
            delta = delta + abs(V[i][j] - v[i][j])
    #print("v")
    #print(v)
    #print(V)
    if (delta < 0.001):
        return 1
    else:
        return 0


def valueUpdate(V, policy):
    # update the v to Vs
    delta = 2
    while (delta > 0.001):
        delta = 0
        v = []
        for line in V:
            tmpv = []
            for Vs in line:
                tmpv.append(Vs)
            v.append(tmpv)


        #calculate new V
        for i in range(4):
            for j in range(4):
                if (i == 0 and j == 0 or (i == 3 and j == 3)):
                    V[i][j] = 0.0
                    continue
                im = i - 1
                ip = i + 1
                jm = j - 1
                jp = j + 1
                if (im < 0): im = 0
                if (ip > 3): ip = 3
                if (jm < 0): jm = 0
                if (jp > 3): jp = 3
                V[i][j] = -1.0 + v[im][j] * policy[2][i][j] + v[ip][j] * policy[3][i][j] + v[i][jm] * policy[0][i][j] + v[i][jp] * policy[1][i][j]
                delta = delta + abs(V[i][j] - v[i][j])
    for line in V:
        print(line)

def generatePolicy(V, policy):
    p = []
    for i in range(4):
        for j in range(4):
            if (i == 0 and j == 0 or i == 3 and j == 3):                
                continue
            im = i - 1
            ip = i + 1
            jm = j - 1
            jp = j + 1
            if (jm < 0):
                west = MINX
            else:
                west = V[i][jm]
            if (jp > 3):
                east = MINX
            else:
                east = V[i][jp]
            if (im < 0):
                north = MINX
            else:
                north = V[im][j]
            if (ip > 3):
                south = MINX
            else:
                south = V[ip][j]
            
            maxp = max(west, east, north, south)
            count = 0
            if (abs(maxp - west) < 0.0001):
                count = count + 1
            if (abs(maxp - east) < 0.0001):
                count = count + 1
            if (abs(maxp - north) < 0.0001):
                count = count + 1
            if (abs(maxp - south) < 0.0001):
                count = count + 1
            if (abs(maxp - west) < 0.0001):
                policy[0][i][j] = 1.0 / count
            else :
                policy[0][i][j] = 0.0
            if (abs(maxp - east) < 0.0001):
                policy[1][i][j] = 1.0 / count
            else :
                policy[1][i][j] = 0.0
            if (abs(maxp - north) < 0.0001):
                policy[2][i][j] = 1.0 / count
            else :
                policy[2][i][j] = 0.0
            if (abs(maxp - south) < 0.0001):
                policy[3][i][j] = 1.0 / count
            else :
                policy[3][i][j] = 0.0
                

V = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
policy = [[[0.25 for i in range(4)] for j in range(4)] for k in range(4)]

for i in range(4):
    policy[i][0][0] = 0.0
    policy[i][3][3] = 0.0

print("Using policy iteration:")
print("The matrix of value is:")
valueUpdate(V, policy)
print("The matrix of policy is:")
generatePolicy(V, policy)
print("The probability of going west in the optimal policy:")
for line in policy[0]:
    print(line)
print("goint east:")
for line in policy[1]:
    print(line)
print("goint north:")
for line in policy[2]:
    print(line)
print("goint south:")
for line in policy[3]:
    print(line)

print("")
V = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
policy = [[[0.25 for i in range(4)] for j in range(4)] for k in range(4)]

for i in range(4):
    policy[i][0][0] = 0.0
    policy[i][3][3] = 0.0
print("Using value iteration:")
for i in range(10):
    valueUpdateOnce(V, policy)
    generatePolicy(V, policy)
    #print(policy)
print("The probability of going west in the optimal policy:")
for line in policy[0]:
    print(line)
print("goint east:")
for line in policy[1]:
    print(line)
print("goint north:")
for line in policy[2]:
    print(line)
print("goint south:")
for line in policy[3]:
    print(line)

            
