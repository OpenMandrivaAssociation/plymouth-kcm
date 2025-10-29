%define plasmaver %(echo %{version} |cut -d. -f1-3)
%define stable %([ "$(echo %{version} |cut -d. -f2)" -ge 80 -o "$(echo %{version} |cut -d. -f3)" -ge 80 ] && echo -n un; echo -n stable)
#define git 20240222
%define gitbranch Plasma/6.0
%define gitbranchd %(echo %{gitbranch} |sed -e "s,/,-,g")

Name: plymouth-kcm
Version:	6.5.1
Release:	%{?git:0.%{git}.}1
%if 0%{?git:1}
Source0:	https://invent.kde.org/plasma/plymouth-kcm/-/archive/%{gitbranch}/plymouth-kcm-%{gitbranchd}.tar.bz2#/plymouth-kcm-%{git}.tar.bz2
%else
Source0: http://download.kde.org/%{stable}/plasma/%{plasmaver}/plymouth-kcm-%{version}.tar.xz
%endif
Summary: SystemSettings module for selecting bootup themes
URL: https://kde.org/
License: GPL
Group: Graphical desktop/KDE
Patch0: plymouth-kcm-dracut.patch
BuildRequires: cmake(ECM)
BuildRequires: cmake(KF6Archive)
BuildRequires: cmake(KF6Auth)
BuildRequires: cmake(KF6Config)
BuildRequires: cmake(KF6CoreAddons)
BuildRequires: cmake(KF6I18n)
BuildRequires: cmake(KF6KIO)
BuildRequires: cmake(KF6NewStuff)
BuildRequires: cmake(KF6Declarative)
BuildRequires: cmake(KF6WidgetsAddons)
BuildRequires: cmake(KF6KCMUtils)
BuildRequires: cmake(Qt6)
BuildRequires: cmake(Qt6Core)
BuildRequires: cmake(Qt6Concurrent)
BuildRequires: cmake(Qt6DBus)
BuildRequires: cmake(Qt6Gui)
BuildRequires: cmake(Qt6Qml)
BuildRequires: cmake(Qt6Test)
BuildRequires: pkgconfig(ply-boot-client)
BuildRequires: pkgconfig(ply-splash-core)
Requires: plymouth
Recommends: plymouth(system-theme)
Recommends: dracut
# Renamed after 6.0 2025-05-03
%rename plasma6-plymouth-kcm

BuildSystem:	cmake
BuildOption:	-DBUILD_QCH:BOOL=ON
BuildOption:	-DKDE_INSTALL_USE_QT_SYS_PATHS:BOOL=ON

%description
SystemSettings module for selecting bootup themes.

%files -f %{name}.lang
%{_bindir}/kplymouththemeinstaller
%{_libdir}/libexec/kf6/kauth/plymouthhelper
%{_datadir}/dbus-1/system.d/org.kde.kcontrol.kcmplymouth.conf
%{_datadir}/dbus-1/system-services/org.kde.kcontrol.kcmplymouth.service
%{_datadir}/knsrcfiles/plymouth.knsrc
%{_datadir}/polkit-1/actions/org.kde.kcontrol.kcmplymouth.policy
%{_qtdir}/plugins/plasma/kcms/systemsettings/kcm_plymouth.so
%{_datadir}/applications/kcm_plymouth.desktop
