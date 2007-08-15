%define name     pfstmo
%define version  1.0
%define release %mkrel 1

Summary: Tone mapping operators
Name:           %{name}
Version:        %{version}
Release:        %{release}
License: GPL
Group: Graphics
Source: http://www.mpi-inf.mpg.de/resources/tmo/%{name}-%{version}.tar.bz2
Patch0: pfstmo-gcc4.patch.bz2
Patch1: pfstmo-configure.patch.bz2
URL: http://www.mpi-inf.mpg.de/resources/tmo/
BuildRoot: %{_tmppath}/%{name}-root
BuildRequires: libpfs-devel fftw3-devel autoconf

%description
pfstmo package contains the implementation of state-of-the-art tone mapping
operators. The motivation here is to provide an implementation of tone mapping
operators suitable for convenient processing of both static images and
animations.

%prep
%setup -q
%patch0 -p1
%patch1

%build
autoreconf
%configure
%make

%install
%makeinstall

%clean
rm -rf %{buildroot}

%files
%defattr(-, root, root)
%doc AUTHORS ChangeLog COPYING INSTALL TODO
%{_bindir}/*
%{_mandir}/man?/*
