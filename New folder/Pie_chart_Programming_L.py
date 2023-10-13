#!/usr/bin/env python3

# ** Import pandas as pd  and read udemy.csv file and store in value name "dataS" **
import pandas as pd 
import matplotlib.pyplot as plt
dataS = pd.read_csv('udemy.csv')

def main():
    num_l = ['Javascript','Python','Go','Java','Kotlin','PHP','C#','Swift','R','Ruby','C','C++','Matlab','TypeScript','Scala','SQL','HTML','CSS','NoSQL','Rust','Perl']
    nud_n = []
    course_title = dataS['course title']
    # print(course_title)
    for i in num_l:
        nub = 0
        for j in course_title:
            if (type(j) == str)and(i in j) :
                nub += 1
        nud_n.append(nub)
    start = 0
    for i in range(len(nud_n)):
        if nud_n[start] == 0:
            nud_n.pop(start)
            num_l.pop(start)
            continue
        start+=1
    # str1 = 'thar is the best'
    colors = ['blue', 'lightcoral', 'lightgreen', 'lightpink', 'lightsalmon', 'lightblue', 'pink', 'cyan', 'lime', 'yellow', 'violet', 'orange', 'skyblue'] 
    explode = (0.05, 0.05, 0.35, 0.25, 0.15, 0.05, 0.1, 0.05, 0.05, 0.05, 0.25, 0.35, 0.5)
    print(nud_n)
    print(num_l)
    # plt.figure(figsize=(8, 7))
    plt.pie(nud_n, labels = num_l, colors=colors,startangle = 120, 
            shadow = False, explode = explode, autopct = '%1.1f%%') 
    plt.title('Program')
    plt.legend() 
    plt.show()




if __name__ == '__main__':
    main()