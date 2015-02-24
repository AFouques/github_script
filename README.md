# github_script

usage: ```github_script.py [-h] [-m] [-l] [-c] {p1,p2}```

Add Milestones or Labels to Github projects

###positional arguments:
```
    {p1,p2}          select one project:
                     p1 = Project 1
                     p2 = Project 2
```

###optional arguments:
```
    -h, --help        show this help message and exit
    -m, --milestone   Add the list of milestones to the repos
    -l, --label       Add the list of labels to the repos
    -c, --clean       Clean the labels and/or milestones (if -l or -m had been set) of the repos: Remove the labels or milestones that are not in the lists
```

###Milestones:
```
    Milestone1
    Milestone2
```

###Labels:
```
    Label1
    Label2
```

##How to use it:
in the file settings.py, 
- REPLACE the Github Token by yours (created here : https://github.com/settings/applications#personal-access-tokens > "Generate new token")
- REPLACE your / your company github account name
- REPLACE project names, command and associated repos
- REPLACE milestones names
- REPLACE labels names and colors

set the script executable: 

```#chmod +x github_script.py```

execute the code as explained above
