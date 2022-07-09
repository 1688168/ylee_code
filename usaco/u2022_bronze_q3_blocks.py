from functools import lru_cache
import os
import sys
from collections import Counter

input_file = os.path.join(os.getcwd(), "u2022_bronze_q3_blocks_input.txt")

# with open(input_file, mode='r', encoding="utf-8") as f:
#     line = f.readline()
#     while line:
#         print(line, end='')
#         line = f.readline()

with open(input_file, mode='r', encoding="utf-8") as f:
    numOfNums = int(f.readline())
    print(" numOfNums: ", numOfNums)
    b1 = f.readline()
    b2 = f.readline()
    b3 = f.readline()
    b4 = f.readline()
    blocks=[b1, b2, b3, b4]
    words = [f.readline().rstrip() for ii in range(numOfNums)]
    print("b1: ", b1, end="")
    print("b2: ", b2, end="")
    print("b3: ", b3, end="")
    print("b4: ", b4, end="")
    print("words: ", words)

# produce all permutations
allPermu = set()

def createAllResults(blocks, iBlock, curr):

    if iBlock >= 4:
        res = "".join(sorted(curr))
        #print(res)
        allPermu.add(res)

        return

    for jj in range(6):
        curr.append(blocks[iBlock][jj])
        createAllResults(blocks, iBlock+1, curr[:])
        curr.pop()

    return





curr = []
createAllResults(blocks, 0, curr[:])
print("all: ", allPermu)

print(" ===== the Answer ===== ")
for w in words:
    cw = Counter(list(w))

    for dw in allPermu:
        found = True
        cdw = Counter(list(dw))
        for kcw, vcw in cw.items():
            if kcw not in cdw or vcw > cdw[kcw]:
                found = False
                break

        if found: break

    if found:
        print("YES")
    else:
        print("NO")



















