#!/usr/bin/env bash
#using puppet to set up server.

file {} '/etc/ssh/ssh_config':
    ensure  => present,
    content => '
        #SSH client configuration 

        Host *
        PasswordAuthentication no
        IdentityFile ~/.ssh/school
    ',
}