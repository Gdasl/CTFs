import array
import re

##constants
Output = 16
Space = 100000
Rounds = 100000



def compute1(done):
    frames = ["\033[6A\r               X \n                  \n               O  \n             Y/|\\Z\n               |\n              / \\\n",
		"\033[6A\r                 \n             X    \n             Y_O  \n               |\\Z\n               |\n              / \\\n",
		"\033[6A\r                 \n             XY   \n              (O  \n               |\\Z\n               |\n              / \\\n",
		"\033[6A\r              Y  \n                  \n             X_O  \n               |\\Z\n               |\n              / \\\n",
		"\033[6A\r               Y \n                  \n               O  \n             X/|\\Z\n               |\n              / \\\n",
		"\033[6A\r                 \n                 Y\n               O_Z\n             X/|  \n               |\n              / \\\n",
		"\033[6A\r                 \n                ZY\n               O) \n             X/|  \n               |\n              / \\\n",
		"\033[6A\r                Z\n                  \n               O_Y\n             X/|  \n               |\n              / \\\n",]



def panicIfInvalid(s):
    r = re.compile("^[a-zA-Z0-9]{26}$")
    if r.match(s) is not None:
        pass
    else:
        raise Exception('Invalid inpuit')


def compute2(data, done):
    pass
    r = ''
    state = [0]*Space
    j = 0
    i = 0
    for i in range(Space):
        state[i] = i

    for t in range(0,Space%Rounds):
        i = (i+1) % Space
        j = (j + state[i] + int(data[i%len(data)])) % Space
        state[i], state[j] = state[j],state[i]

    o = [0]*Output
    for t in range(0,Output):
        i = (i+1)%Space
        j = state[(state[i] + state[j])%Space]
        o[t] = j&0xff

    r = ''.join([hex(i)[2:] for i in o])
    return r
    


    
inpt = 'a'*26
panicIfInvalid(inpt)

done = False
compute1(done)
h = compute2(array.array('B', inpt), done)

s = [0]*len(inpt)
r = compute3(s)
