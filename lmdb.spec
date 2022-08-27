%global _empty_manifest_terminate_build 0
Name:		python-lmdb
Version:	1.3.0
Release:	1
Summary:	Universal Python binding for the LMDB 'Lightning' Database
License:	OLDAP-2.8
URL:		http://github.com/jnwatson/py-lmdb/
Source0:	https://files.pythonhosted.org/packages/ed/61/41f3c7cbd8a67202ef24fad3375ed936093a0547dc645581dd11c09581b7/lmdb-1.3.0.tar.gz
Requires:	python3-cffi

%description
Universal Python binding for the LMDB 'Lightning' Database

%package -n python3-lmdb
Summary:	Universal Python binding for the LMDB 'Lightning' Database
Provides:	python-lmdb
BuildRequires:	python3-devel
BuildRequires:	python3-setuptools
BuildRequires:	python3-cffi
BuildRequires:	gcc

%description -n python3-lmdb
Universal Python binding for the LMDB 'Lightning' Database

%package help
Summary:	Development documents and examples for lmdb
Provides:	python3-lmdb-doc

%description help
Universal Python binding for the LMDB 'Lightning' Database

%prep
%autosetup -n lmdb-1.3.0

%build
%py3_build

%install
%py3_install
install -d -m755 %{buildroot}/%{_pkgdocdir}
if [ -d doc ]; then cp -arf doc %{buildroot}/%{_pkgdocdir}; fi
if [ -d docs ]; then cp -arf docs %{buildroot}/%{_pkgdocdir}; fi
if [ -d example ]; then cp -arf example %{buildroot}/%{_pkgdocdir}; fi
if [ -d examples ]; then cp -arf examples %{buildroot}/%{_pkgdocdir}; fi
pushd %{buildroot}
if [ -d usr/lib ]; then
	find usr/lib -type f -printf "/%h/%f\n" >> filelist.lst
fi
if [ -d usr/lib64 ]; then
	find usr/lib64 -type f -printf "/%h/%f\n" >> filelist.lst
fi
if [ -d usr/bin ]; then
	find usr/bin -type f -printf "/%h/%f\n" >> filelist.lst
fi
if [ -d usr/sbin ]; then
	find usr/sbin -type f -printf "/%h/%f\n" >> filelist.lst
fi
touch doclist.lst
if [ -d usr/share/man ]; then
	find usr/share/man -type f -printf "/%h/%f.gz\n" >> doclist.lst
fi
popd
mv %{buildroot}/filelist.lst .
mv %{buildroot}/doclist.lst .

%files -n python3-lmdb -f filelist.lst
%dir %{python3_sitearch}/*

%files help -f doclist.lst
%{_docdir}/*

%changelog
* Fri Aug 26 2022 hkgy <kaguyahatu@outlook.com> - 1.3.0-1
- Update to 1.3.0

* Wed Aug 04 2021 chenyanpanHW <chenyanpan@huawei.com> - 1.2.1-2
- DESC: delete BuildRequires gdb

* Sun Jul 04 2021 Python_Bot <Python_Bot@openeuler.org> - 1.2.1-1
- Package Spec generated
