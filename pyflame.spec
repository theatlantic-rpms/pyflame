Name:    pyflame
Version: 1.2.0
Release: 1%{?dist}
URL:     https://github.com/uber/pyflame
Summary: Tool for profiling Python processes and generating flame graphs
License: ASL 2.0
Source0: https://github.com/uber/%{name}/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildRequires: autoconf
BuildRequires: automake
BuildRequires: gcc-c++
BuildRequires: python-devel
BuildRequires: python3-devel
BuildRequires: python2-pytest
BuildRequires: python2-virtualenv

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
bash runtests.sh

%files
%{_bindir}/*
%doc README.md
/usr/share/man/man1/pyflame.1.gz
%license LICENSE

%changelog
* Sat Oct 29 2016 Evan Klitzke <evan@eklitzke.org> - 1.1.1-1
- Get new v1.1.1 release from upstream
- Various packaging changes
- Pyflame now installs a man page

* Sun Oct 16 2016 Evan Klitzke <evan@eklitzke.org> - 1.1-1
- Initial build.
