A=3,5
B=7,8
C=12,7
D=10,6
P=10,6

bx= B[0] - A[0]
by= B[1] - A[1]
cx= C[0] - A[0]
cy= C[1] - A[1]
x = P[0] - A[0]
y = P[1] - A[1]

d=bx*cy-cx*by
WA=(x*(by-cy)+y*(cx-bx)+bx*cy-cx*by)/d
WB=(x*cy-y*cx)/d
WC=(y*bx-x*by)/d

if (0<=WA<=1) and (0<=WB<=1) and (0<=WC<=1) :
	print("Aferin")
else:
	print("Karavana")

print(WA,WB,WC)