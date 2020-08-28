import random
import time
import gc
import datetime
from collections import Counter
try:
    dt = datetime.datetime.now()
    time.sleep(1)
    print(u'程序启动时间:'+dt.strftime('%Y-%m-%d %H:%M:%S'))
    time.sleep(2)
    print(u'程序正在计算......')
    real_red_1 = [1, 2, 3, 4, 5]
    real_red_2 = [7, 8, 6, 9, 5]
    real_red_3 = [14, 11, 13, 16, 12]
    real_red_4 = [20, 17, 22, 23, 18]
    real_red_5 = [26, 27, 25, 28, 24]
    real_red_6 = [32, 33, 31, 30, 29]
    real_blue = [9, 12, 11, 14, 6,13,7,15]
    def num_red_1():
        i = 0
        numlist_1 = []
        numlist_2 = []
        numlist_3 = []
        numlist_4 = []
        numlist_5 = []
        while i < 10000:
            i = i + 1
            numlist_1.append(random.randint(1, 33))
            gc.collect()
            numlist_2.append(random.randint(1, 33))
            gc.collect()
            numlist_3.append(random.randint(1, 33))
            gc.collect()
            numlist_4.append(random.randint(1, 33))
            gc.collect()
            numlist_5.append(random.randint(1, 33))
        global numlist
        numlist = numlist_1 + numlist_2 + numlist_3 + numlist_4 + numlist_5
        numpercent = {}
        for d in set(numlist):
            numpercent[numlist.count(d)] = d
        for e in reversed(sorted(numpercent.keys())[-1:]):
            return numpercent[e]
    while True:
        for i in range(10000):
            num_red_1()
            bingonum_red_1 = num_red_1()
            if bingonum_red_1 not in real_red_1:
                continue
            c = Counter(numlist)
