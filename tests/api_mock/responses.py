server = {
    "version": "2019.2.4 (build 72059)",
    "versionMajor": 2019,
    "versionMinor": 2,
    "startTime": "20200805T190912+0300",
    "currentTime": "20201107T224939+0300",
    "buildNumber": "72059",
    "buildDate": "20200508T000000+0300",
    "internalId": "f5f45726-88a4-4366-b340-563da2e51407",
    "webUrl": "https://teamcity.com",
    "projects": {"href": "/app/rest/projects"},
    "vcsRoots": {"href": "/app/rest/vcs-roots"},
    "builds": {"href": "/app/rest/builds"},
    "users": {"href": "/app/rest/users"},
    "userGroups": {"href": "/app/rest/userGroups"},
    "agents": {"href": "/app/rest/agents"},
    "buildQueue": {"href": "/app/rest/buildQueue"},
    "agentPools": {"href": "/app/rest/agentPools"},
    "investigations": {"href": "/app/rest/investigations"},
    "mutes": {"href": "/app/rest/mutes"},
}

projects = {
    "count": 693,
    "href": "/app/rest/projects",
    "project": [
        {
            "id": "_Root",
            "name": "<Root project>",
            "description": "Contains all other projects",
            "href": "/app/rest/projects/id:_Root",
            "webUrl": "https://teamcity.com/project.html?projectId=_Root",
        },
        {
            "id": "Abc",
            "name": "ABC",
            "parentProjectId": "_Root",
            "description": "ABC Project",
            "href": "/app/rest/projects/id:Abc",
            "webUrl": "https://teamcity.com/project.html?projectId=Abc",
        },
        {
            "id": "Abc_Dependencies",
            "name": "Dependencies",
            "parentProjectId": "Abc",
            "description": "ABC Dependencies",
            "href": "/app/rest/projects/id:Abc_Dependencies",
            "webUrl": "https://teamcity.com/project.html?projectId=Abc_Dependencies",
        },
        {
            "id": "Abc_Dependencies_First",
            "name": "First Dependency",
            "parentProjectId": "Abc_Dependencies",
            "href": "/app/rest/projects/id:Abc_Dependencies_First",
            "webUrl": "https://teamcity.com/project.html?projectId=Abc_Dependencies_First",
        },
        {
            "id": "Abc_Dependencies_Second",
            "name": "Second Dependency",
            "parentProjectId": "Abc_Dependencies",
            "href": "/app/rest/projects/id:Abc_Dependencies_Second",
            "webUrl": "https://teamcity.com/project.html?projectId=Abc_Dependencies_Second",
        },
    ],
}

project = {
    "id": "Abc",
    "name": "ABC",
    "parentProjectId": "_Root",
    "description": "ABC",
    "href": "/app/rest/projects/id:Abc",
    "webUrl": "https://teamcity.com/project.html?projectId=Abc",
    "parentProject": {
        "id": "_Root",
        "name": "<Root project>",
        "description": "Contains all other projects",
        "href": "/app/rest/projects/id:_Root",
        "webUrl": "https://teamcity.com/project.html?projectId=_Root",
    },
    "buildTypes": {
        "count": 9,
        "buildType": [
            {
                "id": "Abc_Master",
                "name": "master",
                "description": "ABC master branch build",
                "projectName": "ABC",
                "projectId": "Abc",
                "href": "/app/rest/buildTypes/id:Abc_Master",
                "webUrl": "https://teamcity.com/viewType.html?buildTypeId=Abc_Master",
            },
            {
                "id": "Abc_Build",
                "name": "build",
                "description": "ABC non-master branch builds",
                "projectName": "ABC",
                "projectId": "Abc",
                "href": "/app/rest/buildTypes/id:Abc_Build",
                "webUrl": "https://teamcity.com/viewType.html?buildTypeId=Abc_Build",
            },
            {
                "id": "Abc_Release",
                "name": "release",
                "description": "release ABC builds",
                "projectName": "ABC",
                "projectId": "Abc",
                "href": "/app/rest/buildTypes/id:Abc_Release",
                "webUrl": "https://teamcity.com/viewType.html?buildTypeId=Abc_Release",
            },
        ],
    },
    "projects": {
        "count": 3,
        "project": [
            {
                "id": "Abc_Dependencies",
                "name": "Dependencies",
                "parentProjectId": "Abc",
                "description": "ABC Dependencies",
                "href": "/app/rest/projects/id:Abc_Dependencies",
                "webUrl": "https://teamcity.com/project.html?projectId=Abc_Dependencies",
            },
            {
                "id": "Abc_Packages",
                "name": "Packages",
                "parentProjectId": "Abc",
                "description": "ABC Packages",
                "href": "/app/rest/projects/id:Abc_Packages",
                "webUrl": "https://teamcity.com/project.html?projectId=Abc_Packages",
            },
            {
                "id": "Abc_Tests",
                "name": "Tests",
                "parentProjectId": "Abc",
                "description": "ABC Tests",
                "href": "/app/rest/projects/id:Abc_Tests",
                "webUrl": "https://teamcity.com/project.html?projectId=Abc_Tests",
            },
        ],
    },
}

