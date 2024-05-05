# Modify client config file
include stdlib

file{'/etc/ssh/ssh_config':
  ensure => present,
}-> file_line {'Use private key in ~/.ssh/school':
  path => '/etc/ssh/ssh_config',
  line => 'IdentifyFile ~/.ssh/school',
}-> file_line {'Disable password Authentication':
  path => '/etc/ssh/ssh_config',
  line => 'PasswordAuthentication no',
}
