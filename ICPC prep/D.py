import io, os
input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline

n = int(input().decode())
line = []
for i in range(n):
    line.append(int(input().decode()))

# fixing start and end
start, end = 0, n-1
while start < n-1:
    if line[start] > line[start+1]: break
    start += 1

while end > start: 
    if line[end-1] < line[end]: break 
    end -=1

print(start, end)
if(end == start): 
    print(n-1)
    exit(0)

ans = 0
# if(start+2 == end): #one away redundant?
#     if(line[end]>line[end-1]): print(n)
#     print(n-1)
#     exit(0)

while start+1 < end: #verify condition
    for i in range(start+2, end+1): #verify condition
        if line[i] > line[start]:
            ans += 1
            start = i
            break
    #change start and end if it's fine
    for j in range(end-2, start, -1):
        if line[j] > line[end]:
            ans += 1
            end = j
            break
        

print(ans + n-1)


#     if line[end-1] < line[end]: end -= 1
#     print("start:", start, "end:", end)

# while start < end:
#     start_h = line[start]
#     end_h = line[end]
    
#     if start_h < line[start+ 1]:
#         start += 1
#         continue
#     if end_h < line[end-1]:
#         end -= 1
#         continue
    
#     broken = False 
#     for i in range(start+1, end):
#         if line[i] > start_h:
#             answer += 1
#             print(i, start)
#             start = i
#             broken = True
#             break
    
#     if broken:
#         continue

#     for j in range(end-1, start):
#         if line[j] > end_h:
#             answer +=1
#             print(j, end)
#             end = j
#             broke = True
#             break
    
#     if start != end -1:
#         answer += 1
#     start += 1

# print(answer + n-1)
