# config nginx
exec { 'update_server':
  command  => '/usr/bin/apt-get -y update',
  user     => 'root',
  path     => ['/usr/bin'],
  creates  => '/var/lib/apt/periodic/update-success-stamp',
  require  => Package['nginx'], # Ensure nginx is installed first
}

package { 'nginx':
  ensure   => present,
  provider => 'apt'
}

file_line { 'add_http_header':
  ensure  => present,
  path    => '/etc/nginx/sites-available/default',
  line    => 'add_header X-Served-By $::hostname;',
  after   => 'server_name _;',
  require => Exec['update_server'],
  notify  => Service['nginx'],
}

service { 'nginx':
  ensure  => 'running',
  enable  => true,
  require => File_line['add_http_header'],
}
