#
#
%define	module	GooeyPy

Summary:	Python/GooeyPy - a fast, flexible and cool looking GUI for pygame
Summary(pl.UTF-8):	Python/GooeyPy - szybkie, elastycznie i dobrze wyglądające GUI dla pygame
Name:		python-%{module}
Version:	0.0.4.1
Release:	1
License:	LGPL v2.1
Group:		Libraries/Python
Source0:	http://cheeseshop.python.org/packages/source/G/GooeyPy/%{module}-%{version}.tar.gz
# Source0-md5:	1675af89a1b5be44097bde705c2e6c38
URL:		http://joey101.net/gooeypy/
BuildRequires:	python >= 1:2.4
BuildRequires:	python-devel
BuildRequires:	python-setuptools
BuildRequires:	rpmbuild(macros) >= 1.219
Requires:	python-Cellulose
%pyrequires_eq	python-modules
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A fast, flexible, and cool looking GUI for pygame. 

%description -l pl.UTF-8
Szybkie, elastyczne i dobrze wyglądające GUI dla pygame.

%package examples
Summary:	Examples of Python/GooeyPy
Summary(pl.UTF-8):	Przykłady do Python/GooeyPy
Group:		Development/Languages/Python
%pyrequires_eq	python
Requires:	%{name} = %{version}-%{release}

%description examples
Examples of Python/GooeyPy.

%description examples -l pl.UTF-8
Przykłady do Python/GooeyPy.

%prep
%setup -q -n %{module}-%{version}

%build
python setup.py build

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{py_sitescriptdir}
install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

#python setup.py install \
#	--root=$RPM_BUILD_ROOT \
#	--optimize=2

cp -af  examples/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
cp -af  gooeypy $RPM_BUILD_ROOT%{py_sitescriptdir}/gooeypy

%py_ocomp $RPM_BUILD_ROOT%{py_sitescriptdir}
%py_comp $RPM_BUILD_ROOT%{py_sitescriptdir}
%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS CHANGELOG README
%doc docs
%{py_sitescriptdir}/gooeypy

%files examples
%defattr(644,root,root,755)
%{_examplesdir}/%{name}-%{version}
