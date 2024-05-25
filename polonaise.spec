# TODO: shared library?
Summary:	Polonaise - file system protocol
Summary(pl.UTF-8):	Polonaise - protokół systemów plików
Name:		polonaise
Version:	0.3.1
Release:	1
License:	Apache v2.0
Group:		Libraries
#Source0Download: https://github.com/polonaise/polonaise/tags
Source0:	https://github.com/polonaise/polonaise/archive/v%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	4de289df625cdc6669b42d953466e7e3
Patch0:		%{name}-thrift-c++11.patch
Patch1:		%{name}-cmake.patch
URL:		https://github.com/polonaise/polonaise
BuildRequires:	boost-devel
BuildRequires:	cmake >= 2.8
BuildRequires:	libfuse-devel
BuildRequires:	libstdc++-devel >= 6:4.7
BuildRequires:	rpmbuild(macros) >= 1.605
BuildRequires:	thrift >= 0.11
BuildRequires:	thrift-devel >= 0.11
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Polonaise is a file system protocol. It uses Thrift
(<https://thrift.apache.org/>) in its transport layer.

%description -l pl.UTF-8
Polonaise to protokół systemów plików. W warstwie transportowej
wykorzystuje bibliotekę Thrift (<https://thrift.apache.org/>).

%package devel
Summary:	Development files for Polonaise library
Summary(pl.UTF-8):	Pliki programistyczne biblioteki Polonaise
Group:		Development/Libraries
Requires:	libstdc++-devel >= 6:4.7
Requires:	thrift-devel >= 0.11

%description devel
Development files for Polonaise library.

Polonaise is a file system protocol. It uses Thrift
(<https://thrift.apache.org/>) in its transport layer.

%description devel -l pl.UTF-8
Pliki programistyczne biblioteki Polonaise.

Polonaise to protokół systemów plików. W warstwie transportowej
wykorzystuje bibliotekę Thrift (<https://thrift.apache.org/>).

%package fuse
Summary:	FUSE based Polonaise client
Summary(pl.UTF-8):	Oparty na FUSE klient Polonaise
Group:		Applications/System
Requires:	libfuse-tools

%description fuse
FUSE based Polonaise client.

%description fuse -l pl.UTF-8
Oparty na FUSE klient Polonaise.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
install -d build
cd build
%cmake ..

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files devel
%defattr(644,root,root,755)
%doc README.md
%{_libdir}/libpolonaise.a
%{_includedir}/polonaise
%{_libdir}/cmake/Polonaise

%files fuse
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/polonaise-fuse-client
