def test_build_types(client):
    build_types = client.build_types()
    assert build_types
    assert len(build_types)


def test_build_type(client):
    build_type = client.build_types(id="test")
    assert build_type.id
    assert build_type.name
    assert build_type.description
    assert build_type.project_name
    assert build_type.project_id
    assert build_type.builds
    assert build_type.project
    assert build_type.builds
    assert build_type.investigations
    assert build_type.compatible_agents


def test_builds(client):
    assert client.builds()
