# ProgrammableWeb_2022
Programmable Web Course 2022

Mikke's and Mikko's shared web project.

Aim is to produce API-based task-planner calendar.

The project will be Dockerized soon, for easy migration.
Database is generated automatically with Ansible...

Ansible playboook can be run with command:
<br>

```
ansible-playbook --ask-become-pass database_playbook.yml
```
<br>
This asks sudo password to install dependencies and runs install script for them
