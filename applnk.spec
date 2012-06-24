Summary:	Applnk - base directories tree used for storing desktop/kdelnk menu entries
Summary(pl):	Applnk - bazowa struktura katalog�w z opisami do plik�w desktop/kdelnk
Name:		applnk
Version:	1.5.5
Release:	1
License:	GPL
Group:		Base
Source0:	ftp://ftp.pld.org.pl/software/applnk/%{name}-%{version}.tar.gz
Conflicts:	wmconfig < 0.9.10-5	
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6

%description
Base directories tree used for storing desktop/kdelnk menu entries.
Package also contains full description of this hierarchy (descriptions
with translations and menu order).

%description -l pl
Bazowa struktura katalog�w u�ywana do przechowywania plik�w
desktop/kdelnk opisu element�w menu ze spisem aplikacji. Pakiet
zawiera pe�ny opis hierarhii katalog�w (w plikach .directory) wraz z
t�umaczenaimi tych opis�w, a tak�e opis sposobu uszeregowania
grup/element�w katalog�w.

%prep
%setup -q

%build
%configure

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_applnkdir}
%{_pixmapsdir}/*
