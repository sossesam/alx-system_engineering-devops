# install flask version 2.1.0

file {'/tmp/school':
    ensure  => present,
    owner   => 'www-data',
    group   => 'www-data',
    mode    => '0744',
    content => 'I love Puppet',
}