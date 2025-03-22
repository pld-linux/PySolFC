%define		cardsets_minimal_ver	2.2.0

Summary:	A collection of solitare card games
Name:		PySolFC
Version:	2.20.1
Release:	5
License:	GPL v2+
Group:		Applications/Games
URL:		http://pysolfc.sourceforge.net/
Source0:	http://downloads.sourceforge.net/pysolfc/%{name}-%{version}.tar.xz
# Source0-md5:	d913fdaeeb3d736701fd7684652c0a5f
Source1:	https://downloads.sourceforge.net/pysolfc/PySolFC-Cardsets--Minimal-%{cardsets_minimal_ver}.tar.xz
# Source1-md5:	74ce380505393a5538b25cccb2ea1682
Patch0:		pysolfc-setup.py-noglade.patch
BuildRequires:	python3-devel
BuildRequires:	python3-modules
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.710
Requires:	python3-modules
Requires:	python3-pillow-tk
Requires:	python3-tkinter
Requires:	tcl
Requires:	tix
Requires:	tk
Provides:	pysol = %{version}-%{release}
Provides:	pysol-sound-server = %{version}-%{release}
Obsoletes:	pysol < 5
Obsoletes:	pysol-sound-server < 5
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
PySolFC (PySol Fan Club) is a collection of more than 1000 solitaire
card games. It is a fork of PySol solitare. Its features include
modern look and feel (uses Tile widget set), multiple cardsets and
tableau backgrounds, sound, unlimited undo, player statistics, a hint
system, demo games, a solitaire wizard, support for user written
plug-ins, an integrated HTML help browser, and lots of documentation.

%prep
%setup -q -a1
%patch -P 0 -p0

%build
%py3_build

%install
rm -rf $RPM_BUILD_ROOT

%py3_install

cp -a PySolFC-Cardsets--Minimal-%{cardsets_minimal_ver}/cardset-* $RPM_BUILD_ROOT%{_datadir}/PySolFC

# Not used in installed code
%{__sed} -i '/pycotap/d' $RPM_BUILD_ROOT%{py3_sitescriptdir}/PySolFC-*.egg-info/requires.txt

%find_lang pysol

%clean
rm -rf $RPM_BUILD_ROOT

%files -f pysol.lang
%defattr(644,root,root,755)
%doc AUTHORS.md NEWS.asciidoc README.md
%attr(755,root,root) %{_bindir}/pysol.py
%{py3_sitescriptdir}/pysollib
%{py3_sitescriptdir}/PySolFC-*.egg-info

%dir %{_datadir}/%{name}
%{_datadir}/%{name}/cardset-*
%{_datadir}/%{name}/html
%{_datadir}/%{name}/images
%{_datadir}/%{name}/sound
%{_datadir}/%{name}/tcl
%{_datadir}/%{name}/themes
%{_datadir}/%{name}/tiles

%{_desktopdir}/*.desktop
%{_iconsdir}/hicolor/*x*/apps/pysol.png
