def test_vcs_root_instances(client):
    instances = client.vcs_root_instances()
    assert len(instances)


def test_vcs_root_instance(client):
    instance = client.vcs_root_instances("597")
    assert instance.id
    assert instance.vcs_root_id
    assert instance.name
    assert instance.vcs_name
    assert instance.modification_check_interval
    assert instance.last_version
    assert instance.href
    assert instance.vcs_root
    assert instance.status
    assert len(instance.properties)
