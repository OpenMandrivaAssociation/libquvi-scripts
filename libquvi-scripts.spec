Summary:	Embedded lua scripts for parsing media details
Name:		libquvi-scripts
Version:	0.9.20131130
Release:	8
Group:		Networking/Other
License:	LGPLv2+
Url:		https://quvi.sourceforge.net/
Source0:	http://downloads.sourceforge.net/quvi/%{name}-%{version}.tar.xz
BuildArch:	noarch

Obsolete:  	libquvi-scripts0.9

%description
libquvi-scripts contains the embedded lua scripts that libquvi uses for
parsing the media details. Some additional utility scripts are also
included.

%package devel
Summary:	The pkgconfig for %{name}
Group:		Development/Other
Requires:	%{name} = %{EVRD}
Obsolete:  libquvi-scripts0.9-devel

%description	devel
The pkgconfig for %{name}.

%prep
%autosetup -p1

%build
%configure --libdir=%{_datadir}
%make_build

%install
%make_install

%files
%doc ChangeLog COPYING README
%{_datadir}/%{name}
%{_mandir}/man7/*

%files devel
%{_datadir}/pkgconfig/*.pc
