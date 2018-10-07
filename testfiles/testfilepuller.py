from github import Github
import random
import os
import shutil

with open('creds.txt', 'r') as f:
    creds = f.read().split()

g = Github(creds[0], creds[1])

search = g.search_repositories("language:javascript")
resultslist = []

for i in range(2):
    resultslist.append(search[random.randint(0,100)])

print(resultslist)
for i in resultslist:
    print(i.git_url)

os.system('git clone {}'.format(resultslist[0].git_url))

input("Press Enter to continue...")

for i in os.listdir():
    if os.path.isdir(i):
        shutil.rmtree(i)
