Summary:	Applnk - base directories tree used for storing desktop/kdelnk menu entries
Summary(pl):	Applnk - bazowa struktura katalogów z opisami do plików desktop/kdelnk
Name:		applnk
Version:	1.6.5
Release:	1
License:	GPL
Group:		Base
Source0:	http://www.kernel.pl/~adgor/pld/%{name}-%{version}.tar.bz2
# Source0-md5:	1ff5e59584875b42f6ee99169113d751
BuildRequires:	autoconf
BuildRequires:	automake
Conflicts:	wmconfig < 0.9.10-5
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
	applnkdir=%{_applnkdir} \
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
%{_applnkdir}
%{_xdgdatadir}
%{_pixmapsdir}/*
