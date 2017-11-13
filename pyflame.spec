Name:    pyflame
Version: 1.6.3
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
BuildRequires: python34-devel
BuildRequires: python34-pytest
%else
BuildRequires: python2-devel
BuildRequires: python2-pytest
BuildRequires: python3-devel
BuildRequires: python3-pytest
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
