class Sol:
    x=0
    def kth_largest_element(self,nums,k):
        self.x+=1
        idx = len(nums) - k
        if len(nums)>1:
            less,equal,greater=[],[],[]
            pivot=nums[0]
            for num in nums:
                if num>pivot:
                    greater.append(num)
                if num<pivot:
                    less.append(num)
                if num==pivot:
                    equal.append(num)
            if idx<len(less):
                print(less)
                return self.kth_largest_element(less,k)
            elif idx<len(less)+len(equal):
                print(True)
                print(equal)
                return pivot
            else:
                print(greater)
                return self.kth_largest_element(greater,k-self.x)
        else:
            return nums[0]



if __name__ == '__main__':
    p=Sol()
    print(p.kth_largest_element([6,2,1,4,3,5],3))
