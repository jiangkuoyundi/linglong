# coding:utf-8
#  析构函数 __del__ ，__del__在对象销毁的时候被调用，当对象不再被使用时，__del__方法运行：
class Point:
    def __init__( self, x=0, y=0):
        self.x = x
        self.y = y
    def __del__(self):
        class_name = self.__class__.__name__
        print(class_name, "destroy ")

pt1 = Point()
pt2 = pt1
pt3 = Point()
print(id(pt1), id(pt2), id(pt3)) # 打印对象的id

# 不调用del方法也会自动销毁对象？
# del pt1
# del pt2
# del pt3
