#!/usr/bin/env python3

# ** Inmport pandas as pd  and read udemy.csv file and store in value name "dataS" **
import pandas as pd 
import matplotlib.pyplot as plt
import numpy as np
dataS = pd.read_csv('udemy.csv')
# ** clean dataS In the section name 'course level' **
dataS = dataS[dataS['course level'] != 'Current price: $16.99']
dataS = dataS[dataS['course level'] != 'Current price: $19.99']
# dataS = dataS[dataS['reviews'] != '0 reviews']

def main():
    n = int(input())
    list_data = make_Data(n)
    make_graph(list_data)
    #################################################################
    #ตัวอย่าง#
    # y = dataS[dataS['instructors'] == 'Spotle Learn']
    # print(y)


def make_Data(n):
    x = dataS['instructors'].value_counts().head(n)
    instructors = []
    num_inst = []
    for i in dataS['instructors']:
        if i in instructors:
            continue
        else:
            instructors.append(i)
    for i in instructors:
        nub = 0
        for j in dataS['instructors']:
            if i == j:
                nub += 1
        num_inst.append(nub)
    result = []
    for i in x:
        inD = num_inst.index(i)
        name = instructors[inD]
        sum_rate = 0
        data = dataS[dataS['instructors'] == name]
        rate = data['Ratings'].apply(lambda x : x[8:11])
        max_rate = 0
        for j in rate:
            if j != 'ws' :
                fj = float(j)
                sum_rate += fj
                if fj > max_rate:
                    max_rate = fj
        result.append([name,round(sum_rate/i,2),max_rate,i])
        num_inst[inD] = 0
    return result


def make_graph(list_d):
    left = [] 
    average_rate = []
    name_instr = []
    max_rate = []
    for i in range(len(list_d)):
        left.append(i+1)
        average_rate.append(list_d[i][1])
        name_instr.append(list_d[i][0])
        max_rate.append(list_d[i][2])

    # t = {'Average': average_rate,'Max' : max_rate}
    # tf = pd.DataFrame(t,columns=['Average','Max'],index=name_instr)
    # plt.figure(figsize=(15,40))
    # tf.plot.bar()
    # plt.savefig('have 0 reviews.png')
    # plt.show()

    # AVERAGE_RATE REVIEW 0
    plt.figure(1)
    plt.bar(left, average_rate, tick_label = name_instr,
        width = 0.8, color = ['Orange', 'Yellow'], label='Average')
    plt.xticks(rotation = 90)
    plt.xlabel('Instructor')
    plt.ylabel('Average_rate')
    plt.title('AVERAGE_RATE HAVE REVIEW 0')
    plt.legend() 
    plt.show()

    # MAX_RATE HAVE REVIEW 0
    plt.figure(2)
    plt.bar(left, max_rate ,tick_label = name_instr,
        width = 0.8, color = ['Blue', 'Skyblue'], label='Max')
    plt.xticks(rotation = 90)
    plt.xlabel('Instructor')
    plt.ylabel('Max_rate')
    plt.title('MAX_RATE HAVE REVIEW 0')
    plt.show()

    # AVERAGE_MAX_RATE HAVE REVIEW 0
    plt.figure(3)
    plt.bar(left, average_rate ,tick_label = max_rate,
        width = 0.8, color = ['Purple', 'yellow'])
    plt.xticks(rotation = 0)
    plt.xlabel('Max_Rate')
    plt.ylabel('Average_rate')
    plt.title('AVERAGE_MAX_RATE HAVE REVIEW 0')
    plt.show()

    plt.figure(4)
    bar_width = 0.35
    x = np.arange(len(name_instr))
    plt.bar(x - bar_width/2, average_rate, bar_width, label='Average', color = 'Red')
    plt.bar(x + bar_width/2, max_rate, bar_width, label='Maxrate', color = 'lightcoral')
    plt.xticks(rotation = 90)
    plt.xlabel('Instructor')
    plt.ylabel('')    
    plt.title('AVERAGE_MAX_COMPARE HAVE REVIEW 0')
    plt.xticks(x, name_instr)
    plt.legend()
    plt.show()

if __name__ == '__main__':
    main()