vcs_roots = {
    "count": 10,
    "href": "/app/rest/vcs-roots?locator=count:10",
    "nextHref": "/app/rest/vcs-roots?locator=count:10,start:10",
    "vcs-root": [
        {"id": "Abc", "name": "ABC", "href": "/app/rest/vcs-roots/id:Abc"},
        {"id": "Abc1_2", "name": "ABC (1)", "href": "/app/rest/vcs-roots/id:Abc1_2"},
        {"id": "Abc2", "name": "ABC (2)", "href": "/app/rest/vcs-roots/id:Abc2"},
        {"id": "AbcCi", "name": "ABC CI", "href": "/app/rest/vcs-roots/id:AbcCi"},
        {
            "id": "Abc_Packages_AbcPackages",
            "name": "ABC packages",
            "href": "/app/rest/vcs-roots/id:Abc_Packages_AbcPackages",
        },
        {
            "id": "Abc_Packages_AbcPackages1",
            "name": "ABC packages (1)",
            "href": "/app/rest/vcs-roots/id:Abc_Packages_AbcPackages1",
        },
        {
            "id": "Abc_Packages_AbcPackages2",
            "name": "ABC packages (2)",
            "href": "/app/rest/vcs-roots/id:Abc_Packages_AbcPackages2",
        },
        {"id": "Abc1", "name": "ABC release", "href": "/app/rest/vcs-roots/id:Abc1"},
        {
            "id": "Abc_Tests_AbcTestMaster",
            "name": "ABC Test Master",
            "href": "/app/rest/vcs-roots/id:Abc_Tests_AbcTestMaster",
        },
        {
            "id": "Abc_Tests_AbcTestDefault",
            "name": "ABC Test Default",
            "href": "/app/rest/vcs-roots/id:Abc_Tests_AbcTestDefault",
        },
    ],
}

vcs_root = {
    "id": "Abc_Abc",
    "name": "ABC",
    "vcsName": "jetbrains.git",
    "modificationCheckInterval": 60,
    "href": "/app/rest/vcs-roots/id:Abc_Abc",
    "project": {
        "id": "Abc",
        "name": "ABC",
        "parentProjectId": "_Root",
        "description": "This is  ABC",
        "href": "/app/rest/projects/id:Abc",
        "webUrl": "https://teamcity.com/project.html?projectId=Abc",
    },
    "properties": {
        "count": 11,
        "property": [
            {"name": "agentCleanFilesPolicy", "value": "ALL_UNTRACKED"},
            {"name": "agentCleanPolicy", "value": "ON_BRANCH_CHANGE"},
            {"name": "authMethod", "value": "TEAMCITY_SSH_KEY"},
            {"name": "branch", "value": "master"},
            {"name": "ignoreKnownHosts", "value": "True"},
            {"name": "submoduleCheckout", "value": "CHECKOUT"},
            {"name": "teamcity:branchSpec", "value": "+:refs/heads/*"},
            {"name": "teamcitySshKey", "value": "GitLab Public Deploy Key"},
            {"name": "url", "value": "git@github.com:ABC/ABC.git"},
            {"name": "useAlternates", "value": "True"},
            {"name": "usernameStyle", "value": "USERID"},
        ],
    },
    "vcsRootInstances": {"href": "/app/rest/vcs-root-instances?locator=vcsRoot:(id:Abc_Abc)"},
}

