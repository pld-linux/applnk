Summary:	AppLnk - base directories tree used for storing desktop/kdelnk menu entries
Name:		applnk
Version:	1.0
Release:	1
License:	GPL
Group:		Base
Source0:	ftp://ftp.pld.org.pl/software/applnk/%{name}-%{version}.tar.gz
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Base directories tree used for storing desktop/kdelnk menu entries.
Package also contains full description of this hierarchy (descriptions
with translations and menu order).

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
