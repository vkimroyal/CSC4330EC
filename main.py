from lex import Lexical
from rda import RDA

# Test Case 1: No Error
print("Test Case 1\n")

file = open("testcase1.txt", "rt")
data = file.read()

lex1 = data.split()
tokenStr1 = Lexical(lex1)
tk1 = tokenStr1.checkLex()
print(tk1)
tst1 = RDA(tk1)

print("\n-----\n")

# Test Case 2: No Error
print("Test Case 2\n")

file = open("testcase2.txt", "rt")
data = file.read()

lex2 = data.split()
tokenStr2 = Lexical(lex2)
tk2 = tokenStr2.checkLex()
print(tk2)
tst2 = RDA(tk2)

print("\n-----\n")

# Test Case 3: Lexical Error
print("Test Case 3\n")

file = open("testcase3.txt", "rt")
data = file.read()

lex3 = data.split()
tokenStr3 = Lexical(lex3)
tk3 = tokenStr3.checkLex()
print(tk3)
tst3 = RDA(tk3)

print("\n-----\n")

# Test Case 4: Syntax Error

print("Test Case 4\n")

file = open("testcase4.txt", "rt")
data = file.read()

lex4 = data.split()
tokenStr4 = Lexical(lex4)
tk4 = tokenStr4.checkLex()
print(tk4)
tst4 = RDA(tk4)