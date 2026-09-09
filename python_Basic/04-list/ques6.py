def arv(nums1,nums2):
    new_list=[]
    n=len(nums1)
    for i in range(0,n):
        total=nums1[i]+nums2[i]
        new_list.append(total)
    return new_list

nums1=[1,2,3,4,5,6]
nums2=[3,2,3,4,5,6]

print(arv(nums1,nums2))