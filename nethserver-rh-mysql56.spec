Summary: NethServer MySQL56 configuration and templates.
Name: nethserver-rh-mysql56
Version: 0.0.2
Release: 1%{?dist}
License: GPL
Group: Networking/Daemons
Source: %{name}-%{version}.tar.gz
BuildArch: noarch
Requires: rh-mysql56
Requires: nethserver-base
Requires: nethserver-lib >= 1.0.1
BuildRequires: nethserver-devtools
Conflicts: nethserver-release < 6.7
AutoReq: no


%description
This package adds necessary startup and configuration items for
mysql.

%prep
%setup

%build
mkdir -p root/etc/e-smith/sql/init
perl createlinks

%install
rm -rf $RPM_BUILD_ROOT
(cd root   ; find . -depth -print | cpio -dump $RPM_BUILD_ROOT)
/sbin/e-smith/genfilelist \
    --file  /usr/bin/mysql56 'attr(0755,root,root)' \
    --file  /usr/bin/mysqladmin56 'attr(0755,root,root)' \
    --file  /usr/bin/mysqlbinlog56 'attr(0755,root,root)' \
    --file  /usr/bin/mysqlcheck56 'attr(0755,root,root)' \
    --file  /usr/bin/mysql_config_editor56 'attr(0755,root,root)' \
    --file  /usr/bin/mysqld_multi56 'attr(0755,root,root)' \
    --file  /usr/bin/mysqldump56 'attr(0755,root,root)' \
    --file  /usr/bin/mysqlimport56 'attr(0755,root,root)' \
    --file  /usr/bin/mysql_plugin56 'attr(0755,root,root)' \
    --file  /usr/bin/mysqlshow56 'attr(0755,root,root)' \
    --file  /usr/bin/mysqlslap56 'attr(0755,root,root)' \
$RPM_BUILD_ROOT \
    > %{name}-%{version}-filelist
echo "%doc COPYING"          >> %{name}-%{version}-filelist

%clean 
rm -rf $RPM_BUILD_ROOT


%preun

%post
/sbin/chkconfig rh-mysql56-mysqld on
#/sbin/service rh-mysql56-mysqld start

%files -f %{name}-%{version}-filelist
%defattr(-,root,root)

%changelog
* Sun May 22 2016 stephane de Labrusse <stephdl@de-labrusse.fr> 0.0.2
- backup and restore function added

* Tue May 10 2016 stephane de Labrusse <stephdl@de-labrusse.fr> 0.0.1
- First release

