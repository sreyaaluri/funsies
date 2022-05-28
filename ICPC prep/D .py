import io, os
input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline

n = int(input().decode())
line = []
for i in range(n):
    line.append(int(input().decode()))

answer = 0

start, end = 0, n-1

while start < end:
    #print("start:", start, "end:", end)
    start_h = line[start]
    end_h = line[end]
    
    if start_h < line[start+ 1]:
        start += 1
        continue
    if end_h < line[end-1]:
        end -= 1
        continue
    
    broken = False 
    for i in range(start+1, end):
        if line[i] > start_h:
            answer += 1
     #       print(i, start)
            start = i
            broken = True
            break
    
    if broken:
        continue

    for j in range(end-1, start, -1):
        if line[j] > end_h:
            answer +=1
      #      print(j, end)
            end = j
            broke = True
            break
    
    if broken:
        continue
    
    if start != end -1:
        answer += 1
    start += 1

print(answer + n-1)
