import webbrowser

base_site = r"https://projecteuler.net/problem="
edge_path = r"C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Microsoft Edge.lnk"
import datetime

x = datetime.datetime.now()
date_var = x.year*x.month*x.day
# print(date_var%1000)

problem = base_site + str(date_var%1000)


print(f'goint to {problem}, press anything to continue')
input()

webbrowser.open(problem)
