#
Summary:	A Clamav Antivirus scanner for Squid 3.x
Summary(pl.UTF-8):	Skaner antywirusowy clamav dla Squida 3.x
Name:		squidclamav
Group:		Networking/Utilities
License:	GPL v3
Version:	6.2
Release:	0.1
Source0:	http://downloads.sourceforge.net/squidclamav/%{name}-%{version}.tar.gz
# Source0-md5:	4447ce47033f15b4ac7c08829917041a
Patch0:		%{name}-build.patch
Patch1:		%{name}-conf.patch
URL:		http://squidclamav.darold.net/
Requires:	c-icap
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A Clamav Antivirus scanner for Squid 3.x.

%description -l pl.UTF-8
Skaner antywirusowy clamav dla Squida 3.x.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
%{__aclocal}
%{__autoconf}
%configure
%{__automake}
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
%attr(755,root,root) %{_libdir}/c_icap/squidclamav.so
%attr(755,root,root) %{_libdir}/squidclamav
%{_mandir}/man1/squidclamav.1.gz
