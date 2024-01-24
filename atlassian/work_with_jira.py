from atlassian import Jira
import requests

'''
Create a JIRA ticket using atlassian api
'''
jira = Jira(

    url='<atlassian-url>',

    username='<emailid  with atlassian>,
    password='<API_KEY_created_on_atlassian>',

    cloud=True)


##Running a JQL query
#jql_request ='project = XYZ AND issuetype = Task'

#issues = jira.jql(jql_request)

#print(issues["issues"][0]["fields"])

#try:
    ######### Create a new JIRA

# dep_body={
#     "issuetype": {'name': 'Task'},
#     "summary": "Creating JIRA story.",
#     "project": {"key":"DEV"}
# }

## Access JIRA project data
jira_prj=jira.get_project("DEV")
pd=jira_prj.values()
#print(pd)

########### Following work is to update an existing DEV JIRA story
new_dep=jira.get_issue("DEV-612")


### Update JIRA with following dictionary of data
dep_update={
    "description": "Execute following steps\n. Hello 2nd line.\n Hello 3rd line",
    "assignee": {'id':'5da9fec9f406020c3b181bb5'},
    "components":[{"name":"test1"},{"name":"test2"}] ## test1 and test2 components are already created in DEV JIRA project.
}

## Can update multiple JIRA issues with following statement.
retval=jira.bulk_update_issue_field([new_dep["key"]],fields=dep_update)
print(retval)
if retval:
    print("JIRA issue ",new_dep["key"]," updated")
else:
    print("Bulk update failed for ",new_dep["key"])


