# set limits on user.
exec { 'hard limit':
  command => 'sed -i "s/holberton hard nofile 5/holberton hard nofile 1000/" /etc/security/limits.conf',
  path    => '/bin',
}
exec { 'soft limit':
  command => 'sed -i "s/holberton soft nofile 4/holberton hard nofile 1000/" /etc/security/limits.conf',
  path    => '/bin',
}
