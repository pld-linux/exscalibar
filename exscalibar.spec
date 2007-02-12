Summary:	exscalibar - audio signal refinement architecture
Summary(pl.UTF-8):   exscalibar - architektura do oczyszczania sygnału dźwiękowego
Name:		exscalibar
Version:	1.0.4
Release:	0.1
License:	GPL
Group:		Applications
Source0:	http://dl.sourceforge.net/exscalibar/%{name}-%{version}.tar.bz2
# Source0-md5:	3b0abeb7648d3732e5f4702c4a2be4ab
URL:		http://sourceforge.net/projects/exscalibar/
BuildRequires:	fftw3-single-devel
BuildRequires:	libmad-devel
BuildRequires:	libsndfile-devel
BuildRequires:	libvorbis-devel
BuildRequires:	qmake
BuildRequires:	qt-devel
BuildRequires:	rpmbuild(macros) >= 1.228
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Exscalibar is an EXtendable, SCalable Architecture for Live,
Interactive or Batch-orientated Audio-signal Refinement.

%description -l pl.UTF-8
Exscalibar (EXtendable, SCalable Architecture for Live, Interactive or
Batch-orientated Audio-signal Refinement) to rozszerzalna, skalowalna
architektura do oczyszczania sygnału dźwiękowego na żywo,
interaktywnie lub w trybie wsadowym.

%prep
%setup -q

%build
export QTDIR=/usr
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGELOG NOTES README RELEASE
