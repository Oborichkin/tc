import uuid
from datetime import datetime


def test_server_info(client):
    info = client.server()
    assert info
    assert info.version and isinstance(info.version, str)
    assert info.build_number and isinstance(info.build_number, str)
    assert info.version_minor and isinstance(info.version_minor, int)
    assert info.version_major and isinstance(info.version_major, int)
    assert info.start_time and isinstance(info.start_time, datetime)
    assert info.current_time and isinstance(info.current_time, datetime)
    assert info.build_date and isinstance(info.build_date, datetime)
    assert info.internal_id and isinstance(info.internal_id, uuid.UUID)
