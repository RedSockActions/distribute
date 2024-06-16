import git
import os

repos = []

rp = os.environ['REPOS'].split(',')
keys = os.environ['KEYS'].split(',')

for idx, _ in enumerate(rp):
    repos.append([rp[idx], keys[idx]])

repo = git.Repo('./')
