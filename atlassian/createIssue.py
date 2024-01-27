from atlassian import Jira
import json
import sys
import argparse

arg_parser= argparse.ArgumentParser()
arg_parser.add_argument("-p","--project",type=str,default="DEV")
arg_parser.add_argument("-e","--env",type=str,default="QA") # 
arg_parser.add_argument("-d","--desc",type=str,default="devops")
arg_parser.add_argument("-a","--assignee",type=str,default="mike")
args = arg_parser.parse_args()

print("Project =",args.project)
print("Environment = ",args.env)
print("description = ",args.desc)
print("assignee = ",args.assignee)


jira = Jira(

    url='<atlassian_url>',

    username='<email>',
    password='<atlassian_api_token>',

    cloud=True)

dep_body={
    "issuetype": {'name': 'Task'},
    "summary": "Creating DEV for batch run.",
    "project": {"key":"DEV"},
}

new_dep=jira.create_issue(fields=dep_body)
print(new_dep)

print("Created new DEV ticket ",new_dep["key"]," .")
