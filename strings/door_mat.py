"""Size: 7 x 21
    ---------.|.---------
    ------.|..|..|.------
    ---.|..|..|..|..|.---
    -------WELCOME-------
    ---.|..|..|..|..|.---
    ------.|..|..|.------
    ---------.|.---------

    Size: 11 x 33
    ---------------.|.---------------
    ------------.|..|..|.------------
    ---------.|..|..|..|..|.---------
    ------.|..|..|..|..|..|..|.------
    ---.|..|..|..|..|..|..|..|..|.---
    -------------WELCOME-------------
    ---.|..|..|..|..|..|..|..|..|.---
    ------.|..|..|..|..|..|..|.------
    ---------.|..|..|..|..|.---------
    ------------.|..|..|.------------
    ---------------.|.---------------"""
ine=list(map(int,input().split()))#this must be odd
S="WELCOME"
M=line[0]
N=line[1]
pattern='.|.'
why=M//2
for i in range(M//2):
    p=(2*i+1)*pattern
    print(p.center(N,'-'))
print(S.center(N,'-'))
for i in range(M//2):
    p=(2*(why-i-1)+1)*pattern
    print(p.center(N,'-'))
