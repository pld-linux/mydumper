#
# Conditional build:
%bcond_with	doc		# build documentation
%bcond_without	tests		# build without tests

Summary:	MySQL Data Dumper
Name:		mydumper
Version:	0.9.3
Release:	0.1
License:	GPL v3
Group:		Applications/Databases
Source0:	https://github.com/maxbube/mydumper/archive/v%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	72e411c8f20fa7d7c36bb78625536b1d
URL:		https://github.com/maxbube/mydumper
BuildRequires:	cmake
BuildRequires:	glib2-devel
BuildRequires:	mysql-devel
BuildRequires:	openssl-devel
BuildRequires:	pcre-devel
BuildRequires:	zlib-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A high-performance multi-threaded backup toolset for MySQL and
Drizzle.

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
%doc README
%attr(755,root,root) %{_bindir}/mydumper
%attr(755,root,root) %{_bindir}/myloader
