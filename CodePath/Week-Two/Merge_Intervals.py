#Prompt
#Given a collection of intervals, merge all overlapping intervals.

#Key Actions
#merge

#What is the input?
# A list of lists
#What is the data type?
#A list
#What is the output?
#a new list





               #new list is equal to first num of first list and second num of next list.
            #else new list is equal to same sublist
   
   

   


#THIS WORKS, EXCEPT FOR INPUT LIKE 
##
# def merge(intervals):
#   if len(intervals) <= 1:
#             return intervals
        
#         newList = []


#         i=1

#         ##PROBLEM WITH THIS IS WE CANNOT CONTROL 
#         while i<len(intervals):

#            if intervals[i][0] <= intervals[i-1][1]:
#              if intervals[i][0] < intervals[i-1][0]:
#                 newList.append([intervals[i][0],intervals[i][1]])
#                 i+=1
#              else:
#                 newList.append([intervals[i-1][0],intervals[i][1]])
#                 i+=2
#            else:
#                  newList.append((intervals[i-1][0], intervals[i-1][1]))
#                  newList.append((intervals[i][0], intervals[i][1]))
#                  i+=1




#HOWEVER, We can use a HEAP to get max/min out of 2 sublist and make a new sublist if needed be.

#
#[[1,3],[2,6],[8,10],[15,18]]
interval_list= [[1,4],[0,1]]
def merge(intervals):
  intervals.sort()
  i=1

  while i < len(intervals):
      if intervals[i][0] <= intervals[i-1][1]:
          intervals[i-1][0] = min(intervals[i-1][0],intervals[i][0])
          intervals[i-1][1] = max(intervals[i-1][1],intervals[i][1])
          intervals.pop(i)
      else:
        i+=1
  return intervals




print (merge(interval_list))