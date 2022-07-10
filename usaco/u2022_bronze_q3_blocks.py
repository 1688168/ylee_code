#http://usaco.org/index.php?page=viewproblem2&cpid=1205
from functools import lru_cache
import os
import sys
from collections import Counter, defaultdict, deque
from pprint import pprint as pp

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
    #print("words: ", words)


arr = [x for x in range(4)] # 4 blocks

output=[]

def permutation(st, arr, res):
    if st >= len(arr):
        res.append(arr[:])
        return

    for jj in range(st, len(arr)):
        arr[st], arr[jj] = arr[jj], arr[st]
        permutation(st+1, arr[:], res)
        arr[st], arr[jj] = arr[jj], arr[st]

    return

permutation(0, arr, output)
#print(output)

blocks=[set(list(b1.rstrip())), set(list(b2.rstrip())), set(list(b3.rstrip())), set(list(b4.rstrip()))]
#pp(blocks)

for w in words:
    # given a word we need to try all permutation of the blocks
    #print(" check word: ", w)
    for permu in output:
        ii = 0
        found = True
        for c in w:
            if c not in blocks[permu[ii]]:
                found = False
                break
            ii += 1
        if found: break
    if found:
        print("YES")
    else:
        print("NO")



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
#createAllResults(blocks, 0, curr[:])
#pp(allPermu)
#print(" size: ", len(allPermu))

print(" ===== the Answer ===== ")
def loopAnswer(allPermu, words):
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

# build Trie
class MyTrie:
    def __init__(self):
        self.dict = defaultdict(MyTrie)
        return
    def __repr__(self):
        ii = 0
        dq = deque([self.dict])
        while dq:
            print(f"\n ===== level: {ii} ===== ")
            ii += 1
            sz=len(dq)
            while sz > 0:

                curr = dq.popleft()
                sz -= 1
                for kk, vv in curr.items():
                    print(kk, end=", ")
                    if vv.dict:
                        dq.append(vv.dict)
                print(" / ", end="")
        return ""




def trieAnswer(allPermu, words):
    aTrie = MyTrie()

    for w in allPermu:
        for ii in range(len(w)):
            itr = aTrie
            for c in w[ii:]:
                if c in itr.dict:
                    itr = itr.dict[c]
                else:
                    itr.dict[c] = MyTrie()
                    itr = itr.dict[c]

    print(" ===== the Trie ==== ")
    print(aTrie)
    print(" =================== ")
    for w in words:
        w = "".join(sorted(list(w)))
        found = True
        print(" checking w: ", w)
        itr = aTrie
        for c in w:
            # print(" ============ ")
            # print(" checking C: ", c)
            # pp(itr.dict.keys())
            # print(" ============ ")

            if itr and c not in itr.dict:
                print("NO")
                found = False
                break
            else:
                if itr is not None:
                    itr = itr.dict[c]


        if found:
            print("YES")
#loopAnswer(allPermu, words)
#trieAnswer(allPermu, words)

















