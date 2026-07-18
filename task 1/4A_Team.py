n =int(input ())
Solv_Prob=0
for i in range(n):
  line=input().split() 
  peta=int(line[0])
  vasya=int(line[1])
  tony=int(line[2])
  num=[peta, vasya,tony]
  if sum(num)>=2:
    Solv_Prob+=1
print(Solv_Prob)