builds = {
    "count": 10,
    "href": "/app/rest/buildTypes/id:Abc_Master/builds/?locator=start:0,count:10",
    "nextHref": "/app/rest/buildTypes/id:Abc_Master/builds/?locator=start:10,count:10",
    "build": [
        {
            "id": 1316053,
            "buildTypeId": "Abc_Master",
            "number": "570",
            "status": "SUCCESS",
            "state": "finished",
            "branchName": "master",
            "defaultBranch": True,
            "href": "/app/rest/builds/id:1316053",
            "webUrl": "https://teamcity.com/viewLog.html?buildId=1316053&buildTypeId=Abc_Master",
        },
        {
            "id": 1315981,
            "buildTypeId": "Abc_Master",
            "number": "569",
            "status": "SUCCESS",
            "state": "finished",
            "branchName": "master",
            "defaultBranch": True,
            "href": "/app/rest/builds/id:1315981",
            "webUrl": "https://teamcity.com/viewLog.html?buildId=1315981&buildTypeId=Abc_Master",
        },
        {
            "id": 1315290,
            "buildTypeId": "Abc_Master",
            "number": "568",
            "status": "SUCCESS",
            "state": "finished",
            "branchName": "master",
            "defaultBranch": True,
            "href": "/app/rest/builds/id:1315290",
            "webUrl": "https://teamcity.com/viewLog.html?buildId=1315290&buildTypeId=Abc_Master",
        },
        {
            "id": 1314277,
            "buildTypeId": "Abc_Master",
            "number": "567",
            "status": "SUCCESS",
            "state": "finished",
            "branchName": "master",
            "defaultBranch": True,
            "href": "/app/rest/builds/id:1314277",
            "webUrl": "https://teamcity.com/viewLog.html?buildId=1314277&buildTypeId=Abc_Master",
        },
        {
            "id": 1313577,
            "buildTypeId": "Abc_Master",
            "number": "566",
            "status": "SUCCESS",
            "state": "finished",
            "branchName": "master",
            "defaultBranch": True,
            "href": "/app/rest/builds/id:1313577",
            "webUrl": "https://teamcity.com/viewLog.html?buildId=1313577&buildTypeId=Abc_Master",
        },
        {
            "id": 1312998,
            "buildTypeId": "Abc_Master",
            "number": "565",
            "status": "SUCCESS",
            "state": "finished",
            "branchName": "master",
            "defaultBranch": True,
            "href": "/app/rest/builds/id:1312998",
            "webUrl": "https://teamcity.com/viewLog.html?buildId=1312998&buildTypeId=Abc_Master",
        },
        {
            "id": 1312365,
            "buildTypeId": "Abc_Master",
            "number": "564",
            "status": "SUCCESS",
            "state": "finished",
            "branchName": "master",
            "defaultBranch": True,
            "href": "/app/rest/builds/id:1312365",
            "webUrl": "https://teamcity.com/viewLog.html?buildId=1312365&buildTypeId=Abc_Master",
        },
        {
            "id": 1312249,
            "buildTypeId": "Abc_Master",
            "number": "563",
            "status": "SUCCESS",
            "state": "finished",
            "branchName": "master",
            "defaultBranch": True,
            "href": "/app/rest/builds/id:1312249",
            "webUrl": "https://teamcity.com/viewLog.html?buildId=1312249&buildTypeId=Abc_Master",
        },
        {
            "id": 1312166,
            "buildTypeId": "Abc_Master",
            "number": "562",
            "status": "SUCCESS",
            "state": "finished",
            "branchName": "master",
            "defaultBranch": True,
            "href": "/app/rest/builds/id:1312166",
            "webUrl": "https://teamcity.com/viewLog.html?buildId=1312166&buildTypeId=Abc_Master",
        },
        {
            "id": 1311678,
            "buildTypeId": "Abc_Master",
            "number": "561",
            "status": "SUCCESS",
            "state": "finished",
            "branchName": "master",
            "defaultBranch": True,
            "href": "/app/rest/builds/id:1311678",
            "webUrl": "https://teamcity.com/viewLog.html?buildId=1311678&buildTypeId=Abc_Master",
        },
    ],
}

