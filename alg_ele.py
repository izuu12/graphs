
from itertools import zip_longest

def get_file():
    path = r'D:\praca\praca_MZA\zadanie_B\slo1.in'
    with open(path, 'r') as file:
        for nr,line in enumerate(file.readlines()):
           yield line

def get_record(nr_lin,records):
    for nr, record in enumerate(iter(records)):
        if nr == nr_lin:
            yield [int(x) for x in record.strip().split(' ')]
            break
def p(a_list, b_list, b):
    for nr,ai in enumerate(iter(a_list)):
        if b==ai:
            bi= b_list[nr]
            break
    return bi,nr

def get_simple_cycle(a_list, b_list,odw):
    simple_cycles =[]
    for b_li in iter(get_record(3, get_file())):
        for nr,bi in enumerate(b_li):
            if odw[nr] ==False:
                b = bi
                x=nr
                c=[]
                while odw[x]!=True:
                    odw[x]=True
                    c.append(b)
                    b,x =p(a_list, b_list,b)
                simple_cycles.append(c)
    yield simple_cycles

def get_params(simple_cycle,m_list):
    sum_c =[]
    min_mass_c =[]
    len_c =[]
    for cycles in iter(simple_cycle):
        for nr in range(len(cycles)):
            #print('numer cyklu :', nr)
            sum,min_c, nrc =0,6500, 0
            for i in range(len(cycles[nr])):
                nrc+=1
                m = m_list[cycles[nr][i]-1]
                #print('m{}={}'.format(cycles[nr][i],m ))
                sum+=m
                if m<min_c:
                    min_c =m
            sum_c.append(sum),min_mass_c.append(min_c),len_c.append(nrc)
    min_all = min(min_mass_c)
    return sum_c, min_mass_c, len_c, min_all
def get_m(m_list,ci):
    for nr,mi in enumerate(iter(m_list)):
        if ci-1==nr:
            m= mi
            break
    return m
def get_params2(simple_cycle, m_list):
    sum_all_c,min_all_c,len_all_c =[],[],[]
    for cycles in iter(simple_cycle):
        for c in iter(cycles):
            sum_c,min_c,len_c=0,6500,0
            for ci in iter(c):
                len_c+=1
                m=get_m(m_list,ci)
                sum_c +=m
                if m<min_c:
                    min_c=m
            sum_all_c.append(sum_c),min_all_c.append(min_c), len_all_c.append(len_c)
    min_all = min(min_all_c)
    return sum_all_c,min_all_c,len_all_c,min_all




def get_result(simple_cycle, m_list):
    w=0
    sum_mas_c, min_mas_c, len_c, min_all = get_params(simple_cycle,m_list)
    for i in range(len(len_c)):
        metoda1 = sum_mas_c[i] + (len_c[i] - 2) * min_mas_c[i]
        metoda2 =sum_mas_c[i]+ min_mas_c[i] +(len_c[i] +1) *min_all
        w += metoda1 if metoda1 < metoda2 else metoda2
    return w

a_gen,b_gen  =iter(get_record(2, get_file())), iter(get_record(3, get_file()))
odw = [a==b for a,b in zip_longest(next(a_gen), next(b_gen))]

a_list= ([a for a in iter(get_record(2,get_file()))][0])
b_list = ([b for b in iter(get_record(3,get_file()))][0])
m_list = ([b for b in iter(get_record(1,get_file()))][0])

simple_cycle = get_simple_cycle(a_list,b_list, odw)

print(get_result(simple_cycle,m_list))














