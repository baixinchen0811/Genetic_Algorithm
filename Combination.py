def combinations(array,cSpace,index,m):
    #不可重复取组合生成器
    if(m==0):
        for i in range(cSpace.__len__()):
            print(cSpace[i],end='')
        print(' ',end='')
        return
    for i in range(array.__len__()):
        cSpace[index] = array[i];
        if index==0:
            combinations(array=array,cSpace=cSpace,index=index+1,m=m-1)
        elif index>0:
            cIndex=array.index(cSpace[index])
            pIndex=array.index(cSpace[index-1])
            if cIndex>pIndex:
                combinations(array=array,cSpace=cSpace,index=index+1,m=m-1)



def combinations_with_replacement(array,cSpace,index,m):
    #可重复取组合生成器
    if(m==0):
        for i in range(cSpace.__len__()):
            print(cSpace[i],end='')
        print(' ',end='')
        return
    for i in range(array.__len__()):
        cSpace[index] = array[i];
        if index==0:
            combinations_with_replacement(array=array,cSpace=cSpace,index=index+1,m=m-1)
        elif index>0:
            cIndex=array.index(cSpace[index])
            pIndex=array.index(cSpace[index-1])
            if cIndex>=pIndex:
                combinations_with_replacement(array=array,cSpace=cSpace,index=index+1,m=m-1)



if __name__ == '__main__':
    array=list('abcd')#元素
    m=3#所取元素个数
    cSpace=list(range(m))
    combinations(array=array,cSpace=cSpace,index=0,m=m)
    print('')
    combinations_with_replacement(array=array,cSpace=cSpace,index=0,m=m)