vcs_root_instance = {
    "id": "597",
    "vcs-root-id": "some_vcs_root_id",
    "name": "ASDF",
    "vcsName": "svn",
    "modificationCheckInterval": 1800,
    "lastVersion": "97710",
    "href": "/app/rest/vcs-root-instances/id:597",
    "vcs-root": {"id": "some_vcs_root_id", "name": "ASDF", "href": "/app/rest/vcs-roots/id:some_vcs_root_id"},
    "status": {"current": {"status": "finished", "requestorType": "schedule", "timestamp": "20221022T023310+0300"}},
    "properties": {
        "count": 10,
        "property": [
            {"name": "enable-unsafe-ssl", "value": "True"},
            {"name": "externals-mode", "value": "externals-full"},
            {"name": "labelingMessage", "value": "Labeled automatically by TeamCity"},
            {"name": "labelingPatterns", "value": "trunk=>tags"},
            {"name": "secure:svn-password"},
            {"name": "svn-config-directory", "value": "/root/.subversion"},
            {"name": "svn-use-default-config-directory", "value": "True"},
            {"name": "url", "value": "http://svn.com/svn/ws/Teamcity/libs/ASDF"},
            {"name": "user", "value": "pavel"},
            {"name": "working-copy-format", "value": "1.8"},
        ],
    },
}

vcs_root_instances = {
    "count": 1,
    "href": "/app/rest/vcs-root-instances?locator=vcsRoot:(id:Abc_Abc)",
    "vcs-root-instance": [
        {"id": "2476", "vcs-root-id": "Abc_Abc", "name": "ABC", "href": "/app/rest/vcs-root-instances/id:2476"}
    ],
}


build_types = {
    "count": 5,
    "href": "/app/rest/buildTypes?locator=count:5",
    "nextHref": "/app/rest/buildTypes?locator=count:5,start:5",
    "buildType": [
        {
            "id": "Abc_Master",
            "name": "master",
            "description": "ABC master branch build",
            "projectName": "ABC",
            "projectId": "Abc",
            "href": "/app/rest/buildTypes/id:Abc_Master",
            "webUrl": "https://teamcity.com/viewType.html?buildTypeId=Abc_Master",
        },
        {
            "id": "Abc_Build",
            "name": "build",
            "description": "ABC non-master branch builds",
            "projectName": "ABC",
            "projectId": "Abc",
            "href": "/app/rest/buildTypes/id:Abc_Build",
            "webUrl": "https://teamcity.com/viewType.html?buildTypeId=Abc_Build",
        },
        {
            "id": "Abc_IssueSomeIssue",
            "name": "issue/Abc-someIsue",
            "description": "ABC non-master branch builds",
            "projectName": "ABC",
            "projectId": "Abc",
            "href": "/app/rest/buildTypes/id:Abc_IssueAbc903bfcp",
            "webUrl": "https://teamcity.com/viewType.html?buildTypeId=Abc_IssueSomeIssue",
        },
        {
            "id": "Abc_Experimental",
            "name": "Experimental",
            "description": "ABC non-master branch builds",
            "projectName": "ABC",
            "projectId": "Abc",
            "href": "/app/rest/buildTypes/id:Abc_Experimental",
            "webUrl": "https://teamcity.com/viewType.html?buildTypeId=Abc_Experimental",
        },
        {
            "id": "Abc_release",
            "name": "release",
            "description": "release ABC builds",
            "projectName": "ABC",
            "projectId": "Abc",
            "href": "/app/rest/buildTypes/id:Abc_release",
            "webUrl": "https://teamcity.com/viewType.html?buildTypeId=Abc_release",
        },
    ],
}


