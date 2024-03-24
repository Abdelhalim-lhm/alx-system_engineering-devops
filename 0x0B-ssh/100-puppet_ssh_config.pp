# seting up client SSH configuration file so that we can connect to a server without typing a password
file { '/etc/ssh/ssh_config':
  ensure  => present,
  content => "
	host *
	PasswordAuthentication no
	PasswordAuthentication no
	",
}
