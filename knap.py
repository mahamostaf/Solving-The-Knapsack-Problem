from random import randint, random
import tkinter as tk
from functools import partial


def calculate(out1, out2, cap, w0, v0):
    capacity = cap.get()
    w = w0.get()
    v = v0.get()
    weight = w.split()
    val = v.split()


    count = 0
    for k in range(len(weight)):
        if len(capacity) > 0:
            if int(weight[k]) > (int(capacity)):
                count += 1

    if (len(capacity) == 0) | (len(w) == 0) | (len(v) == 0):
        print(len(capacity))
        out1.set("Please Fill All The Text Fields")
        out2.set("")

    elif len(weight) != len(val):
        out1.set("Please Fill The Fileds Where The Number of weights \n"
                 " must be equal to The Number of values")
        out2.set("")

    elif count == len(weight):
        out1.set("Sorry, You Won't be able Fill The Knapsack With Any Item")
        out2.set("")
    else:
        for k in range(len(weight)):
            weight[k] = int(weight[k])
            val[k] = int(val[k])
        capacity = int(capacity)
        pop = [[], [], [], [], [], [], [], [], [], []]
        feasPop = [[], [], [], [], [], [], [], [], [], []]

        for i in range(10):
            for j in range(len(weight)):
                pop[i].append(randint(0, 1))

        for i in range(10):
            sum1 = 0
            for j in range(len(weight)):
                if pop[i][j] == 1:
                    sum1 += weight[j]
            if sum1 <= capacity:
                feasPop[i] = pop[i].copy()
            else:
                for n in range(len(pop[i])):
                    if pop[i][n] == 1:
                        pop[i][n] = 0
                        sum1 -= weight[n]
                    if sum1 <= capacity:
                        feasPop[i] = pop[i].copy()
                        break
                    else:
                        pop[i][n] = 1

        p4 = feasPop[randint(0, 9)]

        for i in range(500):
            p1 = feasPop[randint(0, 9)]
            p2 = feasPop[randint(0, 9)]
            p3 = feasPop[randint(0, 9)]

            CR = random()
            F = random()

            rand = []
            mut = []
            trial = []

            sumTrialWeight = 0
            sumTrialValue = 0
            sumTargetWeight = 0
            sumTargetValue = 0

            for k in range(len(weight)):

                mut.append(p3[k] + round(F * (max(p1[k], p2[k]) - min(p1[k], p2[k]))))
                if mut[k] == 2:
                    mut[k] = 1

                if p4[k] == 1:
                    sumTargetWeight += weight[k]
                    sumTargetValue += val[k]

                rand.append(random())

                if k == 0:
                    trial.append(mut[k])
                    if trial[k] == 1:
                        sumTrialWeight += weight[k]
                        sumTrialValue += val[k]
                    continue
                if rand[k] >= CR:
                    trial.append(p4[k])
                else:
                    trial.append(mut[k])
                if trial[k] == 1:
                    sumTrialWeight += weight[k]
                    sumTrialValue += val[k]

            if (sumTrialWeight <= capacity) & (sumTrialValue > sumTargetValue):
                p4 = trial

        choices = []
        for s in range(len(weight)):
            if p4[s] == 1:
                choices.append(s + 1)
        out1.set("The Best Choice is to Fill The Knapsack by Item Number : ")
        for k in range(len(choices)):
            choices[k] = str(choices[k])
        out2.set(' , '.join(choices))
        return


root = tk.Tk()
root.geometry("400x400")
cap = tk.StringVar()
weights = tk.StringVar()
values = tk.StringVar()
res1 = tk.StringVar()
res2 = tk.StringVar()

label1 = tk.Label(root, text="Capacity", font=('calibre', 10, 'bold'))
label1.place(x=20, y=60)
entry1 = tk.Entry(root, textvariable=cap, font=('calibre', 10, 'normal'))
entry1.place(x=200, y=60)
label2 = tk.Label(root, text="Weights", font=('calibre', 10, 'bold'))
label2.place(x=20, y=120)
entry2 = tk.Entry(root, textvariable=weights, font=('calibre', 10, 'normal'))
entry2.place(x=200, y=120)
label3 = tk.Label(root, text="Values", font=('calibre', 10, 'bold'))
label3.place(x=20, y=180)
entry3 = tk.Entry(root, textvariable=values, font=('calibre', 10, 'normal'))
entry3.place(x=200, y=180)
output1 = tk.Label(root, textvariable=res1)
output1.place(x=30, y=300)
output2 = tk.Label(root, textvariable=res2)
output2.place(x=335, y=300)

calculate = partial(calculate, res1, res2, cap, weights, values)

button = tk.Button(root, text='calculate', command=calculate).place(x=100, y=230)
root.mainloop()