#            print c[bingonum_red_1]
            if bingonum_red_1 == 1:
                numberA = c[bingonum_red_1]/float(50000)
                numberB = 384/float(2004)
                #            print numberA
                #            print numberB
                #            print '%.2f%%'%(numberA / numberB*100)
                print(u'一号红球预测完成' + '     ' + u'号码:' + str(bingonum_red_1) + '     ' + u'中奖概率' + str(
                    '%.2f%%' % (numberB*(1+numberA)*100)))
            elif bingonum_red_1 == 2:
                numberA = c[bingonum_red_1]/float(50000)
                numberB = 307/float(2004)
                print(u'一号红球预测完成' + '     ' + u'号码:' + str(bingonum_red_1) + '     ' + u'中奖概率' + str(
                    '%.2f%%' % (numberB*(1+numberA)*100)))
            elif bingonum_red_1 == 3:
                numberA = c[bingonum_red_1]/float(50000)
                numberB = 255/float(2004)
                print(u'一号红球预测完成' + '     ' + u'号码:' + str(bingonum_red_1) + '     ' + u'中奖概率' + str(
                    '%.2f%%' % (numberB*(1+numberA)*100)))
            elif bingonum_red_1 == 4:
                numberA = c[bingonum_red_1]/float(50000)
                numberB = 209/float(2004)
                print(u'一号红球预测完成' + '     ' + u'号码:' + str(bingonum_red_1) + '     ' + u'中奖概率' + str(
                    '%.2f%%' % (numberB*(1+numberA)*100)))
            else:
                numberA = c[bingonum_red_1]/float(50000)
                numberB = 175/float(2004)
                print(u'一号红球预测完成' + '     ' + u'号码:' + str(bingonum_red_1) + '     ' + u'中奖概率' + str(
                    '%.2f%%' % (numberB*(1+numberA)*100)))
            break
        break
    time.sleep(5)
    def num_red_2():
        i = 0
        numlist_1 = []
        numlist_2 = []
        numlist_3 = []
        numlist_4 = []
        numlist_5 = []
        while i < 10000:
            i = i + 1
            numlist_1.append(random.randint(1, 33))
            gc.collect()
            numlist_2.append(random.randint(1, 33))
            gc.collect()
            numlist_3.append(random.randint(1, 33))
            gc.collect()
            numlist_4.append(random.randint(1, 33))
            gc.collect()
            numlist_5.append(random.randint(1, 33))
        global numlist
        numlist = numlist_1 + numlist_2 + numlist_3 + numlist_4 + numlist_5
        numpercent = {}
        for d in set(numlist):
            numpercent[numlist.count(d)] = d
        for e in reversed(sorted(numpercent.keys())[-1:]):
            return numpercent[e]
    while True:
        for i in range(10000):
            num_red_2()
            bingonum_red_2 = num_red_2()
            if bingonum_red_2 not in real_red_2:
                continue
            c = Counter(numlist)
            if bingonum_red_2 == 7:
                numberA = c[bingonum_red_2]/float(50000)
                numberB = 181/float(2004)
                print(u'二号红球预测完成' + '     ' + u'号码:' + str(bingonum_red_2) + '     ' + u'中奖概率' + str(
                    '%.2f%%' % (numberB*(1+numberA)*100)))
            elif bingonum_red_2 == 8:
                numberA = c[bingonum_red_2]/float(50000)
                numberB = 168/float(2004)
                print(u'二号红球预测完成' + '     ' + u'号码:' + str(bingonum_red_2) + '     ' + u'中奖概率' + str(
                    '%.2f%%' % (numberB*(1+numberA)*100)))
            elif bingonum_red_2 == 6:
                numberA = c[bingonum_red_2]/float(50000)
                numberB = 160/float(2004)
                print(u'二号红球预测完成' + '     ' + u'号码:' + str(bingonum_red_2) + '     ' + u'中奖概率' + str(
                    '%.2f%%' % (numberB*(1+numberA)*100)))
            elif bingonum_red_2 == 9:
                numberA = c[bingonum_red_2]/float(50000)
                numberB = 140/float(2004)
                print(u'二号红球预测完成' + '     ' + u'号码:' + str(bingonum_red_2) + '     ' + u'中奖概率' + str(
                    '%.2f%%' % (numberB*(1+numberA)*100)))
            else:
                numberA = c[bingonum_red_2]/float(50000)
                numberB = 140/float(2004)
                print(u'二号红球预测完成' + '     ' + u'号码:' + str(bingonum_red_2) + '     ' + u'中奖概率' + str(
                    '%.2f%%' % (numberB*(1+numberA)*100)))
            break
        break
    time.sleep(5)
    def num_red_3():
        i = 0
        numlist_1 = []
        numlist_2 = []
        numlist_3 = []
        numlist_4 = []
        numlist_5 = []
        while i < 10000:
            i = i + 1
            numlist_1.append(random.randint(1, 33))
            gc.collect()
            numlist_2.append(random.randint(1, 33))
            gc.collect()
            numlist_3.append(random.randint(1, 33))
            gc.collect()
            numlist_4.append(random.randint(1, 33))
            gc.collect()
            numlist_5.append(random.randint(1, 33))
        global numlist
        numlist = numlist_1 + numlist_2 + numlist_3 + numlist_4 + numlist_5
        numpercent = {}
        for d in set(numlist):
            numpercent[numlist.count(d)] = d
        for e in reversed(sorted(numpercent.keys())[-1:]):
            return numpercent[e]
    while True:
        for i in range(10000):
            num_red_3()
            bingonum_red_3 = num_red_3()
            if bingonum_red_3 not in real_red_3:
                continue
            c = Counter(numlist)
            if bingonum_red_3 == 14:
                numberA = c[bingonum_red_3]/float(50000)
                numberB = 147/float(2004)
                print( u'三号红球预测完成' + '     ' + u'号码:' + str(bingonum_red_3) + '     ' + u'中奖概率' + str(
                    '%.2f%%' % (numberB*(1+numberA)*100)))
            elif bingonum_red_3 == 11:
                numberA = c[bingonum_red_3]/float(50000)
                numberB = 136/float(2004)
                print( u'三号红球预测完成' + '     ' + u'号码:' + str(bingonum_red_3) + '     ' + u'中奖概率' + str(
                    '%.2f%%' % (numberB*(1+numberA)*100)))
            elif bingonum_red_3 == 13:
                numberA = c[bingonum_red_3]/float(50000)
                numberB = 129/float(2004)
                print( u'三号红球预测完成' + '     ' + u'号码:' + str(bingonum_red_3) + '     ' + u'中奖概率' + str(
                    '%.2f%%' % (numberB*(1+numberA)*100)))
            elif bingonum_red_3 == 16:
                numberA = c[bingonum_red_3]/float(50000)
                numberB = 128/float(2004)
                print( u'三号红球预测完成' + '     ' + u'号码:' + str(bingonum_red_3) + '     ' + u'中奖概率' + str(
                    '%.2f%%' % (numberB*(1+numberA)*100)))
            else:
                numberA = c[bingonum_red_3]/float(50000)
                numberB = 125/float(2004)
                print( u'三号红球预测完成' + '     ' + u'号码:' + str(bingonum_red_3) + '     ' + u'中奖概率' + str(
                    '%.2f%%' % (numberB*(1+numberA)*100)))
            break
        break
    time.sleep(5)
    def num_red_4():
        i = 0
        numlist_1 = []
        numlist_2 = []
        numlist_3 = []
        numlist_4 = []
        numlist_5 = []
        while i < 10000:
            i = i + 1
            numlist_1.append(random.randint(1, 33))
            gc.collect()
            numlist_2.append(random.randint(1, 33))
            gc.collect()
            numlist_3.append(random.randint(1, 33))
            gc.collect()
            numlist_4.append(random.randint(1, 33))
            gc.collect()
            numlist_5.append(random.randint(1, 33))
        global numlist
        numlist = numlist_1 + numlist_2 + numlist_3 + numlist_4 + numlist_5
        numpercent = {}
        for d in set(numlist):
            numpercent[numlist.count(d)] = d
        for e in reversed(sorted(numpercent.keys())[-1:]):
            return numpercent[e]
    while True:
        for i in range(10000):
            num_red_4()
            bingonum_red_4 = num_red_4()
            if bingonum_red_4 not in real_red_4:
                continue
            c = Counter(numlist)
            if bingonum_red_4 == 20:
                numberA = c[bingonum_red_4]/float(50000)
                numberB = 147/float(2004)
                print( u'四号红球预测完成' + '     ' + u'号码:' + str(bingonum_red_4) + '     ' + u'中奖概率' + str(
                    '%.2f%%' % (numberB*(1+numberA)*100)))
            elif bingonum_red_4 == 17:
                numberA = c[bingonum_red_4]/float(50000)
                numberB = 146/float(2004)
                print( u'四号红球预测完成' + '     ' + u'号码:' + str(bingonum_red_4) + '     ' + u'中奖概率' + str(
                    '%.2f%%' % (numberB*(1+numberA)*100)))
            elif bingonum_red_4 == 22:
                numberA = c[bingonum_red_4]/float(50000)
                numberB = 144/float(2004)
                print( u'四号红球预测完成' + '     ' + u'号码:' + str(bingonum_red_4) + '     ' + u'中奖概率' + str(
                    '%.2f%%' % (numberB*(1+numberA)*100)))
            elif bingonum_red_4 == 23:
                numberA = c[bingonum_red_4]/float(50000)
                numberB = 132/float(2004)
                print( u'四号红球预测完成' + '     ' + u'号码:' + str(bingonum_red_4) + '     ' + u'中奖概率' + str(
                    '%.2f%%' % (numberB*(1+numberA)*100)))
            else:
                numberA = c[bingonum_red_4]/float(50000)
                numberB = 129/float(2004)
                print( u'四号红球预测完成' + '     ' + u'号码:' + str(bingonum_red_4) + '     ' + u'中奖概率' + str(
                    '%.2f%%' % (numberB*(1+numberA)*100)))
            break
        break
    time.sleep(5)
    def num_red_5():
        i = 0
        numlist_1 = []
        numlist_2 = []
        numlist_3 = []
        numlist_4 = []
        numlist_5 = []
        while i < 10000:
            i = i + 1
            numlist_1.append(random.randint(1, 33))
            gc.collect()
            numlist_2.append(random.randint(1, 33))
            gc.collect()
            numlist_3.append(random.randint(1, 33))
            gc.collect()
            numlist_4.append(random.randint(1, 33))
            gc.collect()
            numlist_5.append(random.randint(1, 33))
        global numlist
        numlist = numlist_1 + numlist_2 + numlist_3 + numlist_4 + numlist_5
        numpercent = {}
        for d in set(numlist):
            numpercent[numlist.count(d)] = d
        for e in reversed(sorted(numpercent.keys())[-1:]):
            return numpercent[e]
    while True:
        for i in range(10000):
            num_red_5()
            bingonum_red_5 = num_red_5()
            if bingonum_red_5 not in real_red_5:
                continue
            c = Counter(numlist)
            if bingonum_red_5 == 26:
                numberA = c[bingonum_red_5]/float(50000)
                numberB = 173/float(2004)
                print( u'五号红球预测完成' + '     ' + u'号码:' + str(bingonum_red_5) + '     ' + u'中奖概率' + str(
                    '%.2f%%' % (numberB*(1+numberA)*100)))
            elif bingonum_red_5 == 27:
                numberA = c[bingonum_red_5]/float(50000)
                numberB = 167/float(2004)
                print( u'五号红球预测完成' + '     ' + u'号码:' + str(bingonum_red_5) + '     ' + u'中奖概率' + str(
                    '%.2f%%' % (numberB*(1+numberA)*100)))
            elif bingonum_red_5 == 25:
                numberA = c[bingonum_red_5]/float(50000)
                numberB = 164/float(2004)
                print( u'五号红球预测完成' + '     ' + u'号码:' + str(bingonum_red_5) + '     ' + u'中奖概率' + str(
                    '%.2f%%' % (numberB*(1+numberA)*100)))
            elif bingonum_red_5 == 28:
                numberA = c[bingonum_red_5]/float(50000)
                numberB = 160/float(2004)
                print( u'五号红球预测完成' + '     ' + u'号码:' + str(bingonum_red_5) + '     ' + u'中奖概率' + str(
                    '%.2f%%' % (numberB*(1+numberA)*100)))
            else:
                numberA = c[bingonum_red_5]/float(50000)
                numberB = 133/float(2004)
                print( u'五号红球预测完成' + '     ' + u'号码:' + str(bingonum_red_5) + '     ' + u'中奖概率' + str(
                    '%.2f%%' % (numberB*(1+numberA)*100)))
            break
        break
    time.sleep(5)
    def num_red_6():
        i = 0
        numlist_1 = []
        numlist_2 = []
        numlist_3 = []
        numlist_4 = []
        numlist_5 = []
        while i < 10000:
            i = i + 1
            numlist_1.append(random.randint(1, 33))
            gc.collect()
            numlist_2.append(random.randint(1, 33))
            gc.collect()
            numlist_3.append(random.randint(1, 33))
            gc.collect()
            numlist_4.append(random.randint(1, 33))
            gc.collect()
            numlist_5.append(random.randint(1, 33))
        global numlist
        numlist = numlist_1 + numlist_2 + numlist_3 + numlist_4 + numlist_5
        numpercent = {}
        for d in set(numlist):
            numpercent[numlist.count(d)] = d
        for e in reversed(sorted(numpercent.keys())[-1:]):
            return numpercent[e]
    while True:
        for i in range(10000):
            num_red_6()
            bingonum_red_6 = num_red_6()
            if bingonum_red_6 not in real_red_6:
                continue
            c = Counter(numlist)
            if bingonum_red_6 == 32:
                numberA = c[bingonum_red_6]/float(50000)
                numberB = 309/float(2004)
                print( u'六号红球预测完成' + '     ' + u'号码:' + str(bingonum_red_6) + '     ' + u'中奖概率' + str(
                    '%.2f%%' % (numberB*(1+numberA)*100)))
            elif bingonum_red_6 == 33:
                numberA = c[bingonum_red_6]/float(50000)
                numberB = 307/float(2004)
                print( u'六号红球预测完成' + '     ' + u'号码:' + str(bingonum_red_6) + '     ' + u'中奖概率' + str(
                    '%.2f%%' % (numberB*(1+numberA)*100)))
            elif bingonum_red_6 == 31:
                numberA = c[bingonum_red_6]/float(50000)
                numberB = 249/float(2004)
                print( u'六号红球预测完成' + '     ' + u'号码:' + str(bingonum_red_6) + '     ' + u'中奖概率' + str(
                    '%.2f%%' % (numberB*(1+numberA)*100)))
            elif bingonum_red_6 == 30:
                numberA = c[bingonum_red_6]/float(50000)
                numberB = 221/float(2004)
                print( u'六号红球预测完成' + '     ' + u'号码:' + str(bingonum_red_6) + '     ' + u'中奖概率' + str(
                    '%.2f%%' % (numberB*(1+numberA)*100)))
            else:
                numberA = c[bingonum_red_6]/float(50000)
                numberB = 202/float(2004)
                print( u'六号红球预测完成' + '     ' + u'号码:' + str(bingonum_red_6) + '     ' + u'中奖概率' + str(
                    '%.2f%%' % (numberB*(1+numberA)*100)))
            break
        break
    time.sleep(5)
    def num_blue():
        i = 0
        numlist_1 = []
        numlist_2 = []
        numlist_3 = []
        numlist_4 = []
        numlist_5 = []
        while i < 10000:
            i = i + 1
            numlist_1.append(random.randint(1, 16))
            gc.collect()
            numlist_2.append(random.randint(1, 16))
            gc.collect()
            numlist_3.append(random.randint(1, 16))
            gc.collect()
            numlist_4.append(random.randint(1, 16))
            gc.collect()
            numlist_5.append(random.randint(1, 16))
        global numlist
        numlist = numlist_1 + numlist_2 + numlist_3 + numlist_4 + numlist_5
        numpercent = {}
        for d in set(numlist):
            numpercent[numlist.count(d)] = d
        for e in reversed(sorted(numpercent.keys())[-1:]):
            return numpercent[e]
    while True:
        for i in range(10000):
            num_blue()
            bingonum_blue = num_blue()
            if bingonum_blue not in real_blue:
                continue
            c = Counter(numlist)
            if bingonum_blue == 9:
                numberA = c[bingonum_blue]/float(50000)
                numberB = 140/float(2004)
                print(u'蓝球预测完成' + '     ' + u'号码:' + str(bingonum_blue) + '     ' + u'中奖概率' + str(
                    '%.2f%%' % (numberB*(1+numberA)*100)))
            elif bingonum_blue == 12:
                numberA = c[bingonum_blue]/float(50000)
                numberB = 136/float(2004)
                print( u'蓝球预测完成' + '     ' + u'号码:' + str(bingonum_blue) + '     ' + u'中奖概率' + str(
                    '%.2f%%' % (numberB*(1+numberA)*100)))
            elif bingonum_blue == 11:
                numberA = c[bingonum_blue]/float(50000)
                numberB = 135/float(2004)
                print( u'蓝球预测完成' + '     ' + u'号码:' + str(bingonum_blue) + '     ' + u'中奖概率' + str(
                    '%.2f%%' % (numberB*(1+numberA)*100)))
            elif bingonum_blue == 14:
                numberA = c[bingonum_blue]/float(50000)
                numberB = 130/float(2004)
                print( u'蓝球预测完成' + '     ' + u'号码:' + str(bingonum_blue) + '     ' + u'中奖概率' + str(
                    '%.2f%%' % (numberB*(1+numberA)*100)))
            elif bingonum_blue == 6:
                numberA = c[bingonum_blue]/float(50000)
                numberB = 129/float(2004)
                print(u'蓝球预测完成' + '     ' + u'号码:' + str(bingonum_blue) + '     ' + u'中奖概率' + str(
                    '%.2f%%' % (numberB*(1+numberA)*100)))
            elif bingonum_blue == 13:
                numberA = c[bingonum_blue]/float(50000)
                numberB = 129/float(2004)
                print(u'蓝球预测完成' + '     ' + u'号码:' + str(bingonum_blue) + '     ' + u'中奖概率' + str(
                    '%.2f%%' % (numberB*(1+numberA)*100)))
            elif bingonum_blue == 7:
                numberA = c[bingonum_blue]/float(50000)
                numberB = 128/float(2004)
                print(u'蓝球预测完成' + '     ' + u'号码:' + str(bingonum_blue) + '     ' + u'中奖概率' + str(
                    '%.2f%%' % (numberB*(1+numberA)*100)))
            else:
                numberA = c[bingonum_blue]/float(50000)
                numberB = 128/float(2004)
                print( u'蓝球预测完成' + '     ' + u'号码:' + str(bingonum_blue) + '     ' + u'中奖概率' + str(
                    '%.2f%%' % (numberB*(1+numberA)*100)))
            break
        break
finally:
  input()



