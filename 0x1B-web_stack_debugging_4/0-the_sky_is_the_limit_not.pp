# update config files..

exec { '/etc/nginx/nginx.conf_0':
  path    => ['usr/local/sbin:usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin'],
  command => "sed -i 's/worker_processes.*/worker_processes 7;/g' /etc/nginx/nginx.conf",
}

exec { '/etc/nginx/nginx.conf_1':
  path    => ['usr/local/sbin:usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin'],
  command => "sed -i 's/worker_connections.*/worker_connections 4000;/g' /etc/nginx/nginx.conf",
}

-> exec { '/etc/nginx/nginx.conf_2':
  path    => ['usr/local/sbin:usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin'],
  command => "sed -i 's/keepalive_timeout.*/keepalive_timeout 15;/g' /etc/nginx/nginx.conf",
}

-> exec { '/etc/nginx/nginx.conf_3':
  path    => ['usr/local/sbin:usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin'],
  command => "sed -i 's/access_log.*/access_log off;/g' /etc/nginx/nginx.conf",
}

-> exec { '/etc/nginx/nginx.conf_4':
  path    => ['usr/local/sbin:usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin'],
  command => "sed -i '/error_log.*/a \\\topen_file_cache_errors on;' /etc/nginx/nginx.conf",
}

exec { '/etc/nginx/nginx.conf_5':
  path    => ['usr/local/sbin:usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin'],
  command => "sed -i '/error_log.*/a \\\topen_file_cache_min_uses 2;' /etc/nginx/nginx.conf",
}

-> exec { '/etc/nginx/nginx.conf_6':
  path    => ['usr/local/sbin:usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin'],
  command => "sed -i '/error_log.*/a \\\topen_file_cache_valid 30s;' /etc/nginx/nginx.conf",
}

-> exec { '/etc/nginx/nginx.conf_7':
  path    => ['usr/local/sbin:usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin'],
  command => "sed -i '/error_log.*/a \\\topen_file_cache max=200000 inactive=20s;' /etc/nginx/nginx.conf",
}

exec { 'nginx-restart':
  command => 'nginx restart',
  path    => '/etc/init.d/'
}
