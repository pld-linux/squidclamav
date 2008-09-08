# TODO:
# - get rid of internal copies of regex library
# /TODO
Summary:	A Clamav Antivirus Redirector for Squid
Summary(pl.UTF-8):	Skaner antywirusowy clamav dla Squida
Name:		squidclamav
Group:		Networking/Utilities
License:	GPL v2
Version:	3.5
Release:	2
Source0:	http://www.samse.fr/GPL/squidclamav/%{name}-%{version}.tar.gz
# Source0-md5:	955060d2cf87d5fb9ab05f6c8cf83f56
URL:		http://www.samse.fr/GPL/squidclamav/
BuildRequires:	clamav-devel >= 0.82
BuildRequires:	curl-devel >= 7.12.1
Requires:	squid
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_sysconfdir	/etc/squid

%description
A Clamav Antivirus Redirector for Squid.

%description -l pl.UTF-8
Skaner antywirusowy clamav dla Squida.

%prep
%setup -q

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_sysconfdir}}

install squidclamav $RPM_BUILD_ROOT%{_bindir}
install squidclamav.conf.dist $RPM_BUILD_ROOT%{_sysconfdir}/squidclamav.conf

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog INSTALL README
%attr(640,root,squid) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/squidclamav.conf
%attr(755,root,root) %{_bindir}/squidclamav
