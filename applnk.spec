Summary:	Applnk - base directories tree used for storing desktop/kdelnk menu entries
Summary(pl):	Applnk - bazowa struktura katalog�w z opisami do plik�w desktop/kdelnk
Name:		applnk
Version:	1.9.3
Release:	4
License:	GPL
Group:		Base
#Source0:	ftp://ftp.pld-linux.org/software/applnk/
Source0:	%{name}-%{version}.tar.bz2
# Source0-md5:	4ca390faf2287051251cca02d971bac1
Source1:	package_gnome_accessibility.png
Source2:	package_gnome_advanced.png
Source3:	package_gnome_system.png
Source4:	package_xfce4.png
Patch0:		%{name}-xmllint.patch
Patch1:		%{name}-gnome-settings.patch
Patch2:		%{name}-xfce4-settings.patch
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
Bazowa struktura katalog�w u�ywana do przechowywania plik�w
desktop/kdelnk opisu element�w menu ze spisem aplikacji. Pakiet
zawiera pe�ny opis hierarchii katalog�w (w plikach .directory) wraz z
t�umaczeniami tych opis�w, a tak�e opis sposobu uszeregowania
grup/element�w katalog�w.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1

%build
rm -f missing
%{__aclocal}
%{__autoconf}
%{__automake}
%configure

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_xdgconfdir}/menus/applications-merged

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	pixmapsdir=%{_pixmapsdir}

install %{SOURCE1} %{SOURCE2} %{SOURCE3} %{SOURCE4} $RPM_BUILD_ROOT%{_pixmapsdir}

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
