# Fixes wordpress config file typo
exec { 'replace':
  command => "sed -i 's/phpp/php/' /var/www/html/wp-settings.php",
  path    => '/bin',
}
