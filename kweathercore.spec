%define major 25
%define libname %mklibname KF5WeatherCore
%define devname %mklibname KF5WeatherCore -d
%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 80 ] && echo -n un; echo -n stable)

Name: kweathercore
Version:	25.12.0
Release:	1
#Source0: http://download.kde.org/%{stable}/frameworks/%(echo %{version} |cut -d. -f1-2)/%{name}-%{version}.tar.xz
#Source0:	https://invent.kde.org/libraries/kweathercore/-/archive/master/kweathercore-master.tar.bz2
#Source0:	https://invent.kde.org/libraries/kweathercore/-/archive/v%{version}/kweathercore-v%{version}.tar.bz2
Source0:	https://download.kde.org/stable/release-service/%{version}/src/kweathercore-%{version}.tar.xz
Summary: KDE library for handling weather data
URL: https://invent.kde.org/libraries/kweathercore
License: GPL
Group: System/Libraries
BuildRequires: bison
BuildRequires: doxygen
BuildRequires: cmake(Qt6Test)
BuildRequires: cmake(ECM)
BuildRequires: cmake(Qt6Core)
BuildRequires: cmake(Qt6Network)
BuildRequires: cmake(Qt6Positioning)
BuildRequires: cmake(KF6I18n)
BuildRequires: cmake(KF6Holidays)
BuildSystem:	cmake
BuildOption:	-DKDE_INSTALL_USE_QT_SYS_PATHS:BOOL=ON

%description
KDE library for handling weather data

%package -n %{libname}
Summary: KDE library for handling weather data
Group: System/Libraries

%description -n %{libname}
KDE library for handling weather data

%package -n %{devname}
Summary: Development files for %{name}
Group: Development/C
Requires: %{libname} = %{EVRD}

%description -n %{devname}
Development files (Headers etc.) for %{name}.

%files -n %{libname} -f %{name}.lang
%{_libdir}/*.so.%{major}*
%{_libdir}/*.so.6
%{_qtdir}/qml/org/kde/weathercore

%files -n %{devname}
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/cmake/*
%{_qtdir}/mkspecs/modules/*.pri
