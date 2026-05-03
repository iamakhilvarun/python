# Returns sum of even or odd natural numbers less than n.
# t = 'e' → even numbers, t = 'o' → odd numbers, else returns -1
def sum_eo(n,t):
   if t == "e":
       start = 2
   elif t == "o":
       start = 1
   else:
        return - 1
   return  sum(range(start,n,2))    

x= sum_eo(10,'e')
print(x)