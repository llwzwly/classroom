# -*- coding = utf-8 -*-

with open(r'C:\Users\温志伟\Desktop\file.txt','r') as f1 :
    list1 = f1.read().split('\n')
    perfor = []
    all_sum = 0
    all_avg = 0

    del list1[-3:]
    
    for num in list1 :
        if list1.index(num) != 0 :
            
            list2 = num.split(' ')
            sum = 0
            id = -1
            for i in list2 :
                id += 1
                if id !=0 :
                    sum += float(i)
                      
            avg = round(sum / (len(list2)-1), 2)
            perfor.append(list2[0:] +[str(sum), str(avg)])
            all_sum += sum 
            all_avg += avg
        
        else:
            pass
    
    perfor = sorted(perfor, key = lambda x:x[-1], reverse = True)
    fina_perfor = []
    grade = 1
    for i in perfor :
        fina_word = [str(grade)] + i
        fina_perfor.append(fina_word)
        grade += 1
    print(fina_perfor)
    all_sum = round(all_sum / len(list1), 2)
    all_avg = round(all_avg / len(list1), 2)

Chinese_sum = 0
math_sum = 0
English_sum = 0
physic_sum = 0
chemistry_sum = 0
biology_sum = 0
politics_sum = 0
histroy_sum = 0
geography_sum = 0
for word in fina_perfor :
    Chinese_sum = Chinese_sum + float(word[2])
    math_sum = math_sum + float(word[3])
    English_sum = English_sum + float(word[4])
    physic_sum = physic_sum + float(word[5])
    chemistry_sum = chemistry_sum + float(word[6])
    biology_sum = biology_sum + float(word[7])
    politics_sum = politics_sum + float(word[8])
    histroy_sum = histroy_sum + float(word[9])
    geography_sum = geography_sum + float(word[10])    
    num1 = -1
    for i in word :
        num1 += 1
        if num1 != 0 :
            if num1 != 1 :
                if num1 != len(word) - 1 :
                    if float(i) < 60 :
                        word[word.index(i)] = '不及格'
                    else :
                        pass


Chinese_sum = round(Chinese_sum / len(list1), 2)
math_sum = round(math_sum / len(list1), 2)
English_sum = round(English_sum / len(list1), 2)
physic_sum = round(physic_sum / len(list1), 2)
chemistry_sum = round(chemistry_sum / len(list1), 2)
biology_sum = round(biology_sum / len(list1), 2)
politics_sum = round(politics_sum / len(list1), 2)
histroy_sum = round(histroy_sum / len(list1), 2)
geography_sum = round(geography_sum / len(list1), 2)

all_perfor = [['0', '平均', str(Chinese_sum), str(math_sum), str(English_sum), str(physic_sum), str(chemistry_sum), \
str(biology_sum), str(politics_sum), str(histroy_sum), str(geography_sum), str(all_sum), str(all_avg)]]

perfor = [['名次'] + list1[0].split(' ') + ['总分', '平均分']] + all_perfor + fina_perfor

for one in perfor :
    one.append('\n')

end_perfor = []
for every in perfor :
    every = ' '.join(every)
    end_perfor.append(every)
print(end_perfor)


with open(r'C:\Users\温志伟\Desktop\report.txt', 'w') as f2 :
    f2.writelines(end_perfor)
