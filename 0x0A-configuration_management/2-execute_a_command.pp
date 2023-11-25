# command to kill a process

exec { 'Kill killmenow process':
  command => '/bin/pkill killmenow',
}