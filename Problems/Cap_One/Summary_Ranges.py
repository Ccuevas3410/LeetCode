


#[0,1,4,5,7]   ->> [ "0->1", "4->5", "7"]



def summaryRanges(nums):

        if not nums:
            return 0


        newSet = set(nums)
        answer = []
        i=0


        while i < len(nums):
            current = nums[i]
            count = 0

            while current+1 in newSet:
                current += 1 
                count +=1 

            if count == 0:
                answer.append(str(current))
            else:
                answer.append(str(nums[i]) + "->" + str(current))

            i += count + 1

        return answer

        



print(summaryRanges([0,1,2,4,5,7,8]))
print(summaryRanges([0,1,4,5,7,9]))
print(summaryRanges([]))