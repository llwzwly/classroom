#-*- coding : utf-8 -*-
class prize:
    def __init__(self, country, gold_medal_number, silver_medal_number, copper_medal_number):
        self.country = country
        self.gold_medal_number = gold_medal_number
        self.silver_medal_number = silver_medal_number
        self.copper_medal_number = copper_medal_number
    def get_place(self, place):
        if place == 1:
            self.gold_medal_number += 1
        elif place == 2:
            self.silver_medal_number += 1
        elif place == 3:
            self.copper_medal_number += 1
    def medal_number(self):
        return self.gold_medal_number + self.silver_medal_number + self.copper_medal_number
    def __str__(self):
        return r'%s: 金 %d, 银 %d, 铜 %d' % (self.country, self.gold_medal_number, self.silver_medal_number, \
        self.copper_medal_number)

if __name__ == '__main__':
    China = prize('中国', 99, 88, 66)
    UK = prize('英国', 66, 55, 33)
    US = prize('美国', 77, 55, 10)
    print(China)
    print(UK)
    print(US)
    print('中国又获得一个冠军')
    China.get_place(1)
    medal_list = [China, UK, US]
    order_gold = sorted(medal_list, key = lambda x:x.gold_medal_number, reverse = True)
    print('按金牌数排序：')
    for i in order_gold:
        print(i)
    print('按奖牌牌数排序：')
    order_number = sorted(medal_list, key = lambda x: x.medal_number(), reverse = True)
    for j in order_number:
        print(j)
