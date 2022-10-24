def test_agents(client):
    agents = client.agents()
    assert agents
    assert len(agents)


def test_agent(client):
    agent = client.agents("test")
    assert agent.id
    assert agent.name
    assert agent.type_id
    assert agent.connected
    assert agent.enabled
    assert agent.authorized
    assert agent.uptodate
    assert agent.ip
    assert agent.enabled_info
    assert agent.authorized_info
    assert agent.properties
    assert agent.pool


def test_agent_pools(client):
    pools = client.agent_pools()
    assert pools
    assert len(pools)


def test_agent_pool(client):
    pool = client.agent_pools("test")
    assert pool.id
    assert pool.name
    assert pool.projects
    assert pool.agents
