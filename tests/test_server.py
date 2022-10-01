def test_server_info(client):
    info = client.server
    assert info
    assert info.version
    assert info.build_number
    assert info.version_minor
    assert info.version_major
    assert info.start_time
    assert info.current_time
    assert info.build_date
    assert info.internal_id
