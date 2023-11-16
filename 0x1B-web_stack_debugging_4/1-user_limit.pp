# fixes a file
exec {'sets file limite for nginx':
  command => "sudo sed -i 's/nofile 4/nofile 6000/g; s/nofile 5/nofile 6000/g' /etc/security/limits.conf",
  path    => '/bin/:/sbin/:/usr/bin/:/usr/sbin/',
  onlyif  => 'test -f /etc/security/limits.conf'
}
