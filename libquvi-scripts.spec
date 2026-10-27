Summary:	Embedded lua scripts for parsing media details
Name:		libquvi-scripts
Version:	0.9.20131130
Release:	10
Group:		Networking/Other
License:	LGPLv2+
Url:		https://quvi.sourceforge.net/
Source0:	http://downloads.sourceforge.net/quvi/%{name}-%{version}.tar.xz
BuildArch:	noarch

# libquvi 0.9 still requires this name. Keep the obsolete versioned so
# this package does not obsolete its own provide.
Provides:	libquvi-scripts0.9 = %{version}-%{release}
Obsoletes:	libquvi-scripts0.9 < %{version}-%{release}

BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	slibtool
BuildRequires:	make
%description
libquvi-scripts contains the embedded lua scripts that libquvi uses for
parsing the media details. Some additional utility scripts are also
included.

%package devel
Summary:	The pkgconfig for %{name}
Group:		Development/Other
Requires:	%{name} = %{EVRD}
Provides:	libquvi-scripts0.9-devel = %{version}-%{release}
Obsoletes:	libquvi-scripts0.9-devel < %{version}-%{release}

%description	devel
The pkgconfig for %{name}.

%prep
%autosetup -p1

%build
%configure --libdir=%{_datadir}
%make_build

%install
%make_install
# For compatibility with libquvi 0.4.x
ln -s libquvi-scripts-0.9.pc %{buildroot}%{_datadir}/pkgconfig/libquvi-scripts.pc

%files
%doc ChangeLog COPYING README
%{_datadir}/%{name}
%{_mandir}/man7/*

%files devel
%{_datadir}/pkgconfig/*.pc
