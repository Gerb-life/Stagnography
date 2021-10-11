# printing ascii val is ord(whatever)
# n = ascii value of each character
# k = most significant digit of n
# l = middle digit of n
with open ('input.txt') as f:
   for line in f:
       i = 0

       while i < len(line):

            n = ord(line[i])
            if n < 100 :

                n = n * 10
                print(n)

                i += 1
            else:
                print(n)
                i +=1