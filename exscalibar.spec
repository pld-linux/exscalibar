Summary:	exscalibar
Name:		exscalibar
Version:	1.0.4
Release:	0.1
License:	GPL
Group:		Applications
Source0:	http://dl.sourceforge.net/exscalibar/%{name}-%{version}.tar.bz2
# Source0-md5:	3b0abeb7648d3732e5f4702c4a2be4ab
URL:		http://sourceforge.net/projects/exscalibar
BuildRequires:	fftw-devel
BuildRequires:	libmad-devel
BuildRequires:	libsndfile-devel
BuildRequires:	libvorbis-devel
BuildRequires:	qmake
BuildRequires:	qt-devel
BuildRequires:	rpmbuild(macros) >= 1.228
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description

%prep
%setup -q

%build

QTDIR=%{_datadir}/includes/qt/ %configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
# create directories if necessary
#install -d $RPM_BUILD_ROOT
#install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CREDITS CHANGELOG NOTES README RELEASE
