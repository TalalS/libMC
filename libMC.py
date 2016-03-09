# /usr/bin/env python
import sys
import core.user
import core.server
import core.projects
import core.config
from core import ErrorMessage

"""
    {
        "success": true
    }
    {
        "success": false,
        "detail": " Error !!!"
    }
"""


def main(argv):

    if argv[0] == "login":  # ex, login t.sariiriI@modsoft.io 123456
        email = argv[1]
        password = argv[2]
        user = core.user.User()
        return user.login(email=email, password=password)

    elif argv[0] == "uploadProject":  # ex, uploadProject projectName
        projectname = argv[1]
        project = core.projects.Project(projectname)
        return project.upload()
    elif argv[0] == "signout":
        signout = core.user.User()
        return signout.signout()
    elif argv[0] == "downloadProject":  # ex, downloadProject projectName
        projectname = argv[1]
        downloadProject = core.projects.Project(projectname)
        return downloadProject.downloadProject()
    elif argv[0] == "deleteProject":    # ex, deleteProject projectName
        projectname = argv[1]
        deleteProject = core.projects.Project(projectname)
        return deleteProject.removeProject()
    elif argv[0] == "runProject":   # ex, runProject projectName user
        projectname = argv[1]
        userrun = argv[2]
        return core.server.runServer(projectname, userrun)
    elif argv[0] == "createProject":    # ex, createProject projectname dataBaseName environment projectPath
        projectname = argv[1]
        dataBaseName = argv[2]
        environment = argv[3]
        projectPath = argv[4]
        createProject = core.projects.Project(projectname)
        return createProject.setupNewProject(dataBaseName, environment, projectPath)
    elif argv[0] == "getProjects":
        return core.projects.Project(None).listProjects()
    elif argv[0] == "getProject":   # ex, projectName
        projectname = argv[1]
        getProject = core.projects.Project(projectname)
        return getProject.getLocalProjectData()
    elif argv[0] == "syncProjects":     # ex, syncProjects
        syncProjects = core.projects.Project(None)
        return syncProjects.getProjectsFromCloud()
    elif argv[0] == "getUser":      # ex, projectName
        projectname = argv[1]
        getUser = core.projects.Project(projectname)
        return getUser.checkIfUserIsLoggedIn()
    elif argv[0] == "getToken":
        user = core.user.User()
        return user.token()
    elif argv[0] == "checkUpdates":     # ex, Logpath
        logpath = argv[1]
        checkUpdates = core.config.debug(logpath)
        return checkUpdates.checkForUpdates()


def printResponse(response):
    success = True
    if isinstance(response, ErrorMessage):
        success = False
    output = {
        "success": success,
        "detail": response
    }
    print output

if __name__ == '__main__':
    printResponse(main(sys.argv[1:]))
