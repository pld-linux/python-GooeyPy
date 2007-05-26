#
# TODO :
# - Licence version
# - polish desc
# - precompile *.py
#
%define	module	GooeyPy
%define python_version py2.4

Summary:	Python/GooeyPy package
Summary(pl.UTF-8):	Pakiet Python/GooeyPy
Name:		python-%{module}
Version:	0.0.4.1
Release:	0.1
License:	LGPL or GPL v2.1
Vendor:		XML-SIG <xml-sig@python.org>
Group:		Libraries/Python
Source0:	http://cheeseshop.python.org/packages/source/G/GooeyPy/%{module}-%{version}.tar.gz
# Source0-md5:	1675af89a1b5be44097bde705c2e6c38
URL:		http://joey101.net/gooeypy/
#BuildRequires:	expat-devel >= 1:1.95.8
BuildRequires:	python >= 1:2.4
BuildRequires:	python-devel
BuildRequires:	python-setuptools
#Requires:	python-Cellulose
%pyrequires_eq	python-modules
Provides:	python-Cellulose
#Requires:	expat >= 1:1.95.8
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The PyXML package is a collection of libraries to process XML with
Python. 

#% description -l pl.UTF-8
#Pakiet PyXML jest zestawem bibliotek do obsługi XML-a z poziomu
#Pythona. 

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
install -d $RPM_BUILD_ROOT%{_examplesdir}/%{module}

python setup.py install \
	--root=$RPM_BUILD_ROOT \
	--optimize=2

# Cellulose
unzip  -d $RPM_BUILD_ROOT%{py_sitescriptdir} $RPM_BUILD_ROOT%{py_sitescriptdir}/Cellulose-0.1.2-py2.4.egg 
rm -f  $RPM_BUILD_ROOT%{py_sitescriptdir}/Cellulose-0.1.2-py2.4.egg

cp -a  examples/* $RPM_BUILD_ROOT%{_examplesdir}/%{module}
rm -f  $RPM_BUILD_ROOT%{py_sitescriptdir}/*.py[co]
rm -rf $RPM_BUILD_ROOT%{py_sitescriptdir}/EGG-INFO
cp -a  $RPM_BUILD_ROOT%{py_sitescriptdir}/%{module}-%{version}-%{python_version}.egg/gooeypy $RPM_BUILD_ROOT%{py_sitescriptdir}/gooeypy
rm -rf $RPM_BUILD_ROOT%{py_sitescriptdir}/%{module}-%{version}-%{python_version}.egg/examples
rm -rf $RPM_BUILD_ROOT%{py_sitescriptdir}/%{module}-%{version}-%{python_version}.egg/docs
rm -rf $RPM_BUILD_ROOT%{py_sitescriptdir}/%{module}-%{version}-%{python_version}.egg/gooeypy

%py_ocomp $RPM_BUILD_ROOT%{py_sitescriptdir}
%py_comp $RPM_BUILD_ROOT%{py_sitescriptdir}
%py_postclean
#install site.py $RPM_BUILD_ROOT%{py_sitescriptdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS CHANGELOG LICENSE.txt README
%{py_sitescriptdir}/gooeypy
%{py_sitescriptdir}/cellulose
#%{py_sitescriptdir}/*.py[co]
%{py_sitescriptdir}/*.egg
#%{py_sitescriptdir}/site.py

%files examples
%defattr(644,root,root,755)
%dir %{_examplesdir}/%{module}
%{_examplesdir}/%{module}
