# config nginx
exec { 'update server':
  command  => 'apt-get update',
  user     => 'root',
  provider => 'shell',
}

package { 'nginx':
  ensure   => present,
  provider => 'apt'
}

file_line { 'add HTTP header':
  ensure => 'present',
  path   => '/etc/nginx/sites-available/default',
  after  => 'server_name _;',
  line   => 'add_header X-Served-By $HOSTNAME;'
}

service { 'nginx':
  ensure  => 'running',
  enable  => true,
  require => Package['nginx']
}
