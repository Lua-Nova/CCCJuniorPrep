#ccc 01 j1
n = int(input())

for x in range(n):
  if x < n/2:
    print( '*'*(2*x+1) + (2*(n-2*x)-2)*' ' + '*'*(2*x+1))
  elif x > n/2:
    print ('*'*(2*(n-x)+1) + (2*(n-2*(n-x))-2)*' ' + '*'*(2*(n-x)+1))
  else:
    print ('*'**n)
  
print ('*' + ' '*(2*n-2) + '*')