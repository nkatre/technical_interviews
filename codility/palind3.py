#Write a function
#def solution(S)
#that, given a string S of length N letters, returns the number of palindromic slices of S. The function should return −1 if this number is greater than 100,000,000.
#For example, for string S = baababa the function should return 6, because exactly six of its slices are palindromic; namely: (0, 3), (1, 2), (2, 4), (2, 6), (3, 5), (4, #6).
def solution(A):
    list=[]
    for item in A:
        list.append("#")
        list.append(item)
    list.append("#")
    count=[0 for i in range(0,len(list))]
    count2=[0 for i in range(0,len(list))]
    #print len(count),len(list)
    left=0
    right=0
    centre=0
    for i in range(2,len(list)):
        mirror=(2*centre)-i
        if(right>i):
            count2[i]=min(right-i,count2[mirror])
            #print "start", i+1+count2[i],i-1-count2[i]
        if(((i+1+count2[i])<len(list)-1) & ((i-1-count2[i])>=0)):
            while(list[i+1+count2[i]]==list[i-1-count2[i]]):
                #print list[i+1+count2[i]],list[i-1-count2[i]]
                count2[i]+=1
                #print i+1+count2[i],i-1-count2[i]
                if(((i+1+count2[i])>len(list)-1) or ((i-1-count2[i])<0)):
                    #print "here"
                    break
                #print list[(i-1-count2[i]),(i+1+count2[i])]
        if(i+count2[i]>right):
            centre=i
            right=i+count2[i]
    new_count=[x/2 for x in count2]
    print count2
    return sum( new_count)
if __name__ == '__main__':
    A="abababbbabbbaba"
    B=" baababa"
    print solution(B)
