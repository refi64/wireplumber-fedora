Name: wireplumber
Version: 0.3.0
Release: 1%{?dist}
Summary: Session / policy manager implementation for PipeWire

License: MIT
URL: https://gitlab.freedesktop.org/pipewire/wireplumber
Source0: https://gitlab.freedesktop.org/pipewire/wireplumber/-/archive/%{version}/%{name}-%{version}.tar.gz
Patch0: 0001-Allow-system-cpptoml.patch
Patch1: 0002-Fix-some-format-security-warnings.patch
Patch2: 0003-config-disable-audio-sink-streams-they-fail-on-lates.patch

BuildRequires: /usr/bin/g-ir-scanner
BuildRequires: cmake
BuildRequires: cmake(cpptoml)
BuildRequires: gcc
BuildRequires: gcc-c++
BuildRequires: meson
BuildRequires: pkgconfig(gio-2.0) >= 2.58
BuildRequires: pkgconfig(gio-unix-2.0) >= 2.58
BuildRequires: pkgconfig(gmodule-2.0) >= 2.58
BuildRequires: pkgconfig(gobject-2.0) >= 2.58
BuildRequires: pkgconfig(libpipewire-0.3)

Requires: %{name}-libs%{?_isa} = %{version}-%{release}

%description
WirePlumber is a modular session / policy manager for PipeWire and a GObject-based
high-level library that wraps PipeWire's API, providing convenience for writing the
daemon's modules as well as external tools for managing PipeWire.

%prep
%autosetup -p1

%build
export CFLAGS=
%meson -Ddoc=disabled
%meson_build

%install
%meson_install

# TODO: make this work
%dnl %check
%dnl %meson_test

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%package libs
Summary: Libraries for %{name}
License: MIT

%description libs
This package contains libwireplumber.

%package devel
Summary: Development fiels for %{name}
License: MIT
Requires: %{name}-libs%{?_isa} = %{version}-%{release}

%description devel
This package contains the pkg-config file and development headers for %{name}.

%files
%{_bindir}/wireplumber
%{_bindir}/wpctl
%config %{_sysconfdir}/wireplumber/*

%files libs
%{_libdir}/girepository-1.0/Wp-0.3.typelib
%{_libdir}/libwireplumber-0.3.so.*
%{_libdir}/wireplumber-0.3/libwireplumber-module-*.so

%files devel
%{_datadir}/gir-1.0/Wp-0.3.gir
%{_includedir}/wireplumber-0.3/wp/*.h
%{_libdir}/libwireplumber-0.3.so
%{_libdir}/pkgconfig/wireplumber-0.3.pc
