Summary:	Applnk - base directories tree used for storing desktop/kdelnk menu entries
Summary(pl.UTF-8):	Applnk - bazowa struktura katalogów z opisami do plików desktop/kdelnk
Name:		applnk
Version:	2.2.0
Release:	7
License:	GPL
Group:		Base
Source0:	ftp://ep09.pld-linux.org/software/applnk/%{name}-%{version}.tar.bz2
# Source0-md5:	0af5401b44bb2c91c771da76c627b4f5
Patch0:		xfce-4.10.patch
Provides:	xdg-menus
Requires:	filesystem >= 4.1-15
Conflicts:	xfdesktop < 4.10.0
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_xdgconfdir		/etc/xdg
%define		_xdgdirectorydir	%{_datadir}/desktop-directories

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
%patch -P0 -p1

%build
%configure

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post
%banner %{name} -e << EOF
Use of applnk menu is now controlled via XDG_MENU_PREFIX
environment variable.  If you want to disable it, then edit
/etc/env.d/XDG_MENU_PREFIX file.

If your menus just disappeared you need to re-login!

KDE users may have to logout, remove /{var,}/tmp/kdecache-*
directories before logging in and run kbuildsycoca4.
EOF

%files
%defattr(644,root,root,755)
%doc ChangeLog NEWS
%config(noreplace,missingok) %verify(not md5 mtime size) /etc/env.d/XDG_MENU_PREFIX
%{_xdgconfdir}/menus/applnk-applications.menu
%{_xdgdirectorydir}/accessories*.directory
%{_xdgdirectorydir}/applications.directory
%{_xdgdirectorydir}/development*.directory
%{_xdgdirectorydir}/education.directory
%{_xdgdirectorydir}/games*.directory
%{_xdgdirectorydir}/gnome.directory
%{_xdgdirectorydir}/gnome-settings.directory
%{_xdgdirectorydir}/graphics*.directory
%{_xdgdirectorydir}/kde.directory
%{_xdgdirectorydir}/misc.directory
%{_xdgdirectorydir}/multimedia*.directory
%{_xdgdirectorydir}/network*.directory
%{_xdgdirectorydir}/office*.directory
%{_xdgdirectorydir}/science.directory
%{_xdgdirectorydir}/settings*.directory
%{_xdgdirectorydir}/system*.directory
%{_xdgdirectorydir}/terminals.directory
%{_xdgdirectorydir}/x11.directory
%{_pixmapsdir}/package-*.png
