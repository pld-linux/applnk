Summary:	Applnk - base directories tree used for storing desktop/kdelnk menu entries
Summary(pl):	Applnk - bazowa struktura katalogów z opisami do plików desktop/kdelnk
Name:		applnk
Version:	1.9.0
Release:	1
License:	GPL
Group:		Base
Source0:	ftp://ftp.pld-linux.org/software/applnk/%{name}-%{version}.tar.bz2
# Source0-md5:	15d1f7c032416e5c2a3915c40c240120
BuildRequires:	autoconf
BuildRequires:	automake
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_xdgconfdir	/etc/xdg
%define		_xdgdatadir	%{_datadir}/desktop-directories

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
	pixmapsdir=%{_pixmapsdir}

install -d $RPM_BUILD_ROOT%{_xdgconfdir}/menus/applications-merged

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%dir %{_xdgconfdir}/menus
%dir %{_xdgconfdir}/menus/applications-merged
# should be marked as %%config
%{_xdgconfdir}/menus/applications.menu
%{_xdgdatadir}
%{_pixmapsdir}/*
