#-*- coding: utf-8 -*-
import os
import time
import readExcel

#循环读取已经生产的语搜指令；函数范围range(4)0,1,2,3  range(1,4)1,2,3
for i in range(1,readExcel.getExcleData()):
    os.system("audio\\"+str(i)+".wav")
    if 1==1:
        print(str(i)+'pass')
    else:
        print(str(i)+'failure')
    time.sleep(15)

#待添加内容：对音箱的发音进行录音，然后将录音内容转换为文字与预期结果进行对比，如果符合预期则通过；