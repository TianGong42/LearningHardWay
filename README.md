# 笨方法学python学习目录，计划在2月1号时把整本书过一遍

## 第一章
讲了打印
## 第二章
讲了注释
## 第三章
讲了四则运算
## 第四章
讲了变量
## 第五章讲了
格式化的变量输出
## 第六章讲了
其他的格式化输出
## 第十三章
讲述了引入包，并且使用argv获取参数
## 第十四章
还是练习了使用引入sys包，并且使用argv获取参数。也用input获取参数，然后输出
# 第十五章
windows 下获取pydoc的方式
`python -m pydoc open`
第十五章主要还是通过open()方法，获取一个文件对象，然后使用read()方法来获取本文里的对象
# 第十六章
- close:关闭文件。跟你的编辑器中的"文件"->"保存"是一个意思
- read:读取文件内容。你可以把结果赋值给一个变量
- readline： 只读取文本文件中的一行
- truncate: 清空文件，小心使用
- write('stuff'):将"stuff"写入文件
- seek(0):将文件位置移动到文件开头
这一章讲了通过write方法将文本写入到文本中，并介绍了文件对象的几个用法

# 第十七章
1. 第十七章讲述了在命令行下创建文件，并输入内容
2. len()获取字符串对象的长度
3. exists()函数判断文件是否存在
# 第十八章
本章就是讲述了函数的初级使用方法，有入参是列表，两个入参，单个入参，和无参函数

# 第十九章
使用了函数，并且函数的入参使用了变量、数值、数学公式等

# 第二十章
本章重点还是使用函数，并且自己定义的两个函数
通过因为文件对象的内容，来实现函数。
通过readline()的特性，实现了着行打印的功能，也可以使用seek来清除标光的位置
readline()函数：里面的代码会扫描文件的每一个字节，直到找到一个\n为止，然后它停止读取文件，
并且返回此前发现的文件内容。文件f会记录每次调用readline()后读取的位置。这样它就可以在下次被调用时读取接下来的一行。

# 第二十一章
本章使用了四个函数，包含了加减乘除。
然后使用了嵌套，一次性调用了四个函数

# 第三十二章
1、本章讲了list，list可以存储数字和字符串。既可以单独存储，也可以混合存储
2、创建了一个空列表，使用range(0,5)和append()方法往列表里存储数据

# 第三十三章
1、本章使用了while循环，将0-6存入list里面，然后每次循环都打印要存入的数和整个list
2、使用for，着行打印列表里的数

# 第三十四章
这章看了半天，还上网查了资料。本章应该是讲数组的关系。
一个list的第一个数字，是list[0]而不是list[1]

# 第三十五章
这张讲了一个小游戏，比较麻烦。多分支链路，但是真实开发应该就这种多分支的链路

# 第三十六章
1. 每一条if语句必须包含一个else
2. 如果这个else永远不应该被执行到，因为它本身没有任何意思，那你必须在else
语句后面使用一个叫die的函数，让它打印出出错消息并且“死”给你看，这和上一个习题类似，
这样你可以找到更多的错误
3. if语句的嵌套不要超过两层，最好尽量不要保持只有一层
4. 把if语句当做段落来对待，其中的每一个if、elif和else组合就跟一个段落的句子组合一样。
在这种组合的最前面和最后面留一个空行以作区分。
5. 你的布尔测试应该很简单，如果它们很复杂，你需要在函数里将它们的运算事先放到一个变量里，并且为变量取一个好名字

# 第三十八章
讲了使了while循环和两个list。通过pop()和append()函数
进行了运算


# 第41章
- 类：告诉Python创建新类型的东西
- 对象：两个意思，即最基本的东西，或者某样东西的实例
- 实例：这是让Python创建一个类时得到的东西
- def:这是在类里边定义函数的方法
- self:在类的函数中，self指代被访问的对象或者实例的一个变量
- 继承：指一个类可以继承另一个类的特性，和父子关系类似
- 组合：值一个类可以将别的类作为它的部件构建起来，有点像车子和车轮的关系
- 属性：类的一个属性，它来自组合，而且通常是一个变量
- 是什么：用来描述继承关系，如Salmon is-a Fish
- 有什么：用来描述某个东西是由另外一些东西组成，或者某个东西有某个特征，如Salmon has-a month
## 措辞
- class X(Y): 创建一个叫X的类，它是Y的一种。
- class X(object): def __init__(self, J): 类X有一个__init__,它接受self和J作为参数
- class X(object): def M(self, J): 类X有一个名为M的函数，它接受self和J作为参数
- foo = X():将foo设为类X的一个实例
- foo.M(J):从foo中找到M函数，并使用self和J参数调用
- foo.K = Q：从foo中获取K属性，并将其设为Q

## 注意的点
1. 在抄第41章的代码的时候，发现第35行一直提示语法不合法
调试后发现，是上一行的括号没有合拢
最后，第41章的代码没看懂。算了，先跳过

# 第四十二章
这一章主要是讲了类的创建，子类的创建，还有对象的创建，总体还是比较简单的
# 第四十三章 基本的面向对象分析和设计
一个标准的设计方法如下
1. 把要解决的问题写下来或者画出来
2. 将第一条中的关键概念提取出来并加以研究
3. 创建一个类层次结构和对象图
4. 用代码实现各个类， 并写一个测试来运行它们
5. 重复上述步骤并细化代码

## 设计一个游戏
> 外星人入侵宇宙飞船，我们的英雄需要通过各种房间组成迷宫，打败遇到的外星人，这样才能
通过救生船回到下面的行星上去
下面是各个场景
- **死亡**。玩家死去的场景，应该比较搞笑
- **中央走廊**。这是游戏的起点，哥顿人已经在那里把守了，玩家需要讲一个笑话才能继续
- **激光武器库**。在这里英雄会找找到一个中子弹，在乘坐救生船离开时要用它把飞船炸掉。
这个房间有一个数字键盘，英雄需要猜测密码组合。
- **飞船**。另一个战斗场景，英雄需要在这里埋炸弹
- **救生舱**。英雄逃离场景，但需要才对是哪艘救生船

### 提取和研究关键概念
- 外星人(Alien)
- 迷宫(Maze)
- 玩家(Player)
- 房间(Room)
- 飞船(Ship)
- 场景(Scene)
- 哥顿人(Gothon)
- 死亡(Death)
- 救生舱(Escape Pod)
- 中央走廊(Central Corridor)
- 行星(Planet)
- 激光武器库(Laser Weapon Armory)
- 地图(Map)
- 主控舱(The Bridge)
- 引擎(Engine)

## 创建类层次结构图和对象图
- Map 地图
    - next_scene(方法)
    - opening_scene(方法)
- Engine 引擎
    - play(方法)
- Scene 场景
    - enter(方法)
    - Death 死亡
    - Central Corridor  中央走廊
    - Laser Weapon Armory 激光武器库
    - The Bridge 主控舱
    - Escape Pod 救生舱

## 最后结果没有跑起来
 ```
File ".\ex43.py", line 301, in <module>
    a_game.play()
  File ".\ex43.py", line 25, in play
    next_scene_name = current_scene.enter()
 ```
 反正我也是莫名其妙，再说了

 # 第四十四章 继承与组合
 继承就是用来指明一个类的大部分或全部功能都是从一个父类中获得的。
 父类和子类有3种交互方式
 1. 子类上的动作完全等同于父类上的动作
 2. 子类上的动作完全覆盖了父类上的动作
 3. 子类上的动作部分替换了父类上的动作
 