Summary:	AppLnk - base directories tree used for storing desktop/kdelnk menu entries
Summary(pl):	Applnk - bazowa srruktura katalog�w z opisami do plik�w desktop/kdelnk
Name:		applnk
Version:	1.2
Release:	1
License:	GPL
Group:		Base
Group(pl):	Podstawowe
Source0:	ftp://ftp.pld.org.pl/software/applnk/%{name}-%{version}.tar.bz2
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Base directories tree used for storing desktop/kdelnk menu entries.
Package also contains full description of this hierarchy (descriptions
with translations and menu order).

%description -l pl
Bazowa strukt�ra katalog�w u�ywana do przechowywania plik�w
desktop/kdelnk opisu element�w mwnu ze spisem aplikacji. Pakiet
zawiera pe�ny opis hierarhii katalog�w (w plikach .directory) w raz z
t�umaczenaimi tych opis�w, a tak�e opis sposobu uszeregowania
grup/element�w katalog�w.

%prep
%setup -q

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_applnkdir}

cp -ar .order * $RPM_BUILD_ROOT%{_applnkdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_applnkdir}
