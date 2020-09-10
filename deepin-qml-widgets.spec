Name:           deepin-qml-widgets
Version:        2.3.6
Release:        1
Summary:        Deepin QML widgets
License:        GPLv3
URL:            https://github.com/linuxdeepin/deepin-qml-widgets
Source0:        %{url}/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires:  dtkwidget2-devel dtkcore2-devel deepin-gettext-tools
BuildRequires:  pkgconfig(gdk-pixbuf-2.0) pkgconfig(gtk+-2.0) pkgconfig(glib-2.0) pkgconfig(gio-2.0) pkgconfig(pango) pkgconfig(x11) pkgconfig(xcb) pkgconfig(xcb-damage) pkgconfig(Qt5X11Extras) pkgconfig(atk)
BuildRequires:  pkgconfig(xcomposite) pkgconfig(Qt5Core) pkgconfig(Qt5DBus) pkgconfig(Qt5Gui) pkgconfig(Qt5Network) pkgconfig(Qt5OpenGL) pkgconfig(Qt5Qml) pkgconfig(Qt5WebKit) pkgconfig(Qt5Widgets)
Requires:       qt5-qtgraphicaleffects%{?_isa} qt5-qtquickcontrols%{?_isa}

%description
Extends QML by providing widgets that is used by Deepin applications.

%prep
%setup -q

%build
deepin-generate-mo locale/locale_config.ini
%qmake_qt5
%make_build

%install
%make_install INSTALL_ROOT=%{buildroot}

install -d %{buildroot}%{_datadir}/locale/
cp -r locale/mo/* %{buildroot}%{_datadir}/locale/

%find_lang %{name}

%files -f %{name}.lang
%doc README.md
%license LICENSE
%{_bindir}/deepin-dialog
%{_qt5_qmldir}/Deepin/Locale/
%{_qt5_qmldir}/Deepin/StyleResources/
%{_qt5_qmldir}/Deepin/Widgets/
%{_datadir}/dbus-1/services/com.deepin.dialog.service

%changelog
* Thu Sep 10 2020 chenbo pan <panchenbo@uniontech.com> - 2.3.6-1
- Initial build
