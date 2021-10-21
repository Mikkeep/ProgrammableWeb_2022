#!/bin/bash

ansible-playbook --ask-become-pass database_playbook.yml
echo "Hello there!"
