# Elementary

> Elementary, my dear Watson.

# Solving

Simple key check, only there are 800+ functions. The obvious way here was to use angr to do it for us. Using ida we could identify the starting point as well as the target and the place to avoid(success and fail messages respectively. I had a typo in my script but the below actually works.

```python
import angr
import claripy

# angr uses 0x400000 as base address for PIE executables

START = 0x40071a
FIND  = 0x40077f
AVOID = [0x400786] 
BUF_LEN = 104


def char(state, c):
    return state.solver.And(c <= '~', c >= ' ')


def main():
    p = angr.Project("elementary")

    flag = claripy.BVS('flag', BUF_LEN * 8)
    state = p.factory.blank_state(addr=START, stdin=flag)

    for c in flag.chop(8):
        state.solver.add(char(state, c))

    ex = p.factory.simulation_manager(state)
    ex.use_technique(angr.exploration_techniques.Explorer(find=FIND, avoid=AVOID))

    ex.run()

    return ex.found[0].posix.dumps(0).decode("utf-8")


if __name__ == '__main__':
    print("flag: {}".format(main()))
