0x1B-web_stack_debugging_4
For this project : 
I am testing how well our web server setup featuring Nginx is doing under pressure and it turns out it’s not doing well: we are getting a huge amount of failed requests.

For the benchmarking, we are using ApacheBench which is a quite popular tool in the industry. It allows you to simulate HTTP requests to a web server. In this case, 2000 requests to a  server with 100 requests at a time have been made . We can see that 943 requests failed, let’s fix our stack so that we get to 0.

# Web Stack Debugging with Nginx

## Overview
This project involves debugging and optimizing an Nginx web server setup to handle high traffic without failures.

## Setup
1. Ensure Nginx is installed on Ubuntu 14.04 LTS.
2. Edit `/etc/nginx/nginx.conf` with optimal settings.
3. Place the Puppet manifest `0-the_sky_is_the_limit_not.pp` in the project directory.

## Applying Puppet Manifest
Run the following command to apply the Puppet manifest:
```sh
puppet apply 0-the_sky_is_the_limit_not.pp

