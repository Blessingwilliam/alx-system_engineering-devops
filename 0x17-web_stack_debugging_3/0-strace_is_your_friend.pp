# This Puppet manifest ensures the index.html file exists to prevent Apache from returning a 500 error.

file { '/var/www/html/index.html':
  ensure  => file,
  content => 'Hello, World!',
  require => Package['apache2'],
}

package { 'apache2':
  ensure => installed,
}

service { 'apache2':
  ensure  => running,
  enable  => true,
  require => File['/var/www/html/index.html'],
}
