Name: myelin-website
Version: 1.0
Release: %{_release}
Summary: Myelin Website
License: MIT
Source0: root.tar.gz
BuildArch: noarch

%description
Myelin website

%prep
tar -xvf %{SOURCE0}

%install
install -d -m 0755 %{buildroot}/etc/systemd/system
install -d -m 0755 %{buildroot}/etc/letsencrypt/conf.d
install -d -m 0755 %{buildroot}/usr/bin
install -d -m 0755 %{buildroot}/etc/nginx/conf.d
install -d -m 0755 %{buildroot}/usr/share/nginx/html/myelin

cp -R %{_builddir}/config/* %{buildroot}/
cp -R public/* %{buildroot}/usr/share/nginx/html/myelin/

%post
if [ ! -f /etc/nginx/dhparams.pem ]; then
    openssl dhparam -out /etc/nginx/dhparams.pem 2048
fi

%files
%defattr(-,root,root)
/etc/systemd/system/*
/etc/letsencrypt/conf.d/*
/usr/bin/*
/etc/nginx/*
/etc/nginx/conf.d/*
%defattr(-,nginx,nginx)
/usr/share/nginx/html/myelin/*
