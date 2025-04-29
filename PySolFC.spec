%define		cardsets_minimal_ver	3.0.0

Summary:	A collection of solitare card games
Name:		PySolFC
Version:	3.2.0
Release:	1
License:	GPL v2+
Group:		Applications/Games
URL:		http://pysolfc.sourceforge.net/
Source0:	http://downloads.sourceforge.net/pysolfc/%{name}-%{version}.tar.xz
# Source0-md5:	db3be4114c10a7f066826091417ed35d
Source1:	https://downloads.sourceforge.net/pysolfc/PySolFC-Cardsets--Minimal-%{cardsets_minimal_ver}.tar.xz
# Source1-md5:	0bdd0de61bfe5a97ad9eb10516f7356a
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
Requires(post,postun):	desktop-file-utils
Requires(post,postun):	gtk-update-icon-cache
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

%post
%update_icon_cache hicolor
%update_desktop_database_post

%postun
%update_icon_cache hicolor
%update_desktop_database_postun

%prep
%setup -q -a1
%patch -P 0 -p0

%build
%py3_build
# fixing shebang - this probably can be done in a nicer way
%{__sed} -i '1s,python$,%{__python3},' build-3/scripts-3.13/pysol.py

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
