#!/bin/python

import settings

import requests, json, argparse
from argparse import RawTextHelpFormatter

headers = {'Authorization': 'token ' + settings.GITHUB_TOKEN}

def project_loop_milestones (project, repo_list):
    print ""
    print "***********************"
    print "%s"%(project)
    print "***********************"
    for repo in repo_list:
        if args.clean:
            repo_clean_milestones(repo)
        for milestone in settings.milestone_list:
            url = 'https://api.github.com/repos/%s/%s/milestones' % (settings.OWNER, repo)
            payload = {'title': milestone}
            r = requests.post(url, headers=headers, data=json.dumps(payload))
            print "called %s for milestone %s" % (r.url, milestone)

def repo_clean_milestones(repo):
    url = 'https://api.github.com/repos/%s/%s/milestones' % (settings.OWNER, repo)
    r = requests.get(url, headers=headers)
    for m in r.json():
        if m.get('title') not in settings.milestone_list:
            url = 'https://api.github.com/repos/%s/%s/milestones/%d' % (settings.OWNER, repo, m.get('number'))
            r = requests.delete(url, headers=headers)
            print "called %s to delete milestone %s" % (r.url, m.get('title'))

def project_loop_labels (project, repo_list):
    print ""
    print "***********************"
    print "%s"%(project)
    print "***********************"
    for repo in repo_list:
        if args.clean:
            repo_clean_labels(repo)
        for label in settings.label_dictionnary:
            url = 'https://api.github.com/repos/%s/%s/labels' % (settings.OWNER, repo)
            payload = {'name': label, 'color': settings.label_dictionnary[label]}
            r = requests.post(url, headers=headers, data=json.dumps(payload))
            print "called %s for label %s" % (r.url, label)

def repo_clean_labels(repo):
    url = 'https://api.github.com/repos/%s/%s/labels' % (settings.OWNER, repo)
    r = requests.get(url, headers=headers)
    for l in r.json():
        if l.get('name') not in settings.label_dictionnary:
            url = 'https://api.github.com/repos/%s/%s/labels/%s' % (settings.OWNER, repo, l.get('name'))
            r = requests.delete(url, headers=headers)
            print "called %s to delete label %s" % (r.url, l.get('name'))

epilog = 'Milestones:\n'
for milestone in settings.milestone_list:
    epilog += '    %s\n' % milestone
epilog += '\nLabels:\n'
for label in settings.label_dictionnary:
    epilog += '    %s\n' % label

parser = argparse.ArgumentParser(prog='github_script.py', description='Add Milestones or Labels to Github projects', 
        formatter_class=RawTextHelpFormatter, epilog=epilog)
parser.add_argument('-m', '--milestone', action='store_true', help='Add the list of milestones to the repos')
parser.add_argument('-l', '--label', action='store_true', help='Add the list of labels to the repos')
parser.add_argument('-c', '--clean', action='store_true', help='Clean the labels and/or milestones (if -l or -m '
                            'had been set) of the repos: Remove the labels or milestones that are not in the lists')
parser.add_argument('project', choices=['p1', 'p2'], help='select one project:\n' # <--------------------REPLACE project names
                                                          'p1 = Project 1\n'      # <--|
                                                          'p2 = Project 2')       # <--|
args = parser.parse_args()

if args.milestone:
    if args.project == 'p1':                                          # <----REPLACE project names
        project_loop_milestones("Project 1", settings.project1_list)  # <--|
    if args.project == 'p2':                                          # <--|
        project_loop_milestones("Project 2", settings.project2_list)  # <--|

if args.label:
    if args.project == 'p1':                                          # <----REPLACE project names
        project_loop_labels("Project 1", settings.project1_list)      # <--|
    if args.project == 'p2':                                          # <--|
        project_loop_labels("Project 2", settings.project2_list)      # <--|

