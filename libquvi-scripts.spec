Summary:	Embedded lua scripts for parsing media details
Name:		libquvi-scripts
Version:	0.9.20131130
Release:	7
Epoch:		1
Group:		Networking/Other
License:	LGPLv2+
Url:		https://quvi.sourceforge.net/
Source0:	http://downloads.sourceforge.net/quvi/%{name}-%{version}.tar.xz
BuildArch:	noarch

%description
libquvi-scripts contains the embedded lua scripts that libquvi uses for
parsing the media details. Some additional utility scripts are also
included.

%package devel
Summary:	The pkgconfig for %{name}
Group:		Development/Other
Requires:	%{name} = %{EVRD}

%description	devel
The pkgconfig for %{name}.

%prep
%setup -q

%build
%configure --libdir=%{_datadir}
%make

%install
%makeinstall_std

%files
%doc ChangeLog COPYING README
%{_datadir}/%{name}
%{_mandir}/man7/*

%files devel
%{_datadir}/pkgconfig/*.pc
