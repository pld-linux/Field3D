# TODO: (optional) MPI?
Summary:	Field3D - open source library for storing voxel data
Summary(pl.UTF-8):	Field3D - mająca otwarte źródła biblioteka do przechowywania danych vokseli
Name:		Field3D
Version:	1.7.3
Release:	2
License:	BSD
Group:		Libraries
#Source0Download: https://github.com/imageworks/Field3D/releases
Source0:	https://github.com/imageworks/Field3D/archive/v%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	536198b1b4840a5b35400ccf05d4431c
URL:		http://opensource.imageworks.com/?p=field3d
BuildRequires:	cmake >= 2.8
BuildRequires:	boost-devel >= 1.34.0
BuildRequires:	doxygen
BuildRequires:	hdf5-devel >= 1.8
BuildRequires:	ilmbase-devel >= 1.0.1
BuildRequires:	libstdc++-devel
BuildRequires:	rpmbuild(macros) >= 1.605
Requires:	hdf5 >= 1.8
Requires:	ilmbase >= 1.0.1
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Field3D is an open source library for storing voxel data. It provides
C++ classes that handle in-memory storage and a file format based on
HDF5 that allows the C++ objects to be written to and read from disk.

%description -l pl.UTF-8
Field3D to mająca otwarte źródła biblioteka do przechowywania danych
vokseli. Udostępnia klasy C++ obsługujące przechowywanie ich w pamięci
oraz format plików oparty na HDF5 pozwalający na zapis i odczyt
obiektów C++ z dysku.

%package devel
Summary:	Header files for Field3D library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki Field3D
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	boost-devel >= 1.34.0
Requires:	hdf5-devel >= 1.8
Requires:	ilmbase-devel >= 1.0.1
Requires:	libstdc++-devel

%description devel
Header files for Field3D library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki Field3D.

%package apidocs
Summary:	Field3D API documentation
Summary(pl.UTF-8):	Dokumentacja API biblioteki Field3D
Group:		Documentation
BuildArch:	noarch

%description apidocs
API and internal documentation for Field3D library.

%description apidocs -l pl.UTF-8
Dokumentacja API biblioteki Field3D.

%prep
%setup -q

%build
# main build system is scons, but there is cmake alternative, which is slightly more usable in rpm building
install -d build
cd build
export CXXFLAGS="%{rpmcxxflags} %{rpmcppflags} -std=c++14"
%cmake ..

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} -r $RPM_BUILD_ROOT%{_prefix}/docs

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc CHANGES COPYING README
%attr(755,root,root) %{_bindir}/f3dinfo
%attr(755,root,root) %{_libdir}/libField3D.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libField3D.so.1.7

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libField3D.so
%{_includedir}/Field3D

%files apidocs
%defattr(644,root,root,755)
%doc docs/html/*.{css,html,js,png}
