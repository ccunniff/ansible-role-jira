Ansible Role: jira
=========

Installs Jira Software.

Requirements
------------

None

Role Variables
--------------

A list of variables and their default values
```
jira_version: 8.4.1
jira_user: root
jira_installation: /opt/atlassian/jira
jira_home: /var/atlassian/application-data/jira
jira_download_base_url: https://www.atlassian.com/software/jira/downloads/binary
```

Dependencies
------------

geerlingguy.java

Example Playbook
----------------

    - hosts: servers
      roles:
         - role: ansible-role-jira

License
-------

MIT / BSD
