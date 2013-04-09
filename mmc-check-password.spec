Summary:	OpenLDAP password checker module for MMC
Name:		mmc-check-password
Version:	3.0.0
Release:	6
License:	GPL
Group:		System/Servers
URL:		http://mds.mandriva.org/
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
rm -rf %{buildroot}

install -d %{buildroot}%{_libdir}/openldap
install -d %{buildroot}%{_sysconfdir}/openldap

install -m0644 mmc-check-password.conf %{buildroot}%{_sysconfdir}/openldap/mmc-check-password.conf
install -m0755 mmc-check-password.so %{buildroot}%{_libdir}/openldap/mmc-check-password.so

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,0755)
%attr(0644,root,root) %config(noreplace) %{_sysconfdir}/openldap/mmc-check-password.conf
%attr(0755,root,root) %{_libdir}/openldap/mmc-check-password.so



%changelog
* Wed May 04 2011 Oden Eriksson <oeriksson@mandriva.com> 3.0.0-3mdv2011.0
+ Revision: 666472
- mass rebuild

* Fri Dec 03 2010 Oden Eriksson <oeriksson@mandriva.com> 3.0.0-2mdv2011.0
+ Revision: 606654
- rebuild

* Thu Apr 29 2010 Anne Nicolas <ennael@mandriva.org> 3.0.0-1mdv2010.1
+ Revision: 540942
- fix version

* Tue Apr 27 2010 Oden Eriksson <oeriksson@mandriva.com> 0-1mdv2010.1
+ Revision: 539598
- import mmc-check-password


* Tue Apr 27 2010 Oden Eriksson <oeriksson@mandriva.com> 0-1mdv2010.1
- initial Mandriva package
