# Ensure pip3 is present

package{'python3-pip':
ensure  => 'present',
}

# Install flask
exec{'install_flask':
command => '/usr/bin/pip3 install flask==2.1.0',
path    => '/usr/local/bin',
require => Package['python3-pip'],
}


