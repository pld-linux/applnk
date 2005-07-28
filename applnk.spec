Summary:	Applnk - base directories tree used for storing desktop/kdelnk menu entries
Summary(pl):	Applnk - bazowa struktura katalogów z opisami do plików desktop/kdelnk
Name:		applnk
Version:	1.9.5
Release:	18
License:	GPL
Group:		Base
Source0:	ftp://ftp.pld-linux.org/software/applnk/%{name}-%{version}.tar.bz2
# Source0-md5:	e3d5d40cfd4ea6c891d4e337004e09f4
Source1:	%{name}-gnome-preferences.menu
Source2:	%{name}-gnome-settings.menu
Patch0:		%{name}-system.patch
Patch1:		%{name}-gnome.patch
Patch2:		%{name}-category.patch
Patch3:		%{name}-ca+es.patch
BuildRequires:	autoconf
BuildRequires:	automake
Obsoletes:	gnome-menus
Obsoletes:	gnome-menus-filter
Provides:	xdg-menus
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
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1

%build
rm -f missing
%{__aclocal}
%{__autoconf}
%{__automake}
%configure

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_xdgconfdir}/menus/applications-merged \
	$RPM_BUILD_ROOT%{_desktopdir}/docklets

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	pixmapsdir=%{_pixmapsdir}

install %{SOURCE1} $RPM_BUILD_ROOT%{_xdgconfdir}/menus/preferences.menu
install %{SOURCE2} $RPM_BUILD_ROOT%{_xdgconfdir}/menus/settings.menu

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog NEWS 
%dir %{_desktopdir}/docklets
%dir %{_xdgconfdir}/menus
%dir %{_xdgconfdir}/menus/applications-merged
%{_xdgconfdir}/menus/*.menu
%{_xdgdatadir}
%{_pixmapsdir}/*
