##while True:
##    total = 0
##    for i in range (1, 6, 1):
##        marks = int(input("enter marks for subject{i}:"))
##        total = total + marks
##
##    average = total/5
##    print("average:",average)
##    if(average>=95):
##        print("Grade=A")
##    elif(average>=80):
##        print("Grade=B")
##    elif(average>=60):
##        print("Grade=C")
##    elif(average>=40):
##        print("Grade=D")
##    else:
##        print("Grade=F")
##
##    choice = input("Do you want to calculate grade for another student? (yes/no): ")
##    if choice.lower() !="yes":
##        print("Thank you. Program end.")
##        break


##Class_A = {"Advita" , "Krishna", "Jayesh" , "Manya"}
##Class_B = {"Krupa" , "Dhanashree" , "Chinmayi" , "Samruddhi"}
##print("Class A students:",Class_A)
##print("Class B students:",Class_B)
##print("--------------------------------------------------")
##
##union_students = Class_A.union(Class_B)
##print("Union(All students in either class):", union_students)
##
##common_students = Class_A.intersection(Class_B)
##print("Intersection (Common students):", common_students)
##
##unique_A = Class_A.difference(Class_B)
##print("Students only in Class A:", unique_A)
##
##unique_B = Class_B.difference(Class_A)
##print("Students only in Class B:", unique_B)
##
##student_name = "Riya"
##if student_name in Class_A:
##    print(student_name, "is in Class A")
##else:
##    print(student_name, "is not in Class A")
##
##student_name = "Rahul"
##if student_name in Class_B:
##    print(student_name, "is in Class B")
##else:
##    print(student_name, "is not in Class B")



##def factorial_normal(n):
##    fact = 1
##    for i in range(1, n+1):
##        fact *= i
##    return fact
##
##def factorial_recursive(n):
##    if n==0 or n==1:
##        return 1
##    else:
##        return n * factorial_recursive(n-1)
##
##num = int(input("Enter a number"))
##print("\nUsing normal function:")
##print(f"factorial of {num} = {factorial_normal(num)}")
##
##print("\nUsing recursive function:")
##print(f"factorial of {num} = {factorial_recursive(num)}")


    
##import pickle   
##
##
##def create_file(filename):
##    f = open(filename, "w")   
##    f.close()
##    print("File created successfully!")
##
##def write_file(filename):
##    data = input("Enter text to write in file: ")
##    f = open(filename, "w")
##    f.write(data)
##    f.close()
##    print("Data written successfully!")
##
##def read_file(filename):
##    f = open(filename, "r")
##    content = f.read()
##    f.close()
##    print("File Content:\n", content)
##
##def append_file(filename):
##    data = input("Enter text to append in file: ")
##    f = open(filename, "a")
##    f.write("\n" + data)
##    f.close()
##    print("Data appended successfully!")
##
##
##def write_binary_file(filename):
##    data = [101, "FYIT", "File Handling", 99.99]
##    f = open(filename, "wb")
##    pickle.dump(data, f)   
##    f.close()
##    print("Binary data written successfully!")
##
##def read_binary_file(filename):
##    f = open(filename, "rb")
##    data = pickle.load(f)
##    f.close()
##    print("Reading from Binary File:\n", data)
##
##
##if __name__ == "__main__":
##    text_file = "sample.txt"
##    binary_file = "data.bin"
##
##    while True:
##        print("\n--- FILE HANDLING MENU ---")
##        print("1. Create File")
##        print("2. Write Data to File")
##        print("3. Read Data from File")
##        print("4. Append Data to File")
##        print("5. Write Binary File")
##        print("6. Read Binary File")
##        print("7. Exit")
##
##        choice = int(input("Enter your choice: "))
##
##        if choice == 1:
##            create_file(text_file)
##        elif choice == 2:
##            write_file(text_file)
##        elif choice == 3:
##            read_file(text_file)
##        elif choice == 4:
##            append_file(text_file)
##        elif choice == 5:
##            write_binary_file(binary_file)
##        elif choice == 6:
##            read_binary_file(binary_file)
##        elif choice == 7:
##            print("Exiting Program...")
##            break
##        else:
##            print("Invalid Choice! Try again.")


##import matplotlib.pyplot as plt
##import numpy as np  
##
##
##x = np.random.rand(20)  
##y = np.random.rand(20)   
##
##plt.scatter(x, y, color='blue')
##plt.title("Scatter Plot - Random Points")
##plt.xlabel("X Axis")
##plt.ylabel("Y Axis")
##plt.show()
##
##
##subjects = ["Math", "Science", "English", "History", "IT"]
##marks = [80, 70, 90, 60, 85]
##
##plt.bar(subjects, marks, color='green')
##plt.title("Bar Chart - Student Marks")
##plt.xlabel("Subjects")
##plt.ylabel("Marks")
##plt.show()
##
##
##fruits = ["Apples", "Bananas", "Mangoes", "Grapes", "Oranges"]
##quantity = [20, 15, 25, 10, 30]
##
##plt.pie(quantity, labels=fruits, autopct='%1.1f%%')
##plt.title("Pie Chart - Fruit Distribution")
##plt.show()
##
##
##days = [1, 2, 3, 4, 5, 6, 7]
##sales = [5, 10, 7, 12, 15, 20, 25]
##
##plt.plot(days, sales, marker='o', color='red')
##plt.title("Line Chart - Sales Over a Week")
##plt.xlabel("Days")
##plt.ylabel("Sales")
##plt.show()


##import tkinter as tk
##
##root = tk.Tk()
##root.title("Button Example")
##
##btn1 = tk.Button(root, text="Normal Button")
##btn1.pack()
##
##btn2 = tk.Button(root, text="Big Button", width=20, height=2)
##btn2.pack()
##
##btn3 = tk.Button(root, text="Red Button", bg="red", fg="white")
##btn3.pack()
##
##btn4 = tk.Button(root, text="Disabled", state="disabled")
##btn4.pack()
##
##root.mainloop()



import tkinter as tk

def click(symbol):
    entry.insert(tk.END, str(symbol))

def clear():
    entry.delete(0, tk.END)

def calculate():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(0, str(result))
    except:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

root = tk.Tk()
root.title("Calculator")


entry = tk.Entry(root, width=20, font=("Arial", 16))
entry.grid(row=0, column=0, columnspan=4)

buttons = [
    ('7',1,0),('8',1,1),('9',1,2),('+',1,3),
    ('4',2,0),('5',2,1),('6',2,2),('-',2,3),
    ('1',3,0),('2',3,1),('3',3,2),('*',3,3),
    ('0',4,0),('.',4,1),('/',4,2),('=',4,3)
]

for (txt,r,c) in buttons:
    if txt == '=':
        tk.Button(root, text=txt, width=5, height=2, command=calculate).grid(row=r, column=c)
    else:
        tk.Button(root, text=txt, width=5, height=2, command=lambda t=txt: click(t)).grid(row=r, column=c)


tk.Button(root, text="C", width=22, height=2, command=clear).grid(row=5, column=0, columnspan=4)

root.mainloop()
        
        
          
    
