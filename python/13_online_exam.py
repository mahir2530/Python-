r=0
w=0
at=0
ut=0
m=0

print("Que.1 : ")
print("\n5 * 2 = ?")
print("(A) 8\t\t(B) 10\t\t(C) 12\t\t(D) skip")
ch = input("\nEnter Your Choice : ")
if ch =='D' :
    ut = ut + 1
    m = m + 0
elif ch=='B':
    r = r + 1
    at = at + 1
    m = m + 4
elif ch=='A':
    w = w + 1
    at = at + 1
    m = m - 2
else:
    w = w + 1
    at = at + 1
    m = m - 2

print("\nQue.2 : ")
print("\n3 * 2 = ?")
print("(A) 6\t\t(B) 1\t\t(C) 2\t\t(D) skip")
ch = input("\nEnter Your Choice : ")
if ch =='D' :
    ut = ut + 1
    m = m + 0
elif ch=='B':
    w = w + 1
    at = at + 1
    m = m - 2
elif ch=='A':
    r = r + 1
    at = at + 1
    m = m + 4
else:
    w = w + 1
    at = at + 1
    m = m - 2

print("\nQue.3 : ")
print("\n50 / 10 = ?")
print("(A) 500\t\t(B) 1\t\t(C) 5\t\t(D) skip")
ch = input("\nEnter Your Choice : ")
if ch =='D' :
    ut = ut + 1
    m = m + 0
elif ch=='B':
    w = w + 1
    at = at + 1
    m = m - 2
elif ch=='A':
    w = w + 1
    at = at + 1
    m = m - 2
else:
    r = r + 1
    at = at + 1
    m = m + 4

print("\nQue.4 : ")
print("\n15 * 3 = ?")
print("(A) 5\t\t(B) 40\t\t(C) 45\t\t(D) skip")
ch = input("\nEnter Your Choice : ")
if ch =='D' :
    ut = ut + 1
    m = m + 0
elif ch=='B':
    w = w + 1
    at = at + 1
    m = m - 2
elif ch=='A':
    w = w + 1
    at = at + 1
    m = m - 2
else:
    r = r + 1
    at = at + 1
    m = m + 4

print("\nQue.5 : ")
print("\n(4 * 2) / 2 = ?")
print("(A) 4\t\t(B) 16\t\t(C) 10\t\t(D) skip")
ch = input("\nEnter Your Choice : ")
if ch =='D' :
    ut = ut + 1
    m = m + 0
elif ch=='B':
    w = w + 1
    at = at + 1
    m = m - 2
elif ch=='A':
    r = r + 1
    at = at + 1
    m = m + 4
else:
    w = w + 1
    at = at + 1
    m = m - 2

print("\n\nRight Answer : ",r)
print("Wrong Answer : ",w)
print("Attempted Answer : ",at)
print("Unattempted Answer : ",ut)
print("Marks : ",m)