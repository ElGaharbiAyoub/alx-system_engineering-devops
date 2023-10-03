#automate the task of creating a custom HTTP header response
$hostname = $::hostname
exec { 'update server':
  command  => 'apt-get update',
  user     => 'root',
  provider => shell,
}

package { 'nginx':
  ensure   => present,
  provider => 'apt'
}

service { 'nginx':
  ensure  => 'running',
  enable  => true,
  require => Package['nginx']
}

file_line { 'add HTTP header':
  ensure => 'present',
  path   => '/etc/nginx/sites-available/default',
  after  => 'server_name _;',
  line   => "\n\tadd_header X-Served-By \"${hostname}\";"
}

exec { 'restart service':
    command  => 'sudo service nginx restart',
    provider => shell,
}
