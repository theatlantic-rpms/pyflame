
%if 0%{?rhel} && 0%{?rhel} < 7
%bcond_with python3
%bcond_with check
%global scl_autotools 1
%global with_devtoolset 1
%{?!python2_pkgversion:%global python2_pkgversion 27}
%else
%bcond_without python3
%bcond_without check
%global scl_autotools 0
%global with_devtoolset 0
%{?!python2_pkgversion:%global python2_pkgversion 2}
%endif

Name:    pyflame
Version: 1.6.7
Release: 2%{?dist}
URL:     https://github.com/uber/%{name}
Summary: Tool for profiling Python processes and generating flame graphs
License: ASL 2.0
Source0: https://github.com/uber/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz
Patch0:  0001-support-all-python2-pkgconfig-files.patch
Patch1:  0002-ensure-defined-ptrace-constants.patch

%if 0%{?scl_autotools}
BuildRequires: autotools-latest
%else
BuildRequires: autoconf automake libtool
%endif

%if 0%{?with_devtoolset}
BuildRequires: devtoolset-4-gcc-c++
%else
BuildRequires: gcc-c++
%endif

BuildRequires: python%{python2_pkgversion}-devel
%if %{with check}
BuildRequires: python%{python2_pkgversion}-pytest
%endif

%if %{with python3}
BuildRequires: python3-devel
%if %{with check}
BuildRequires: python3-pytest
%endif
%endif

%description
Pyflame is a Python profiler that can generate flame graphs from Python
programs. Pyflame is different from many other Python profilers because it can
profile uninstrumented Python programs using the ptrace system call. It can be
used as an alternative to, or in conjunction with, existing Python profilers.

%prep
%autosetup -p1 -n %{name}-%{version}

%build
%if 0%{?scl_autotools}
. /opt/rh/autotools-latest/enable
. /opt/rh/devtoolset-4/enable
mkdir -p m4
cp /usr/share/aclocal/pkg.m4 m4
%endif
./autogen.sh
export CXXFLAGS='%{optflags} -fpermissive'
%configure
%make_build

%install
. /opt/rh/devtoolset-4/enable
%make_install

%if %{with check}
%check
./runtests.sh rpm
%endif

%files
%{_bindir}/*
%{_mandir}/man1/pyflame.1*
%doc NEWS.org README.md
%license LICENSE

%changelog
* Mon Jul 30 2018 Frankie Dintino <fdintino@gmail.com> - 1.6.7-2
- Fix building on el6

* Fri Jul 13 2018 Frankie Dintino <fdintino@gmail.com> - 1.6.7-1
- Update to 1.6.7
- Build with both python2 and python3

* Wed May 02 2018 Evan Klitzke <evan@eklitzke.org> - 1.6.6-4
- Include NEWS.org file as a doc file

* Wed May 02 2018 Evan Klitzke <evan@eklitzke.org> - 1.6.6-3
- Fix regression where py2 test suite did not run on Fedora28

* Wed May 02 2018 Evan Klitzke <evan@eklitzke.org> - 1.6.6-2
- Add macros to toggle building python2/3 support

* Wed May 02 2018 Evan Klitzke <evan@eklitzke.org> - 1.6.6-1
- update for pyflame 1.6.6

* Mon Apr 23 2018 Evan Klitzke <evan@eklitzke.org> - 1.6.5-1
- Upgrade for Pyflame 1.6.5, fixes packaging errors on F28/Rawhide

* Mon Apr 23 2018 Evan Klitzke <evan@eklitzke.org> - 1.6.4-3
- remove unneeded patch file

* Thu Apr 19 2018 Evan Klitzke <evan@eklitzke.org> - 1.6.4-2
- fix error w/ executable name for f28/rawhide

* Thu Apr 19 2018 Evan Klitzke <evan@eklitzke.org> - 1.6.4-1
- new version

* Mon Nov 13 2017 Evan Klitzke <evan@eklitzke.org> - 1.6.2-4
- new version

* Mon Nov 13 2017 Evan Klitzke <evan@eklitzke.org> - 1.6.2-3
- rebuilt

* Mon Nov 13 2017 Evan Klitzke <evan@eklitzke.org> - 1.6.2-2
- Fix a bad conditional. Test.

* Mon Nov 13 2017 Evan Klitzke <evan@eklitzke.org> - 1.6.2-1
- Update for new EPEL7 tests.

* Mon Nov 13 2017 Evan Klitzke <evan@eklitzke.org> - 1.6.1-2
- Update for EPEL7.

* Mon Nov 13 2017 Evan Klitzke <evan@eklitzke.org> - 1.6.1-1
- Import new version whose tests should work.

* Mon Nov 13 2017 Evan Klitzke <evan@eklitzke.org> - 1.6.0-3
- Update the test command

* Mon Nov 13 2017 Evan Klitzke <evan@eklitzke.org> - 1.6.0-2
- rebuilt

* Wed Nov 08 2017 Evan Klitzke <evan@eklitzke.org> - 1.6.0-1
- rebuilt

* Wed Nov 02 2016 Evan Klitzke <evan@eklitzke.org> - 1.2.1-1
- Get upstream v1.2.1 changes
- Minor packaging/spec file cleanups

* Wed Nov 02 2016 Evan Klitzke <evan@eklitzke.org> - 1.2.0-1
- Get upstream v1.2.0 changes
- Pyflame now supports both Python2 *and* Python3

* Sat Oct 29 2016 Evan Klitzke <evan@eklitzke.org> - 1.1.1-1
- Get new v1.1.1 release from upstream
- Various packaging changes
- Pyflame now installs a man page

* Sun Oct 16 2016 Evan Klitzke <evan@eklitzke.org> - 1.1-1
- Initial build.
