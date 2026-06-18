Name:           dtk6systemsettings
Version:        6.0.0
Release:        1%{?dist}
Summary:        DTK6 System Settings Library
License:        LGPL-3.0-or-later
URL:            https://github.com/LingmoOS/dtk6systemsettings
Source0:        https://github.com/LingmoOS/dtk6systemsettings/archive/refs/tags/v%{version}/%{name}-%{version}.tar.gz

BuildRequires:  gcc-c++
BuildRequires:  cmake >= 3.13
BuildRequires:  extra-cmake-modules
BuildRequires:  pkgconfig(Qt6Core)
BuildRequires:  pkgconfig(Qt6Gui)
BuildRequires:  pkgconfig(Qt6Quick)
BuildRequires:  pkgconfig(dtk6core)
BuildRequires:  pkgconfig(dtk6gui)

%description
DTK (Deepin Tool Kit) system settings library providing
common settings widgets and utilities for Qt6 applications.

%prep
%autosetup -n %{name}-%{version}

%build
%cmake \
    -DCMAKE_BUILD_TYPE=Release \
    -DCMAKE_INSTALL_PREFIX=%{_prefix}
%cmake_build

%install
%cmake_install

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%doc README.md
%license LICENSE*
%{_libdir}/libdtk6systemsettings*.so*

%package devel
Summary: Development files for DTK6 System Settings
Requires: %{name}%{?_isa} = %{version}-%{release}

%description devel
Header files and development libraries for DTK6 System Settings.

%files devel
%{_includedir}/dtk6systemsettings*/
%{_libdir}/libdtk6systemsettings*.so
%{_libdir}/cmake/DtkSystemSettings/

%changelog
* Tue Jun 18 2025 LingmoOS Build System <dev@lingmo.os> - %{version}-1
- Initial RPM packaging for local source build
