%define plasmaver %(echo %{version} |cut -d. -f1-3)
%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 80 ] && echo -n un; echo -n stable)

Name: plymouth-kcm
Version:	5.27.12
Release:	1
Source0: http://download.kde.org/%{stable}/plasma/%{plasmaver}/%{name}-%{version}.tar.xz
Summary: SystemSettings module for selecting bootup themes
URL: https://kde.org/
License: GPL
Group: Graphical desktop/KDE
Patch0: plymouth-kcm-dracut.patch
BuildRequires: cmake(ECM)
BuildRequires: cmake(KF5Archive)
BuildRequires: cmake(KF5Auth)
BuildRequires: cmake(KF5Config)
BuildRequires: cmake(KF5CoreAddons)
BuildRequires: cmake(KF5I18n)
BuildRequires: cmake(KF5KIO)
BuildRequires: cmake(KF5NewStuff)
BuildRequires: cmake(KF5Declarative)
BuildRequires: cmake(KF5WidgetsAddons)
BuildRequires: cmake(KF5KCMUtils)
BuildRequires: cmake(Qt5Core)
BuildRequires: cmake(Qt5Concurrent)
BuildRequires: cmake(Qt5DBus)
BuildRequires: cmake(Qt5Gui)
BuildRequires: cmake(Qt5Qml)
BuildRequires: cmake(Qt5Test)
BuildRequires: pkgconfig(ply-boot-client)
BuildRequires: pkgconfig(ply-splash-core)
BuildRequires: kcmutils
Requires: plymouth
Recommends: plymouth(system-theme)
Recommends: dracut

%description
SystemSettings module for selecting bootup themes.

%prep
%autosetup -p1
%cmake_kde5

%build
%ninja -C build

%install
%ninja_install -C build
%find_lang %{name} --all-name --with-html

%files -f %{name}.lang
%dir %{_datadir}/kpackage/kcms/kcm_plymouth
%{_bindir}/kplymouththemeinstaller
%{_libdir}/libexec/kauth/plymouthhelper
%{_datadir}/dbus-1/system.d/org.kde.kcontrol.kcmplymouth.conf
%{_datadir}/dbus-1/system-services/org.kde.kcontrol.kcmplymouth.service
%{_datadir}/kpackage/kcms/kcm_plymouth/*
%{_datadir}/knsrcfiles/plymouth.knsrc
%{_datadir}/polkit-1/actions/org.kde.kcontrol.kcmplymouth.policy
%{_libdir}/qt5/plugins/plasma/kcms/systemsettings/kcm_plymouth.so
%{_datadir}/applications/kcm_plymouth.desktop
