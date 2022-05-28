#given an array find min amp you can get after changing up to 3 elem.

strarr = input().split(' ')
arr = []
for elem in strarr:
  arr.append(int(elem))

arr.sort()
lasti = len(arr)-1

option1 = arr[lasti-3]-arr[0]   # 3 from back
option2 = arr[lasti-2]-arr[1]   # 2 front 1 back
option3 = arr[lasti-1]-arr[2]   # 1 front 2 back
option4 = arr[lasti]-arr[3]     # 3 front

print(min(option1,option2,option3,option4))