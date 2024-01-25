# Change OS configuration so that it is possible to login and open a file without any error.

exec { 'change-os-configuration-for-holberton-user':
  path    => ['usr/local/sbin:usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin'],
  command => "sed -i 's/^holberton hard.*/holberton hard nofile 1024/g' /etc/security/limits.conf &&\
  	     sed -i 's/^holberton soft.*/holberton soft nofile 1024/g' /etc/security/limits.conf",
}
