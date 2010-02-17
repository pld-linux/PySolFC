Summary:	A collection of solitare card games
Name:		PySolFC
Version:	1.1
Release:	0.3
License:	GPL v2+
Group:		Applications/Games
URL:		http://pysolfc.sourceforge.net/
Source0:	http://downloads.sourceforge.net/pysolfc/%{name}-%{version}.tar.bz2
# Source0-md5:	56aca8101b3534aaf3564c40ed6824f1
Source1:	PySol.desktop
Patch0:		pysolfc-setup.py-noglade.patch
BuildRequires:	python-devel
BuildRequires:	python-modules
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.219
Requires:	python-PIL-tk
Requires:	python-modules
Requires:	python-tkinter
Requires:	tcl
Requires:	tix
Requires:	tk
Provides:	pysol = %{version}-%{release}
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
%setup -q
%patch0 -p0

%build
%{__python} setup.py build

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_desktopdir}
%{__python} setup.py install \
	--optimize=2 \
	--root=$RPM_BUILD_ROOT

cp -a %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}

# sanitize
mv $RPM_BUILD_ROOT%{_bindir}/pysol{.py,}

%py_postclean

%find_lang pysol

%clean
rm -rf $RPM_BUILD_ROOT

%files -f pysol.lang
%defattr(644,root,root,755)
%doc README PKG-INFO
%attr(755,root,root) %{_bindir}/pysol
%dir %{py_sitescriptdir}/pysollib
%{py_sitescriptdir}/pysollib/*.py[co]
%dir %{py_sitescriptdir}/pysollib/configobj
%{py_sitescriptdir}/pysollib/configobj/*.py[co]
%dir %{py_sitescriptdir}/pysollib/games
%{py_sitescriptdir}/pysollib/games/*.py[co]
%dir %{py_sitescriptdir}/pysollib/games/mahjongg
%{py_sitescriptdir}/pysollib/games/mahjongg/*.py[co]
%dir %{py_sitescriptdir}/pysollib/games/special
%{py_sitescriptdir}/pysollib/games/special/*.py[co]
%dir %{py_sitescriptdir}/pysollib/games/ultra
%{py_sitescriptdir}/pysollib/games/ultra/*.py[co]
%dir %{py_sitescriptdir}/pysollib/macosx
%{py_sitescriptdir}/pysollib/macosx/*.py[co]
%dir %{py_sitescriptdir}/pysollib/pysolgtk
%{py_sitescriptdir}/pysollib/pysolgtk/*.py[co]
%dir %{py_sitescriptdir}/pysollib/tile
%{py_sitescriptdir}/pysollib/tile/*.py[co]
%dir %{py_sitescriptdir}/pysollib/tk
%{py_sitescriptdir}/pysollib/tk/*.py[co]
%dir %{py_sitescriptdir}/pysollib/winsystems
%{py_sitescriptdir}/pysollib/winsystems/*.py[co]

%if "%{py_ver}" > "2.4"
%{py_sitescriptdir}/PySolFC-*.egg-info
%endif

%dir %{_datadir}/%{name}
%{_datadir}/%{name}/cardset-crystal-mahjongg
%{_datadir}/%{name}/cardset-dashavatara-ganjifa
%{_datadir}/%{name}/cardset-dondorf
%{_datadir}/%{name}/cardset-gnome-mahjongg-1
%{_datadir}/%{name}/cardset-hexadeck
%{_datadir}/%{name}/cardset-kintengu
%{_datadir}/%{name}/cardset-matrix
%{_datadir}/%{name}/cardset-mughal-ganjifa
%{_datadir}/%{name}/cardset-oxymoron
%{_datadir}/%{name}/cardset-standard
%{_datadir}/%{name}/cardset-tuxedo
%{_datadir}/%{name}/cardset-vienna-2k
%{_datadir}/%{name}/html
%{_datadir}/%{name}/images
%{_datadir}/%{name}/sound
%{_datadir}/%{name}/tcl
%{_datadir}/%{name}/themes
%{_datadir}/%{name}/tiles

%{_pixmapsdir}/*.xbm
%{_pixmapsdir}/*.xpm
%{_desktopdir}/*.desktop
