# config nginx
# Install Nginx package
class { 'nginx':
  ensure => 'installed',
}

file_line { 'add_http_header':
  ensure  => present,
  path    => '/etc/nginx/sites-available/default',
  line    => 'add_header X-Served-By $::hostname;',
  after   => 'server_name _;',
  require => Class['nginx'],
  notify  => Service['nginx'],
}

service { 'nginx':
  ensure  => 'running',
  enable  => true,
  require => File_line['add_http_header'],
}
