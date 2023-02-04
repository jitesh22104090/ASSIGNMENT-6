class Elements:
    def __init__(self, lst):
        self.lst = lst

    def triplets(self):
        new_lst = []
        for i in self.lst:
            for j in self.lst:
                for k in self.lst:
                    if (i+j+k==0):
                        if ([i, j, k] in new_lst) or ([i, k, j] in new_lst) or ([k, i, j] in new_lst) or ([j, i, k] in new_lst) or ([j, k, i] in new_lst) or ([k, j, i] in new_lst):
                            continue
                        else:
                            new_lst.append([i, j, k])
                    else:
                        continue
        return new_lst

list1 = [-25, -10, -7, -3, 2, 4, 8, 10]

a = Elements(list1).triplets()
print(a)