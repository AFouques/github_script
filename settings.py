#!/bin/python

GITHUB_TOKEN = '<YOUR GITHUB TOKEN>'
OWNER = '<YOUR / YOUR COMPANY GITHUB ACCOUNT NAME>'

PROJECTS = [{
        'name'    : 'Project 1',
        'command' : 'p1',
        'repos'   : [ 'repo1',
                      'repo2' ]
            },
            {
        'name'    : 'Project 2',
        'command' : 'p2',
        'repos'   : [ 'repo3',
                      'repo4' ]
            }]

milestone_list = [
    'Milestone 1',
    'Milestone 2' ]
label_dictionnary = {
    'Label 1' : 'FF0000',
    'Label 2' : '00FF00'
}
