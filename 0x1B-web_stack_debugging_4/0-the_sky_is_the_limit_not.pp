# change limit for nginx server
exec { 'upper limit':
  command => 'sed -i s/15/1000/ /etc/default/nginx',
  path    => '/bin',
}
service { 'nginx':
    ensure    => running,
    subscribe => Exec['upper limit'],
}
