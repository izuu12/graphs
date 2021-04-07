'''
calculates the sum of the masses of elements on the list with the current setting,
which have changed places so that they are in the place indicated on the list with the target setting

'''
class Zoo:
    def __init__(self,nr,m,a,b):
        '''
        :param nr: number of elephants
        :param m: list with the mass elephant
        :param a: list with the current position
        :param b: list with the proposed item
        '''
        self.nr=nr
        self.m=m
        self.a=a
        self.b =b
    def __getitem__(self, tup):
        '''
        :param tup: index - item number in the list and typ - a number representing a mass, current or target list
        :return: StopIteration or list item
        '''
        index, typ =tup
        if index<=self.nr:
            if typ==1:
                return self.m[index]
            if typ == 2:
                return self.a[index]
            if typ==3:
                return self.b[index]
        else:
            raise StopIteration
    @classmethod
    def get_file(cls, path):
        '''
        returns class object based on the contents of the input file
        :param path: path to the input file
        :return: class object
        '''
        with open(path, 'r') as file:
            zoo =[]
            for nr, line in enumerate(file):
                for x in range(0,4):
                    if nr==x:
                        zoo.append([int(l) for l in line.strip().split(' ')])
        return Zoo(zoo[0][0], zoo[1], zoo[2], zoo[3])

    def p(self,bi):
        '''
        the method compares the elements in the current list with the target list,
        when the value of the element is equal, it returns the value of the number from the target list
        :param bi: number on the expected list
        :return: number of e
        '''
        for nr,a in enumerate(iter(self.a)):
            if a==bi:
                b =self[nr,3]
                break
        return b,nr
'''
sum_all - Minimum mass parameters for the cycle and 
the minimum mass for all cycles - min_all_gl,
the number of cycles - len_c
the sum of the masses of the cycles are determined - sum_c
'''

zoo = Zoo.get_file(r'D:\praca_MZA\zadanie_B\slo1.in')

it_a,it_b = iter(zoo.a),iter(zoo.b)
odw,simple_cycle = [b==next(it_a) for b in iter(zoo.b)], []
for nr,b in enumerate(it_b):
    if odw[nr] ==False:
        bi,x,c=b,nr,[]
        while odw[x]!=True:
            odw[x]=True
            c.append(bi)
            bi, x = zoo.p(bi)
        simple_cycle.append(c)
sum_all,min_all,len_all =[],[],[]
for cycles in iter(simple_cycle):
    sum_c,min_c,len_c =0, 6500,0
    for c in iter(cycles):
        len_c += 1
        m =zoo.m[c-1]
        sum_c +=m
        if m<min_c:
            min_c=m
    sum_all.append(sum_c), min_all.append(min_c), len_all.append(len_c)
    min_all_gl = min(min_all)
w = 0
# counts the sum for items that change places on the list
for i in range(len(len_all)):
    metoda1 = sum_all[i] + (len_all[i] - 2) * min_all[i]
    metoda2 = sum_all[i] + min_all[i] + (len_all[i] + 1) * min_all_gl
# the results for both methods are compared. The result for the lower sum is selected.
    w += metoda1 if metoda1 < metoda2 else metoda2
print(w)




