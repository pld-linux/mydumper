#
# Conditional build:
%bcond_with	doc		# build documentation
%bcond_without	tests		# build without tests

Summary:	MySQL Data Dumper
Name:		mydumper
Version:	0.9.5
Release:	1
License:	GPL v3
Group:		Applications/Databases
Source0:	https://github.com/maxbube/mydumper/archive/v%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	6599d60f0088dfe55582a3f71c87f284
URL:		https://github.com/maxbube/mydumper
BuildRequires:	cmake
BuildRequires:	glib2-devel
BuildRequires:	libstdc++-devel
BuildRequires:	mysql-devel
BuildRequires:	openssl-devel
BuildRequires:	pcre-devel
BuildRequires:	pkgconfig
BuildRequires:	zlib-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
mydumper/myloader:
- Parallelism (hence, speed) and performance (avoids expensive
  character set conversion routines, efficient code overall)
- Easier to manage output (separate files for tables, dump metadata,
  etc, easy to view/parse data)
- Consistency - maintains snapshot across all threads, provides
  accurate master and slave log positions, etc
- Manageability - supports PCRE for specifying database and tables
  inclusions and exclusions

%prep
%setup -q

%build
install -d build
cd build
%cmake \
	-DBUILD_DOCS=%{!?with_doc:OFF}%{?with_doc:ON} \
	..
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install -C build \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.md
%attr(755,root,root) %{_bindir}/mydumper
%attr(755,root,root) %{_bindir}/myloader
