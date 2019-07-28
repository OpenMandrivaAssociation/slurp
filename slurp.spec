Name:           slurp
Version:        1.2.0
Release:        1.2
Summary:        Wayland region selector
License:        MIT
URL:            https://github.com/emersion/slurp
Source0:        https://github.com/emersion/slurp/archive/v%{version}.tar.gz
BuildRequires:  meson >= 0.48.0
BuildRequires:  scdoc
BuildRequires:  pkgconfig(cairo)
BuildRequires:  pkgconfig(wayland-client)
BuildRequires:  pkgconfig(wayland-protocols) >= 1.14

%description
Tool to select a region in a Wayland compositor.
Meant to be used with a tool called grim.

%prep
%autosetup -p1

%build
export CFLAGS="%{optflags} -I/usr/include/wayland"
%meson
%meson_build

%install
%meson_install

%files
%{_bindir}/slurp
%{_mandir}/man1/slurp.1*
