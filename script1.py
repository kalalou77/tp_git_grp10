#Script pour afficher les nombres premiers de 1 à 1 000 000
min = 1
max = 1000000
for n in range(min,max + 1):
   if n > 1:
       for i in range(2,n):
           if (n % i) == 0:
               break
       else:
           print(n)
