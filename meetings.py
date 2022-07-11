# https://leetcode.com/problems/meeting-rooms/submissions/

def canAttendMeetings(intervals) -> bool:
  intervals.sort()
  for i in range(1, len(intervals)):
    if intervals[i-1][1] > intervals[i][0]:
      return False
  return True

def main():
  intervals = [[0,30],[5,10],[15,20]]
  print(canAttendMeetings(intervals))

if __name__ == '__main__':
  main()