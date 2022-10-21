def test_vcs_roots(client):
    roots = client.vsc_roots()
    assert len(roots)


def test_vcs_root(client):
    root = client.vsc_roots("Abc_Abc")
    assert root.name
    assert root.vcs_name
    assert root.modification_check_interval
    assert root.href
    assert root.project
    assert len(root.properties)
    assert root.vcs_root_instances