build_type = {
    "id": "Abc",
    "name": "ABC",
    "description": "ABC non-master branch builds",
    "projectName": "ABC",
    "projectId": "Abc",
    "href": "/app/rest/buildTypes/id:Abc",
    "webUrl": "https://teamcity.com/viewType.html?buildTypeId=Abc",
    "project": {
        "id": "Abc",
        "name": "ABC",
        "parentProjectId": "_Root",
        "description": "Simple as ABC",
        "href": "/app/rest/projects/id:Abc",
        "webUrl": "https://teamcity.com/project.html?projectId=Abc",
    },
    "builds": {"href": "/app/rest/buildTypes/id:Abc/builds/"},
    "investigations": {"href": "/app/rest/investigations?locator=buildType:(id:Abc)"},
    "compatibleAgents": {"href": "/app/rest/agents?locator=compatible:(buildType:(id:Abc))"},
}

investigation = {
    "id": "test:(id:-8676170902480411651),assignmentProject:(id:Abc_Tests)",
    "state": "TAKEN",
    "href": "/app/rest/investigations/test:(id:-8676170902480411651),assignmentProject:(id:Abc_Tests)",
    "assignee": {"username": "jobs", "name": "Steve Jobs", "id": 68, "href": "/app/rest/users/id:68"},
    "assignment": {
        "timestamp": "20210331T154612+0300",
        "text": "Some text here",
        "user": {"username": "carmack", "name": "John Carmack", "id": 85, "href": "/app/rest/users/id:85"},
    },
    "scope": {
        "project": {
            "id": "Abc_Tests",
            "name": "Tests",
            "parentProjectId": "Abc",
            "description": "ABC Tests",
            "href": "/app/rest/projects/id:Abc_Tests",
            "webUrl": "https://teamcity.com/project.html?projectId=Abc_Tests",
        }
    },
    "target": {
        "tests": {
            "count": 1,
            "test": [
                {
                    "id": "-8676170902480411651",
                    "name": "Some test name",
                    "href": "/app/rest/tests/id:-8676170902480411651",
                }
            ],
        }
    },
    "resolution": {"type": "manually"},
}

