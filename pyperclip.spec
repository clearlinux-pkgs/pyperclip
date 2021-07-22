#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pyperclip
Version  : 1.8.2
Release  : 24
URL      : https://files.pythonhosted.org/packages/a7/2c/4c64579f847bd5d539803c8b909e54ba087a79d01bb3aba433a95879a6c5/pyperclip-1.8.2.tar.gz
Source0  : https://files.pythonhosted.org/packages/a7/2c/4c64579f847bd5d539803c8b909e54ba087a79d01bb3aba433a95879a6c5/pyperclip-1.8.2.tar.gz
Summary  : A cross-platform clipboard module for Python. (Only handles plain text for now.)
Group    : Development/Tools
License  : BSD-3-Clause
Requires: pyperclip-license = %{version}-%{release}
Requires: pyperclip-python = %{version}-%{release}
Requires: pyperclip-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3

%description
Pyperclip is a cross-platform Python module for copy and paste clipboard functions. It works with Python 2 and 3.

%package license
Summary: license components for the pyperclip package.
Group: Default

%description license
license components for the pyperclip package.


%package python
Summary: python components for the pyperclip package.
Group: Default
Requires: pyperclip-python3 = %{version}-%{release}

%description python
python components for the pyperclip package.


%package python3
Summary: python3 components for the pyperclip package.
Group: Default
Requires: python3-core
Provides: pypi(pyperclip)

%description python3
python3 components for the pyperclip package.


%prep
%setup -q -n pyperclip-1.8.2
cd %{_builddir}/pyperclip-1.8.2

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1614015124
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$FFLAGS -fno-lto "
export FFLAGS="$FFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pyperclip
cp %{_builddir}/pyperclip-1.8.2/LICENSE.txt %{buildroot}/usr/share/package-licenses/pyperclip/0b5987b151853a0d55a7629eea600fe5cd311e8b
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pyperclip/0b5987b151853a0d55a7629eea600fe5cd311e8b

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
