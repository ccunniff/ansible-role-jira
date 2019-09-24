import os
import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']
).get_hosts('all')


def test_jira_service(host):
    jira = host.service("jira")
    assert jira.is_running
    assert jira.is_enabled


def test_jira_started(host):
    res = host.ansible("uri",
                       "url=http://localhost:8080/status return_content=yes",
                       check=False)
    assert "FIRST_RUN" in res["content"]
    assert res["status"] == 200
