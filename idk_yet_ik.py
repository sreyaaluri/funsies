# https://www.reddit.com/r/math/comments/32opae/next_level_cheryl_birthday_question/cqd7sus/
# https://alexanderell.is/posts/numbers-game/ explains the concept really well

# pairs = [(i,j) for i in range(1,100) for j in range(1,100)]
sums = {i : set() for i in range (2,199)} # min sum 1+1=2; max sum 99+99=198         dict w/ sum : set of pairs that give that sum
products = {i : set() for i in range(1,9802)} # min prod 1*1=1; max prod 99*99=9801  dict w/ product : set of pairs that give that product
known = False

for i in range(1,100):
  for j in range(i,100):
    sums[i+j].add((i,j))
    products[i*j].add((i,j))

peter = True # Peter = 1 Sandy = 0 Start with Peter
while(not known):
  # setup
  if(peter): print("Peter: ", end="")
  else: print("Sandy: ", end="")

  # parse input
  response = input()
  if(response == "I know the numbers."): # end condition
    known = True
  elif(response == "I don't know the numbers."):
    known = False
  else:
    print("invalid input, please respond with either \"I know the numbers.\" or \"I don't know the numbers.\"")
    continue # turn does not end due to invalid input
  
  # take appropriate action
  if(peter):
    for prod in products:
      pairs = products[prod]
      if(len(pairs) == 1):
        pair = pairs.pop()
        if(known):
          print(pair)
          # break
        else:             # delete pair from sum breakdown
          sums[pair[0] + pair[1]].discard(pair)
  else:
    for sum in sums:
      pairs = sums[sum]
      if(len(pairs) == 1):
        pair = pairs.pop()
        if(known):
          print(pair)
          # break
        else:             # delete pair from product breakdown
          products[pair[0] * pair[1]].discard(pair)

  # successfully end turn
  peter = (peter+1)%2
