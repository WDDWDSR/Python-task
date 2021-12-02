#coding:gbk
"""
第一个小项目：Rock-paper-scissors-lizard-Spock
程序目的：利用python程序设计RPSLS游戏
作者：申书瑜
日期：2021/11/27
"""

import random



# 0 - 石头
# 1 - 史波克
# 2 - 布
# 3 - 蜥蜴
# 4 - 剪刀

# 以下为完成游戏所需要用到的自定义函数

def name_to_number(name):    #自定义函数name_to_number实现将游戏对象对应到不同整数
    if name=="石头":
        return 0
    elif name=="史波克":
        return 1
    elif name=="布":
        return 2
    elif name=="蜥蜴":
        return 3
    elif name=="剪刀":
        return 4


    #"""
    #将游戏对象对应到不同的整数
    #"""

    # 使用if/elif/else语句将各游戏对象对应到不同的整数
    # 不要忘记返回结果





def number_to_name(comp_number):   #自定义num_to_name函数，将不同整数对应到游戏的不同对象
    if comp_number==0:
        return "石头"
    elif comp_number==1:
        return "史波克"
    elif comp_number==2:
        return "布"
    elif comp_number==3:
        return "蜥蜴"
    elif comp_number==4:
        return "剪刀"
    """
    将整数 (0, 1, 2, 3, or 4)对应到游戏的不同对象
    """

    # 使用if/elif/else语句将不同的整数对应到游戏的不同对象
    # 不要忘记返回结果




def rpsls(player_choice):       #自定义函数rpsls，通过对玩家输入的对象转化为的数字与计算机随机生成的数字比较，按照rpsls规则进行胜负判断
    player_choice_number = name_to_number(player_choice)  #调用name_to_number函数
    if player_choice_number==comp_number:  #平局是输出“您和计算机出的一样呢”
        return "您和计算机出的一样呢"
    elif (player_choice_number==0 and comp_choice==3) or (player_choice_number==0 and comp_number==4):
        return "您赢了"
    elif (player_choice_number==1 and comp_number==4) or (player_choice_number==1 and comp_number==0):
        return "您赢了"
    elif (player_choice_number==2 and comp_number==0) or (player_choice_number==2 and comp_number==1):
        return "您赢了"
    elif (player_choice_number==3 and comp_number==1) or (player_choice_number==3 and comp_number==2):
        return "您赢了"
    elif (player_choice_number==4 and comp_number==2) or (player_choice_number==4 and comp_number==3):
        return "您赢了"
    else:
        return "计算机赢了"
    #"""
    #用户玩家任意给出一个选择，根据RPSLS游戏规则，在屏幕上输出对应的结果

    #"""


    # 输出"-------- "进行分割
    # 显示用户输入提示，用户通过键盘将自己的游戏选择对象输入，存入变量player_choice

    # 调用name_to_number()函数将用户的游戏选择对象转换为相应的整数，存入变量player_choice_number

    # 利用random.randrange()自动产生0-4之间的随机整数，作为计算机随机选择的游戏对象，存入变量comp_number

    # 调用number_to_name()函数将计算机产生的随机数转换为对应的游戏对象

    # 在屏幕上显示计算机选择的随机对象

    # 利用if/elif/else 语句，根据RPSLS规则对用户选择和计算机选择进行判断，并在屏幕上显示判断结果

    # 如果用户和计算机选择一样，则显示“您和计算机出的一样呢”，如果用户获胜，则显示“您赢了”，反之则显示“计算机赢了”


#对程序进行测试
print("欢迎使用RPSLS游戏")
print("----------------")
player_choice=str(input("请输入您的选择："))
print("----------------")
player_choice_number=name_to_number(player_choice) #调用name_to_number函数
if (player_choice_number!=0) and (player_choice_number!=1) and (player_choice_number!=2) and (player_choice_number!=3) and (player_choice_number!=4):
    print("Error: No Correct Name")  #用if语句对不按要求输入对应对象的情况显示“Error: No Correct Name"
else:  #对于其他按要求输入相应对象的情况，正常运行程序
    print("您的选择为：" + str(player_choice))
    import random #利用random.randrange()自动产生0-4之间的随机整数，作为计算机随机选择的游戏对象
    comp_number = random.randrange(0,4,1)
    comp_choice=number_to_name(comp_number) #调用number_to_name函数，对计算机产生的随机数进行转换，转换为相应对象
    print("计算机的选择为："+str(comp_choice))
    choice_name=rpsls(player_choice) #调用rpsls函数，得到游戏胜负结果
    print(choice_name)




