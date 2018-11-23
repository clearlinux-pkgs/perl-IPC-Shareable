#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-IPC-Shareable
Version  : 0.61
Release  : 4
URL      : https://cpan.metacpan.org/authors/id/M/MS/MSOUTH/IPC-Shareable-0.61.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/M/MS/MSOUTH/IPC-Shareable-0.61.tar.gz
Source1  : http://http.debian.net/debian/pool/main/libi/libipc-shareable-perl/libipc-shareable-perl_0.61-2.debian.tar.xz
Summary  : No detailed summary available
Group    : Development/Tools
License  : GPL-2.0
Requires: perl-IPC-Shareable-license = %{version}-%{release}
BuildRequires : buildreq-cpan

%description
----------------------------------------------------------------------
This is free software; you can redistribute it and/or modify it
under the terms of the GNU General Public License as published by
the Free Software Foundation; either version 2 of the License , or
(at your option) any later version.
This software is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.
You should have received a copy of the GNU General Public License
along with this software. If not, write to the Free Software
Foundation, 675 Mass Ave, Cambridge, MA 02139, USA.
----------------------------------------------------------------------

%package dev
Summary: dev components for the perl-IPC-Shareable package.
Group: Development
Provides: perl-IPC-Shareable-devel = %{version}-%{release}

%description dev
dev components for the perl-IPC-Shareable package.


%package license
Summary: license components for the perl-IPC-Shareable package.
Group: Default

%description license
license components for the perl-IPC-Shareable package.


%prep
%setup -q -n IPC-Shareable-0.61
cd ..
%setup -q -T -D -n IPC-Shareable-0.61 -b 1
mkdir -p deblicense/
mv %{_topdir}/BUILD/debian/* %{_topdir}/BUILD/IPC-Shareable-0.61/deblicense/

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/perl-IPC-Shareable
cp COPYING %{buildroot}/usr/share/package-licenses/perl-IPC-Shareable/COPYING
cp deblicense/copyright %{buildroot}/usr/share/package-licenses/perl-IPC-Shareable/deblicense_copyright
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
/usr/lib/perl5/vendor_perl/5.28.0/IPC/Shareable.pm
/usr/lib/perl5/vendor_perl/5.28.0/IPC/Shareable/SharedMem.pm

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/IPC::Shareable.3
/usr/share/man/man3/IPC::Shareable::SharedMem.3

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/perl-IPC-Shareable/COPYING
/usr/share/package-licenses/perl-IPC-Shareable/deblicense_copyright
