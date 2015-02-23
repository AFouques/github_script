#!/bin/python

import requests, json, argparse
from argparse import RawTextHelpFormatter

GITHUB_TOKEN = '<YOUR GITHUB TOKEN>' # <------------------------REPLACE
OWNER = "<YOUR / YOUR COMPANY GITHUB ACCOUNT NAME>"# <----------REPLACE

headers = {'Authorization': 'token ' + GITHUB_TOKEN}

project1_list = [ "repo1",# <--------------------REPLACE names and args
                "repo2"]  # <--|
                          #    |
project2_list = [ "repo3",# <--|
                "repo4"]  # <--|

milestone_list = [ "Milestone1",# <------------REPLACE milestones names
    "Milestone2" ]              # <--|
label_dictionnary = {
    "Label1"   :"FF0000",# <------------REPLACE labels names and colors
    "Label2" :"00FF00"   # <--|
}

def project_loop_milestones (project, repo_list):
    print ""
    print "***********************"
    print "%s"%(project)
    print "***********************"
    for repo in repo_list:
        for milestone in milestone_list:
            url = 'https://api.github.com/repos/%s/%s/milestones' % (OWNER, repo)
            payload = {'title': milestone}
            r = requests.post(url, headers=headers, data=json.dumps(payload))
            print "called %s for milestone %s" % (r.url, milestone)

def project_loop_labels (project, repo_list):
    print ""
    print "***********************"
    print "%s"%(project)
    print "***********************"
    for repo in repo_list:
        for label in label_dictionnary:
            url = 'https://api.github.com/repos/%s/%s/labels' % (OWNER, repo)
            payload = {'name': label, 'color': label_dictionnary[label]}
            r = requests.post(url, headers=headers, data=json.dumps(payload))
            print "called %s for label %s" % (r.url, label)

epilog = 'Milestones:\n'
for milestone in milestone_list:
    epilog += '    %s\n' % milestone
epilog += '\nLabels:\n'
for label in label_dictionnary:
    epilog += '    %s\n' % label

parser = argparse.ArgumentParser(prog='github_script.py', description='Add Milestones or Labels to Github projects', 
        formatter_class=RawTextHelpFormatter, epilog=epilog)
parser.add_argument('-m', '--milestone', action='store_true', help='Add the list of milestones to the repos')
parser.add_argument('-l', '--label', action='store_true', help='Add the list of labels to the repos')
parser.add_argument('project', choices=['p1', 'p2'], help='select one project:\n' # <--------------------REPLACE project names
                                                          'p1 = Project 1\n'      # <--|
                                                          'p2 = Project 2')       # <--|
args = parser.parse_args()

if args.milestone:
    if args.project == 'p1':                                 # <--------------------REPLACE project names
        project_loop_milestones("Project 1", project1_list)  # <--|
    if args.project == 'p2':                                 # <--|
        project_loop_milestones("Project 2", project2_list)  # <--|

if args.label:
    if args.project == 'p1':                                 # <--------------------REPLACE project names
        project_loop_labels("Project 1", project1_list)      # <--|
    if args.project == 'p2':                                 # <--|
        project_loop_labels("Project 2", project2_list)      # <--|

