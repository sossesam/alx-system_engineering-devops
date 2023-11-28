#!/usr/bin/env bash
#using puppet to set up server.

file{'etc/ssh/ssh_config':
    ensure  => present,
    content => "
        Include /etc/ssh/ssh_config.d/*.conf

        Host *
        PasswordAuthentication no
        IdentityFile ~/.ssh/school
    ",

}