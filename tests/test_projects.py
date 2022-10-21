from .api_mock.responses import project

def test_projects(client):
    projects = client.projects()
    assert projects
    assert len(projects)


def test_project(client):
    proj = client.projects("Abc")
    assert proj
    assert proj.id
    assert proj.parent_project_id
    assert proj.description
    assert proj.href
    assert proj.webUrl
    assert proj.parent_project
    assert len(proj.build_types)
    assert len(proj.projects)
