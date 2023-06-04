Name:		websocketpp
Summary:	C++ WebSocket Protocol Library
Version:	0.8.2
Release:	1
Group:	 	Development/Other
License:	BSD
Url:    	https://www.zaphoyd.com/websocketpp
Source0:	https://github.com/zaphoyd/websocketpp/archive/%{version}/%{name}-%{version}.tar.gz
# (upsteram) https://github.com/zaphoyd/websocketpp/pull/888
Patch0:		websocketpp-0.8.2-cmake.patch

BuildRequires:	cmake
BuildRequires:	ninja
BuildRequires:	boost-devel

BuildArch: noarch

%description
WebSocket++ is a cross platform open source (BSD license) header only C++
library that implements RFC6455 (The WebSocket Protocol) and RFC7692
(Compression Extensions for WebSocket). It allows integrating WebSocket
client and server functionality into C++ programs. In its most common
configuration full featured network I/O is provided by the Asio Networking
Library.

#----------------------------------------------------------------------------

%package devel
Summary:	C++ WebSocket Protocol Library
Group:		Development/Other
Requires:	boost-devel

%description devel
WebSocket++ is a cross platform open source (BSD license) header only C++
library that implements RFC6455 (The WebSocket Protocol) and RFC7692
(Compression Extensions for WebSocket). It allows integrating WebSocket
client and server functionality into C++ programs. In its most common
configuration full featured network I/O is provided by the Asio Networking
Library.

%files devel
%license COPYING
%doc changelog.md readme.md roadmap.md
%{_includedir}/%{name}/
%{_libdir}/cmake/%{name}/
%{_libdir}/pkgconfig/%{name}.pc

#----------------------------------------------------------------------------

%prep
%autosetup -p1

%build
%cmake \
	-DINSTALL_CMAKE_DIR=%{_libdir}/cmake/%{name} \
	-GNinja
%ninja_build

%install
%ninja_install -C build

# create a pkgconfig file
install -dm 0755 %{buildroot}%{_libdir}/pkgconfig
cat << EOF > %{buildroot}%{_libdir}/pkgconfig/%{name}.pc
prefix=%{_prefix}
exec_prefix=%{_prefix}
libdir=%{_libdir}
includedir=%{_includedir}

Name: %{name}
Description: WebSocket API
Version: %{version}
URL: %{url}
Cflags: -I%{_includedir}/
EOF

