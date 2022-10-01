def test_projects(client):
    assert client.projects


def test_project(client):
    assert client.project("_Root")