investigations = {
    "count": 5,
    "nextHref": "/app/rest/investigations?locator=count:5,start:5",
    "href": "/app/rest/investigations?locator=count:5",
    "investigation": [
        {
            "id": "buildType:(id:MMM_DevelopGit)",
            "state": "GIVEN_UP",
            "href": "/app/rest/investigations/buildType:(id:MMM_DevelopGit)",
            "assignee": {"username": "gates", "name": "Bill Gates", "id": 5, "href": "/app/rest/users/id:5"},
            "assignment": {
                "timestamp": "20221024T161045+0300",
                "user": {"username": "gates", "name": "Bill Gates", "id": 5, "href": "/app/rest/users/id:5"},
            },
            "scope": {
                "buildTypes": {
                    "count": 1,
                    "buildType": [
                        {
                            "id": "MMM_DevelopGit",
                            "name": "develop-git",
                            "description": "MMM GIT",
                            "projectName": "MMM",
                            "projectId": "MMM",
                            "href": "/app/rest/buildTypes/id:MMM_DevelopGit",
                            "webUrl": "https://teamcity.com/viewType.html?buildTypeId=MMM_DevelopGit",
                        }
                    ],
                }
            },
            "target": {"anyProblem": True},
            "resolution": {"type": "whenFixed"},
        },
        {
            "id": "buildType:(id:MMM_CentOS6x8664)",
            "state": "GIVEN_UP",
            "href": "/app/rest/investigations/buildType:(id:MMM_CentOS6x8664)",
            "assignee": {"username": "gates", "name": "Bill Gates", "id": 5, "href": "/app/rest/users/id:5"},
            "assignment": {
                "timestamp": "20200821T083429+0300",
                "user": {"username": "gates", "name": "Bill Gates", "id": 5, "href": "/app/rest/users/id:5"},
            },
            "scope": {
                "buildTypes": {
                    "count": 1,
                    "buildType": [
                        {
                            "id": "MMM_CentOS6x8664",
                            "name": "CentOS6_x86-64",
                            "description": "MMM branch 'R7'",
                            "projectName": "MMM / R7",
                            "projectId": "MMM_R7",
                            "href": "/app/rest/buildTypes/id:MMM_CentOS6x8664",
                            "webUrl": "https://teamcity.com/viewType.html?buildTypeId=MMM_CentOS6x8664",
                        }
                    ],
                }
            },
            "target": {"anyProblem": True},
            "resolution": {"type": "whenFixed"},
        },
        {
            "id": "buildType:(id:MMM_NNN_Master)",
            "state": "TAKEN",
            "href": "/app/rest/investigations/buildType:(id:MMM_NNN_Master)",
            "assignee": {"username": "gates", "name": "Bill Gates", "id": 5, "href": "/app/rest/users/id:5"},
            "assignment": {
                "timestamp": "20211029T194344+0300",
                "user": {"username": "gates", "name": "Bill Gates", "id": 5, "href": "/app/rest/users/id:5"},
            },
            "scope": {
                "buildTypes": {
                    "count": 1,
                    "buildType": [
                        {
                            "id": "MMM_NNN_Master",
                            "name": "master",
                            "description": "Build NNN for MMM",
                            "projectName": "MMM / NNN",
                            "projectId": "MMM_NNN",
                            "href": "/app/rest/buildTypes/id:MMM_NNN_Master",
                            "webUrl": "https://teamcity.com/viewType.html?buildTypeId=MMM_NNN_Master",
                        }
                    ],
                }
            },
            "target": {"anyProblem": True},
            "resolution": {"type": "whenFixed"},
        },
        {
            "id": "test:(id:-8676170902480411651),assignmentProject:(id:Abc_Tests)",
            "state": "TAKEN",
            "href": "/app/rest/investigations/test:(id:-8676170902480411651),assignmentProject:(id:Abc_Tests)",
            "assignee": {"username": "jobs", "name": "Steve Jobs", "id": 68, "href": "/app/rest/users/id:68"},
            "assignment": {
                "timestamp": "20210331T154612+0300",
                "text": "Some text here",
                "user": {"username": "carmack", "name": "John Carmack", "id": 85, "href": "/app/rest/users/id:85"},
            },
            "scope": {
                "project": {
                    "id": "Abc_Tests",
                    "name": "Tests",
                    "parentProjectId": "Abc",
                    "description": "ABC Tests",
                    "href": "/app/rest/projects/id:Abc_Tests",
                    "webUrl": "https://teamcity.com/project.html?projectId=Abc_Tests",
                }
            },
            "target": {
                "tests": {
                    "count": 1,
                    "test": [
                        {
                            "id": "-8676170902480411651",
                            "name": "Test Name",
                            "href": "/app/rest/tests/id:-8676170902480411651",
                        }
                    ],
                }
            },
            "resolution": {"type": "manually"},
        },
        {
            "id": "test:(id:-1850744997341218790),assignmentProject:(id:Abc_Tests)",
            "state": "TAKEN",
            "href": "/app/rest/investigations/test:(id:-1850744997341218790),assignmentProject:(id:Abc_Tests)",
            "assignee": {"username": "jobs", "name": "Steve Jobs", "id": 68, "href": "/app/rest/users/id:68"},
            "assignment": {
                "timestamp": "20210702T142212+0300",
                "text": "Some another text",
                "user": {"username": "jobs", "name": "Steve Jobs", "id": 68, "href": "/app/rest/users/id:68"},
            },
            "scope": {
                "project": {
                    "id": "Abc_Tests",
                    "name": "Tests",
                    "parentProjectId": "Abc",
                    "description": "ABC Tests",
                    "href": "/app/rest/projects/id:Abc_Tests",
                    "webUrl": "https://teamcity.com/project.html?projectId=Abc_Tests",
                }
            },
            "target": {
                "tests": {
                    "count": 1,
                    "test": [
                        {
                            "id": "-1850744997341218790",
                            "name": "Some test name",
                            "href": "/app/rest/tests/id:-1850744997341218790",
                        }
                    ],
                }
            },
            "resolution": {"type": "manually"},
        },
    ],
}

