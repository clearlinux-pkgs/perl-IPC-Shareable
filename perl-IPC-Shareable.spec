#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: cpan
#
Name     : perl-IPC-Shareable
Version  : 1.13
Release  : 34
URL      : https://cpan.metacpan.org/authors/id/S/ST/STEVEB/IPC-Shareable-1.13.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/S/ST/STEVEB/IPC-Shareable-1.13.tar.gz
Source1  : http://http.debian.net/debian/pool/main/libi/libipc-shareable-perl/libipc-shareable-perl_0.61-2.debian.tar.xz
Summary  : 'Use shared memory backed variables across processes'
Group    : Development/Tools
License  : Artistic-1.0-Perl GPL-2.0
Requires: perl-IPC-Shareable-license = %{version}-%{release}
Requires: perl-IPC-Shareable-perl = %{version}-%{release}
Requires: perl(Data::Dumper)
Requires: perl(IPC::Semaphore)
Requires: perl(IPC::SysV)
Requires: perl(JSON)
Requires: perl(Scalar::Util)
Requires: perl(Storable)
Requires: perl(String::CRC32)
BuildRequires : buildreq-cpan
BuildRequires : perl(JSON)
BuildRequires : perl(Mock::Sub)
BuildRequires : perl(Test::SharedFork)
BuildRequires : util-linux-bin
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
NAME
IPC::Shareable - Use shared memory backed variables across processes
SYNOPSIS

%package dev
Summary: dev components for the perl-IPC-Shareable package.
Group: Development
Provides: perl-IPC-Shareable-devel = %{version}-%{release}
Requires: perl-IPC-Shareable = %{version}-%{release}

%description dev
dev components for the perl-IPC-Shareable package.


%package license
Summary: license components for the perl-IPC-Shareable package.
Group: Default

%description license
license components for the perl-IPC-Shareable package.


%package perl
Summary: perl components for the perl-IPC-Shareable package.
Group: Default
Requires: perl-IPC-Shareable = %{version}-%{release}

%description perl
perl components for the perl-IPC-Shareable package.


%prep
%setup -q -n IPC-Shareable-1.13
cd %{_builddir}
tar xf %{_sourcedir}/libipc-shareable-perl_0.61-2.debian.tar.xz
cd %{_builddir}/IPC-Shareable-1.13
mkdir -p deblicense/
cp -r %{_builddir}/debian/* %{_builddir}/IPC-Shareable-1.13/deblicense/

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
if test -f Makefile.PL; then
%{__perl} -I. Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/perl-IPC-Shareable
cp %{_builddir}/IPC-Shareable-%{version}/COPYING %{buildroot}/usr/share/package-licenses/perl-IPC-Shareable/075d599585584bb0e4b526f5c40cb6b17e0da35a || :
cp %{_builddir}/debian/copyright %{buildroot}/usr/share/package-licenses/perl-IPC-Shareable/21192cbbbec96769f9ec218d2bcb586f37d1133c || :
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/IPC::Shareable.3
/usr/share/man/man3/IPC::Shareable::SharedMem.3

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/perl-IPC-Shareable/075d599585584bb0e4b526f5c40cb6b17e0da35a
/usr/share/package-licenses/perl-IPC-Shareable/21192cbbbec96769f9ec218d2bcb586f37d1133c

%files perl
%defattr(-,root,root,-)
/usr/lib/perl5/*
