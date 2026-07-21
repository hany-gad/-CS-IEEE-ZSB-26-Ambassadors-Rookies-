t = 1nt (input())
for i in range(t):
  n=int(input())
  s=input()
  balloons=0
  solved=[]
  for char in s :
    balloons +=1
    if char not in solved :
      ballons+=1
      solved.append(char)
   print(balloons)