#Kills a process

exec{'kill_killmenow':
command => 'pkill -f killmenow',
path    => '/usr/bin',
onlyif  => 'pgrep -f killmenow'
}
