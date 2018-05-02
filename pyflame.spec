# set to 1 if python2 support should be built
%define enable_py2 1

# set to 1 if python3 support should be built
%define enable_py3 1

# ensure that at least one of enable_py{2,3} is set
%if !%{enable_py2} && !%{enable_py3}
%{error: must set at least one of enable_py2/enable_py3}
%endif

Name:    pyflame
Version: 1.6.6
Release: 2%{?dist}
URL:     https://github.com/uber/%{name}
Summary: Tool for profiling Python processes and generating flame graphs
License: ASL 2.0
Source0: https://github.com/uber/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires: autoconf
BuildRequires: automake
BuildRequires: gcc-c++
BuildRequires: libtool

%if 0%{?el7}
BuildRequires: pytest
BuildRequires: python-devel
%if %{enable_py3}
BuildRequires: python34-devel
BuildRequires: python34-pytest
%endif
%else
%if %{enable_py3}
BuildRequires: python3-devel
BuildRequires: python3-pytest
%endif
%if %{enable_py2}
BuildRequires: python2-devel
%if 0%{?fedora} <= 27 || !%{enable_py3}
BuildRequires: python2-pytest
%endif
%endif
%endif

%description
Pyflame is a Python profiler that can generate flame graphs from Python
programs. Pyflame is different from many other Python profilers because it can
profile uninstrumented Python programs using the ptrace system call. It can be
used as an alternative to, or in conjunction with, existing Python profilers.

%prep
%autosetup -n %{name}-%{version}

%build
./autogen.sh
%configure
%make_build

%install
%make_install

%check
./runtests.sh rpm

%files
%{_bindir}/*
%{_mandir}/man1/pyflame.1*
%doc README.md
%license LICENSE

%changelog
* Wed May 02 2018 Evan Klitzke <evan@eklitzke.org> - 1.6.6-2
- Add macros to toggle building python2/3 support
- On Fedora 28+, do not build require python2-pytest when py3 is enabled

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
