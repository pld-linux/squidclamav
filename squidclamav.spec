Summary:	A Clamav Antivirus Redirector for Squid
Summary(pl):	Skaner antywirusowy clamav dla squida
Name:		squidclamav
Group:		Networking/Utilities
License:	GPL v2
Version:	1.2
Release:	0.1
Source0:	http://www.samse.fr/GPL/squidclamav/%{name}-%{version}.tar.gz
# Source0-md5:	72d0dc8ff22dc2f85ddf8a0ba28ad01f
Patch0:		%{name}-paths.patch
URL:		http://www.samse.fr/GPL/squidclamav/
BuildRequires:	curl-devel >= 7.12.1
BuildRequires:	clamav-devel >= 0.82
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A Clamav Antivirus Redirector for Squid

%description -l pl
Skaner antywirusowy clamav dla squida

%prep
%setup -q
%patch0 -p1

%build
cd regex-0.12
%configure
%{__make}
cp regex.h regex.o ../
cd ..
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
%doc README
%attr(640,root,squid) %config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/squidclamav.conf
%attr(755,root,root) %{_bindir}/squidclamav
