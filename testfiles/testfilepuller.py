from github import Github
import random
import os
import shutil

with open('creds.txt', 'r') as f:
    creds = f.read().split()

g = Github(creds[0], creds[1])

for i in ["javascript", "java", "python", "c++", "html"]:
    search = g.search_repositories("language:{} size:<10".format(i))
    os.system('git clone {}'.format(search[random.randint(0,99)].git_url))
    os.system('git clone {}'.format(search[random.randint(100,199)].git_url))

print("\nNow you can open each project in Atom and test your theme.\n\
Use the SyntaxThemeTester package to aid in this.")

input("When you're done, press Enter to continue. This will delete all of the \
cloned repositories.")

for i in os.listdir():
    if os.path.isdir(i):
        shutil.rmtree(i)