agents = {
    "count": 5,
    "nextHref": "/app/rest/agents?locator=count:5,start:5",
    "href": "/app/rest/agents?locator=count:5",
    "agent": [
        {
            "id": 1,
            "name": "first_agent",
            "typeId": 42,
            "href": "/app/rest/agents/id:1",
            "webUrl": "https://teamcity.com/agentDetails.html?id=5606&agentTypeId=42&realAgentName=first_agent",
        },
        {
            "id": 2,
            "name": "second_agent",
            "typeId": 43,
            "href": "/app/rest/agents/id:2",
            "webUrl": "https://teamcity.com/agentDetails.html?id=6089&agentTypeId=43&realAgentName=second_agent",
        },
        {
            "id": 3,
            "name": "third_agent",
            "typeId": 62,
            "href": "/app/rest/agents/id:3",
            "webUrl": "https://teamcity.com/agentDetails.html?id=9835&agentTypeId=62&realAgentName=third_agent",
        },
        {
            "id": 4,
            "name": "fourth_agent",
            "typeId": 67,
            "href": "/app/rest/agents/id:4",
            "webUrl": "https://teamcity.com/agentDetails.html?id=10798&agentTypeId=67&realAgentName=fourth_agent",
        },
        {
            "id": 5,
            "name": "fifth_agent",
            "typeId": 260,
            "href": "/app/rest/agents/id:5",
            "webUrl": "https://teamcity.com/agentDetails.html?id=52112&agentTypeId=260&realAgentName=fifth_agent",
        },
    ],
}

agent = {
    "id": 5606,
    "name": "first_agent",
    "typeId": 42,
    "connected": True,
    "enabled": True,
    "authorized": True,
    "uptodate": True,
    "ip": "127.0.0.1",
    "href": "/app/rest/agents/id:5606",
    "webUrl": "https://teamcity.com/agentDetails.html?id=5606&agentTypeId=42&realAgentName=first_agent",
    "enabledInfo": {
        "status": True,
        "comment": {
            "timestamp": "20211208T144642+0300",
            "text": "some text",
            "user": {"username": "stallman", "name": "Richard Stallman", "id": 158, "href": "/app/rest/users/id:158"},
        },
    },
    "authorizedInfo": {
        "status": True,
        "comment": {
            "timestamp": "20190719T190434+0300",
            "text": "Some other text",
            "user": {"username": "linus", "name": "Linus Torvalds", "id": 16, "href": "/app/rest/users/id:16"},
        },
    },
    "properties": {
        "count": 81,
        "property": [
            {"name": "docker.server.osType", "value": "linux"},
            {"name": "docker.server.version", "value": "18.03.1"},
            {"name": "docker.version", "value": "18.06.1"},
            {"name": "dockerCompose.version", "value": "1.23.2"},
        ],
    },
    "pool": {"id": 19, "name": "main-pool", "href": "/app/rest/agentPools/id:19"},
}
