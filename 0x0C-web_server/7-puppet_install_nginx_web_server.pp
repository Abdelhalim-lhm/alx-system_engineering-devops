# setting up nginx using puppet

package { 'nginx':
  ensure => installed,
}

exec {'install':
  command  => 'sudo apt-get update ; sudo apt-get -y install nginx',
  provider => shell,
}

file { '/var/www/html/index.html':
  content => 'Hello World',
}

exec { 'redirect_me':
  command  => 'sudo sed -i "24i\        rewrite ^/redirect_me https://www.youtube.com/watch?v=QH2-TGUlwu4 permanent;" /etc/nginx/sites-available/default',
  provider => shell,
}

exec { 'run':
  command  => 'sudo service nginx restart',
  provider => shell,
}}
