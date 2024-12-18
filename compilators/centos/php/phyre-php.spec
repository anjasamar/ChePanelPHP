Name:           che-php
Version:        8.2
Release:        1%{?dist}
Summary:       Che PHP - Web server for ChePanel

License:       GPL
URL:    https://chepanel.com
Source0: http://de2.php.net/distributions/php-8.2.0.tar.gz

%description
Che PHP for executing che panel

%prep
# we have no source, so nothing here

%build
wget http://de2.php.net/distributions/php-8.2.0.tar.gz -O $RPM_SOURCE_DIR/php-8.2.0.tar.gz
tar -xzf $RPM_SOURCE_DIR/php-8.2.0.tar.gz -C $RPM_BUILD_DIR
cd php-8.2.0
./buildconf --force
./configure --prefix=/usr/local/che/php \
				--with-libdir=lib/$(arch)-linux-gnu \
				--enable-fpm --with-fpm-user=cheweb --with-fpm-group=cheweb \
				--with-openssl \
				--with-mysqli \
                --with-pdo-mysql=mysqlnd \
                --with-mysqli=mysqlnd \
                --with-pdo-sqlite \
                --with-pdo-pgsql \
				--with-gettext \
				--with-curl \
				--enable-intl \
				--with-zip \
				--with-zlib \
				--with-gmp \
				--with-sodium \
				--with-freetype \
				--with-pear \
			  	--enable-sockets \
				--enable-mbstring \
				--enable-pcntl \
				--enable-shmop \
				--with-libdir=lib/$(arch)-linux-gnu
make -j 4
make install

/usr/local/che/php/bin/php -v
%make_install

wget https://raw.githubusercontent.com/anjasamar/ChePanelPHP/main/compilators/debian/php/php-fpm.conf -O $RPM_BUILD_ROOT/usr/local/che/php/conf/php-fpm.conf

%files
/usr/local/che/php

%changelog
* Tue May 05 2024 Che PHP Packaging <che-nginx-packaging@chepanel.com> - 8.2
- Initial release of Che PHP 8.2
