# This Puppet manifest configures system limits to allow the holberton user to open more files

# Ensure the required package is installed
package { 'limits.conf':
  ensure => installed,
}

# Increase the file limits for the holberton user
file_line { 'increase open file limit for holberton':
  path  => '/etc/security/limits.conf',
  line  => 'holberton  hard  nofile  65536',
  match => '^holberton.*hard.*nofile',
}

file_line { 'increase soft file limit for holberton':
  path  => '/etc/security/limits.conf',
  line  => 'holberton  soft  nofile  65536',
  match => '^holberton.*soft.*nofile',
}

# Ensure PAM module is configured to use limits.conf
file_line { 'pam_limits':
  path  => '/etc/pam.d/common-session',
  line  => 'session required pam_limits.so',
  match => '^session\s+required\s+pam_limits.so',
  ensure => present,
}

file_line { 'pam_limits_noninteractive':
  path  => '/etc/pam.d/common-session-noninteractive',
  line  => 'session required pam_limits.so',
  match => '^session\s+required\s+pam_limits.so',
  ensure => present,
}
