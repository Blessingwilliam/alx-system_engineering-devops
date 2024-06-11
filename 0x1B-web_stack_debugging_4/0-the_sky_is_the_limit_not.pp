# This Puppet manifest configures Nginx for optimal performance

# Ensure Nginx package is installed
package { 'nginx':
  ensure => installed,
}

# Main Nginx configuration file
file { '/etc/nginx/nginx.conf':
  ensure  => file,
  content => "
user www-data;
worker_processes auto;
pid /run/nginx.pid;

events {
  worker_connections 1024;
}

http {
  sendfile on;
  tcp_nopush on;
  tcp_nodelay on;
  keepalive_timeout 65;
  types_hash_max_size 2048;

  include /etc/nginx/mime.types;
  default_type application/octet-stream;

  access_log /var/log/nginx/access.log;
  error_log /var/log/nginx/error.log;

  gzip on;
  gzip_disable 'msie6';

  include /etc/nginx/conf.d/*.conf;
  include /etc/nginx/sites-enabled/*;
}
",
  require => Package['nginx'],
}

# Default site configuration
file { '/etc/nginx/sites-available/default':
  ensure  => file,
  content => "
server {
    listen 80 default_server;
    listen [::]:80 default_server ipv6only=on;

    root /usr/share/nginx/html;
    index index.html index.htm;

    server_name localhost;

    location / {
        try_files \$uri \$uri/ =404;
    }
}
",
  require => Package['nginx'],
}

# Enable the default site by creating a symlink
file { '/etc/nginx/sites-enabled/default':
  ensure => link,
  target => '/etc/nginx/sites-available/default',
  require => File['/etc/nginx/sites-available/default'],
}

# Ensure Nginx service is running and enabled
service { 'nginx':
  ensure     => running,
  enable     => true,
  subscribe  => File['/etc/nginx/nginx.conf'],
}

