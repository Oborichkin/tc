from .agent import AgentSummary, AgentPoolSummary, Agent, AgentPool, Comment, AgentLink
from .artifact import ArtifactLink
from .build import BuildSummary, BuildsLink, BuildTypeSummary, Build, BuildQueue, BuildType, Assignment, Investigation
from .project import ProjectSummary, Project
from .server import Server
from .template import Template
from .user import GroupSummary, UserSummary, Group, User
from .vcs import VcsRootSummary, VcsRootInstanceSummary, VcsRootInstancesLink, VcsRoot, VcsRootInstance, Revision

AgentPool.update_forward_refs(ProjectSummary=ProjectSummary)
Assignment.update_forward_refs(UserSummary=UserSummary)
BuildType.update_forward_refs(ProjectSummary=ProjectSummary, AgentLink=AgentLink)
Build.update_forward_refs(Revision=Revision, Agent=Agent, ArtifactLink=ArtifactLink)
Comment.update_forward_refs(UserSummary=UserSummary)
Investigation.update_forward_refs(UserSummary=UserSummary)
