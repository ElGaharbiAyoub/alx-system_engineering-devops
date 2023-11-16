# fixes a file
exec {'sets file limite for nginx':
  command => "sed -i 's/15/2000/g' /etc/default/nginx && sudo service nginx restart",
  path    => '/bin/:/sbin/:/usr/bin/:/usr/sbin/',
  onlyif  => 'test -f /etc/default/nginx'
}
