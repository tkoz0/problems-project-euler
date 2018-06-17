import math

balltypes = 7
ballcount = 10 # how many of each type
ballsdrawn = 20

bcf = math.factorial(ballcount)
probabilities = [0]*(balltypes+1)
def recurse(x,s): # enumerate every x_i set (count of each ball type)
    global balltypes, ballcount, ballsdrawn, probabilities, bcf
    if len(x) == balltypes: # configuration of amount of each ball
        if s != ballsdrawn: return
        balls = sum(1 for i in x if i != 0) # number of balls
        # 10!/(10-x_i)! * ... / 70*...*51 (ignore) * x_i!... (arrangements)
        fprod = math.factorial(balls)
        for i in x: fprod *= bcf // math.factorial(ballcount-i)
        probabilities[balls] += fprod # count arrangements of the balls
        return
    for i in range(ballcount+1): # select next ball
        if s > ballsdrawn: break
        recurse(x+[i],s)
        s += 1
recurse([],0)

psum = sum(probabilities)
for i,p in enumerate(probabilities): probabilities[i] = p/psum
print(probabilities)

expected = 0
for i in range(1,balltypes+1):
    expected += i * probabilities[i]
print(expected)
