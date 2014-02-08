Summary:	OpenLDAP password checker module for MMC
Name:		mmc-check-password
Version:	3.0.0
Release:	7
License:	GPLv2
Group:		System/Servers
Url:		http://mds.mandriva.org/
Source0:	mmc-check-password.tar.gz
Patch0:		mmc-check-password-mdv_conf.diff
BuildRequires:	openldap-devel
BuildRequires:	wrap-devel

%description
OpenLDAP password checker module for MMC.

%prep

%setup -q -T -c -n %{name}-%{version} -a0
%patch0 -p0

%build
make CFLAGS="%{optflags} -fPIC"

%install
install -d %{buildroot}%{_libdir}/openldap
install -d %{buildroot}%{_sysconfdir}/openldap

install -m0644 mmc-check-password.conf %{buildroot}%{_sysconfdir}/openldap/mmc-check-password.conf
install -m0755 mmc-check-password.so %{buildroot}%{_libdir}/openldap/mmc-check-password.so

%files
%attr(0644,root,root) %config(noreplace) %{_sysconfdir}/openldap/mmc-check-password.conf
%attr(0755,root,root) %{_libdir}/openldap/mmc-check-password.so

