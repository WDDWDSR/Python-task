#coding:gbk
"""
��һ��С��Ŀ��Rock-paper-scissors-lizard-Spock
����Ŀ�ģ�����python�������RPSLS��Ϸ
���ߣ������
���ڣ�2021/11/27
"""

import random



# 0 - ʯͷ
# 1 - ʷ����
# 2 - ��
# 3 - ����
# 4 - ����

# ����Ϊ�����Ϸ����Ҫ�õ����Զ��庯��

def name_to_number(name):    #�Զ��庯��name_to_numberʵ�ֽ���Ϸ�����Ӧ����ͬ����
    if name=="ʯͷ":
        return 0
    elif name=="ʷ����":
        return 1
    elif name=="��":
        return 2
    elif name=="����":
        return 3
    elif name=="����":
        return 4


    #"""
    #����Ϸ�����Ӧ����ͬ������
    #"""

    # ʹ��if/elif/else��佫����Ϸ�����Ӧ����ͬ������
    # ��Ҫ���Ƿ��ؽ��





def number_to_name(comp_number):   #�Զ���num_to_name����������ͬ������Ӧ����Ϸ�Ĳ�ͬ����
    if comp_number==0:
        return "ʯͷ"
    elif comp_number==1:
        return "ʷ����"
    elif comp_number==2:
        return "��"
    elif comp_number==3:
        return "����"
    elif comp_number==4:
        return "����"
    """
    ������ (0, 1, 2, 3, or 4)��Ӧ����Ϸ�Ĳ�ͬ����
    """

    # ʹ��if/elif/else��佫��ͬ��������Ӧ����Ϸ�Ĳ�ͬ����
    # ��Ҫ���Ƿ��ؽ��




def rpsls(player_choice):       #�Զ��庯��rpsls��ͨ�����������Ķ���ת��Ϊ������������������ɵ����ֱȽϣ�����rpsls�������ʤ���ж�
    player_choice_number = name_to_number(player_choice)  #����name_to_number����
    if player_choice_number==comp_number:  #ƽ������������ͼ��������һ���ء�
        return "���ͼ��������һ����"
    elif (player_choice_number==0 and comp_choice==3) or (player_choice_number==0 and comp_number==4):
        return "��Ӯ��"
    elif (player_choice_number==1 and comp_number==4) or (player_choice_number==1 and comp_number==0):
        return "��Ӯ��"
    elif (player_choice_number==2 and comp_number==0) or (player_choice_number==2 and comp_number==1):
        return "��Ӯ��"
    elif (player_choice_number==3 and comp_number==1) or (player_choice_number==3 and comp_number==2):
        return "��Ӯ��"
    elif (player_choice_number==4 and comp_number==2) or (player_choice_number==4 and comp_number==3):
        return "��Ӯ��"
    else:
        return "�����Ӯ��"
    #"""
    #�û�����������һ��ѡ�񣬸���RPSLS��Ϸ��������Ļ�������Ӧ�Ľ��

    #"""


    # ���"-------- "���зָ�
    # ��ʾ�û�������ʾ���û�ͨ�����̽��Լ�����Ϸѡ��������룬�������player_choice

    # ����name_to_number()�������û�����Ϸѡ�����ת��Ϊ��Ӧ���������������player_choice_number

    # ����random.randrange()�Զ�����0-4֮��������������Ϊ��������ѡ�����Ϸ���󣬴������comp_number

    # ����number_to_name()����������������������ת��Ϊ��Ӧ����Ϸ����

    # ����Ļ����ʾ�����ѡ����������

    # ����if/elif/else ��䣬����RPSLS������û�ѡ��ͼ����ѡ������жϣ�������Ļ����ʾ�жϽ��

    # ����û��ͼ����ѡ��һ��������ʾ�����ͼ��������һ���ء�������û���ʤ������ʾ����Ӯ�ˡ�����֮����ʾ�������Ӯ�ˡ�


#�Գ�����в���
print("��ӭʹ��RPSLS��Ϸ")
print("----------------")
player_choice=str(input("����������ѡ��"))
print("----------------")
player_choice_number=name_to_number(player_choice) #����name_to_number����
if (player_choice_number!=0) and (player_choice_number!=1) and (player_choice_number!=2) and (player_choice_number!=3) and (player_choice_number!=4):
    print("Error: No Correct Name")  #��if���Բ���Ҫ�������Ӧ����������ʾ��Error: No Correct Name"
else:  #����������Ҫ��������Ӧ�����������������г���
    print("����ѡ��Ϊ��" + str(player_choice))
    import random #����random.randrange()�Զ�����0-4֮��������������Ϊ��������ѡ�����Ϸ����
    comp_number = random.randrange(0,4,1)
    comp_choice=number_to_name(comp_number) #����number_to_name�������Լ�������������������ת����ת��Ϊ��Ӧ����
    print("�������ѡ��Ϊ��"+str(comp_choice))
    choice_name=rpsls(player_choice) #����rpsls�������õ���Ϸʤ�����
    print(choice_name)




