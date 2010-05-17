Summary:	Applnk - base directories tree used for storing desktop/kdelnk menu entries
Summary(pl.UTF-8):	Applnk - bazowa struktura katalogów z opisami do plików desktop/kdelnk
Name:		applnk
Version:	2.0.0
Release:	1
License:	GPL
Group:		Base
Source0:	ftp://ep09.pld-linux.org/software/applnk/%{name}-%{version}.tar.bz2
# Source0-md5:	28009c432a46358a2a314ea9176a46c7
Provides:	xdg-menus
Conflicts:	gnome-menus
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_xdgconfdir	/etc/xdg
%define		_xdgdatadir	%{_datadir}/desktop-directories

%description
Base directories tree used for storing desktop/kdelnk menu entries.
Package also contains full description of this hierarchy (descriptions
with translations and menu order).

%description -l pl.UTF-8
Bazowa struktura katalogów używana do przechowywania plików
desktop/kdelnk opisu elementów menu ze spisem aplikacji. Pakiet
zawiera pełny opis hierarchii katalogów (w plikach .directory) wraz z
tłumaczeniami tych opisów, a także opis sposobu uszeregowania
grup/elementów katalogów.

%prep
%setup -q

%build
%configure

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_xdgconfdir}/menus/applications-merged

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog NEWS
%dir %{_xdgconfdir}/menus
%dir %{_xdgconfdir}/menus/applications-merged
%{_xdgconfdir}/menus/*.menu
%{_xdgdatadir}
%{_pixmapsdir}/*
