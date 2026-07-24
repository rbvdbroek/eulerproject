import webbrowser

base_site = r"https://projecteuler.net/problem="
edge_path = r"C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Microsoft Edge.lnk"
import datetime

x = datetime.datetime.now()
date_var = x.year*x.month*x.day
# print(date_var%1000)
task_num = date_var%1000
problem_url = base_site + str(task_num)


print(f'goint to {problem_url}, press anything to continue')
# input()

with open(fr"D:\Python\eulerproject\tasks\task_{task_num}.py", "w") as file:
    file.write("Hello, World!")

webbrowser.open(problem_url)
