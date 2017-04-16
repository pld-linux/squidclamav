#
Summary:	A Clamav Antivirus scanner for Squid 3.x
Summary(pl.UTF-8):	Skaner antywirusowy clamav dla Squida 3.x
Name:		squidclamav
Version:	6.16
Release:	1
License:	GPL v3
Group:		Networking/Utilities
Source0:	http://downloads.sourceforge.net/squidclamav/%{name}-%{version}.tar.gz
# Source0-md5:	d5c2e588b4162ed873aa678a47a65f0b
Patch0:		%{name}-build.patch
URL:		http://squidclamav.darold.net/
BuildRequires:	c-icap-devel
Requires:	c-icap
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A Clamav Antivirus scanner for Squid 3.x.

%description -l pl.UTF-8
Skaner antywirusowy clamav dla Squida 3.x.

%prep
%setup -q
%patch0 -p1

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_sysconfdir}/c-icap
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog INSTALL README
%attr(640,root,squid) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/c-icap/squidclamav.conf
%{_sysconfdir}/c-icap/squidclamav.conf.default
%attr(755,root,root) %{_libdir}/c_icap/squidclamav.so
%attr(755,root,root) %{_libdir}/squidclamav
%{_datadir}/c_icap/templates/squidclamav
%{_mandir}/man1/squidclamav.1*
