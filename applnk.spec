Summary:	Applnk - base directories tree used for storing desktop/kdelnk menu entries
Summary(pl):	Applnk - bazowa struktura katalogów z opisami do plików desktop/kdelnk
Name:		applnk
Version:	1.6.2
Release:	1
License:	GPL
Group:		Base
# This file does not exist at this URL.
#Source0:	ftp://ftp.pld.org.pl/software/applnk/%{name}-%{version}.tar.bz2
Source0:	%{name}-%{version}.tar.bz2
BuildRequires:	autoconf
BuildRequires:	automake
Conflicts:	wmconfig < 0.9.10-5
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_vfinfodir	%{_datadir}/desktop-directories
%define		_xdgconfdir	/etc/xdg

%description
Base directories tree used for storing desktop/kdelnk menu entries.
Package also contains full description of this hierarchy (descriptions
with translations and menu order).

%description -l pl
Bazowa struktura katalogów u¿ywana do przechowywania plików
desktop/kdelnk opisu elementów menu ze spisem aplikacji. Pakiet
zawiera pe³ny opis hierarchii katalogów (w plikach .directory) wraz z
t³umaczeniami tych opisów, a tak¿e opis sposobu uszeregowania
grup/elementów katalogów.

%prep
%setup -q

%build
rm -f missing
%{__aclocal}
%{__autoconf}
%{__automake}
%configure

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	applnkdir=%{_applnkdir} \
	pixmapsdir=%{_pixmapsdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%dir %{_xdgconfdir}
%dir %{_xdgconfdir}/menus
# should be marked as %%config
%{_xdgconfdir}/menus/applications.menu
%{_applnkdir}
%{_vfinfodir}
%{_pixmapsdir}/*
