#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : CGNS
Version  : lib.3.4.0
Release  : 2
URL      : https://github.com/CGNS/CGNS/archive/v3.4.0/cgnslib-3.4.0.tar.gz
Source0  : https://github.com/CGNS/CGNS/archive/v3.4.0/cgnslib-3.4.0.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : Zlib zlib-acknowledgement
Requires: CGNS-bin = %{version}-%{release}
Requires: CGNS-lib = %{version}-%{release}
Requires: CGNS-license = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : glu-dev
BuildRequires : hdf5-dev
BuildRequires : libXmu-dev
BuildRequires : mesa-dev
BuildRequires : pkgconfig(x11)
BuildRequires : tk-dev
BuildRequires : util-linux
BuildRequires : zlib-dev

%description
The CFD General Notation System (CGNS) provides a standard for recording
and recovering computer data associated with the numerical solution of fluid
dynamics equations.

%package bin
Summary: bin components for the CGNS package.
Group: Binaries
Requires: CGNS-license = %{version}-%{release}

%description bin
bin components for the CGNS package.


%package dev
Summary: dev components for the CGNS package.
Group: Development
Requires: CGNS-lib = %{version}-%{release}
Requires: CGNS-bin = %{version}-%{release}
Provides: CGNS-devel = %{version}-%{release}
Requires: CGNS = %{version}-%{release}

%description dev
dev components for the CGNS package.


%package lib
Summary: lib components for the CGNS package.
Group: Libraries
Requires: CGNS-license = %{version}-%{release}

%description lib
lib components for the CGNS package.


%package license
Summary: license components for the CGNS package.
Group: Default

%description license
license components for the CGNS package.


%prep
%setup -q -n CGNS-3.4.0
cd %{_builddir}/CGNS-3.4.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1572652302
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
%cmake .. -DCMAKE_SKIP_RPATH:BOOL=ON \
-DCGNS_ENABLE_HDF5:BOOL=ON \
-DHDF5_NEED_MPI:BOOL=OFF \
-DCGNS_BUILD_CGNSTOOLS:BOOL=OFF \
-DCGNS_BUILD_TESTING:BOOL=ON \
-DCGNS_ENABLE_64BIT:BOOL=ON \
-DCGNS_ENABLE_FORTRAN:BOOL=ON \
-DCGNS_ENABLE_TESTS:BOOL=ON
make  %{?_smp_mflags}  VERBOSE=1
popd

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
cd clr-build; make test

%install
export SOURCE_DATE_EPOCH=1572652302
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/CGNS
cp %{_builddir}/CGNS-3.4.0/license.txt %{buildroot}/usr/share/package-licenses/CGNS/1be7ca6b47850de97d2dd5cab74d22620d017274
cp %{_builddir}/CGNS-3.4.0/src/LICENSE %{buildroot}/usr/share/package-licenses/CGNS/1be7ca6b47850de97d2dd5cab74d22620d017274
cp %{_builddir}/CGNS-3.4.0/src/cgnstools/LICENSE %{buildroot}/usr/share/package-licenses/CGNS/a429c0e28adfbea645b03002dacff5f40d46da4c
pushd clr-build
%make_install
popd
## install_append content
mkdir -p %{buildroot}/usr/lib64
mv %{buildroot}/usr/lib/* %{buildroot}/usr/lib64
## install_append end

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/adf2hdf
/usr/bin/cgnscheck
/usr/bin/cgnscompress
/usr/bin/cgnsconvert
/usr/bin/cgnsdiff
/usr/bin/cgnslist
/usr/bin/cgnsnames
/usr/bin/cgnsupdate
/usr/bin/hdf2adf

%files dev
%defattr(-,root,root,-)
/usr/include/cgns.mod
/usr/include/cgnsBuild.defs
/usr/include/cgns_io.h
/usr/include/cgnsconfig.h
/usr/include/cgnslib.h
/usr/include/cgnstypes.h
/usr/include/cgnstypes_f.h
/usr/include/cgnstypes_f03.h
/usr/include/cgnswin_f.h
/usr/lib64/libcgns.so

%files lib
%defattr(-,root,root,-)
/usr/lib64/libcgns.so.3.4

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/CGNS/1be7ca6b47850de97d2dd5cab74d22620d017274
/usr/share/package-licenses/CGNS/a429c0e28adfbea645b03002dacff5f40d46da4c
