import os
import sys
import subprocess

log_path = sys.argv[1]
edge_path = sys.argv[2]

commits_log = open(log_path).read().replace("STARTOFTHECOMMIT:", "", 1).split("STARTOFTHECOMMIT:")
print(len(commits_log))
file_t_author = {}
for commit in commits_log:
    commit = commit.strip("\n")
    commit = commit.replace("\n\n", "\n")
    commit = commit.replace("\n", ";")
    commit = commit.split(";")
    sha, name, email, t = commit[0], commit[1], commit[2], int(commit[3])
    if (len(commit) > 4):
        for file in commit[4:]:
            if file not in file_t_author.keys():
                file_t_author[file] = {}
            file_t_author[file][t] = name
print(len(file_t_author))

knowledge_trans = {}
for k, v in file_t_author.items():
    v = sorted(v.items(), key=lambda x: x[0])
    for i in range(len(v)):
        for j in range(i+1, len(v)):
            contr1 = v[i][1]
            contr2 = v[j][1]
            if(contr1 != contr2):
                if contr1 not in  knowledge_trans.keys():
                    knowledge_trans[contr1] = {}
                if contr2 not in knowledge_trans[contr1].keys():
                    knowledge_trans[contr1][contr2] = 0
                knowledge_trans[contr1][contr2] = knowledge_trans[contr1][contr2] + 1

f = open(edge_path, 'w')
for k, v in knowledge_trans.items():
    for i, j in knowledge_trans[k].items():
        f.write(k+';'+i+';'+str(j)+'\n')
f.close()