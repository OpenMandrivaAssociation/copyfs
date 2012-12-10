%define name copyfs
%define version 1.0.1
%define release %mkrel 5

Version:	%version
Release:	%release
Name:		%name
Summary:	A copy-on-write, versionned filesystem
License:	GPL
URL:		http://n0x.org/copyfs/
Group:		Archiving/Backup
BuildRoot:	%{_tmppath}/%{name}-root
BuildRequires:	%{mklibname fuse -d}, libattr-devel
Requires:	fuse, attr
Source:		http://n0x.org/copyfs/%{name}-%{version}.tar.bz2

%description
CopyFS is a copy-on-write, versionned file system. This file system is
useful for example when you have a directory containing important
files, for which you want to track changes, and be able to revert to an
older version. CopyFS lets you do that by transparently making backups
of each file that you modify. You are then able to see what version are
available for a file, and get an older version.

%prep
%setup -q

%build
%configure
%make

%install
%{__rm} -Rf %{buildroot}
%makeinstall

%clean
%{__rm} -Rf %{buildroot}

%files
%defattr(-,root,root)
%{_bindir}/copyfs-daemon
%{_bindir}/copyfs-fversion
%{_bindir}/copyfs-mount
%{_mandir}/man1/copyfs-daemon.*
%{_mandir}/man1/copyfs-fversion.*
%{_mandir}/man1/copyfs-mount.*
%{_mandir}/man1/copyfs.*
%doc README TODO COPYING


%changelog
* Thu Dec 09 2010 Oden Eriksson <oeriksson@mandriva.com> 1.0.1-5mdv2011.0
+ Revision: 617416
- the mass rebuild of 2010.0 packages

* Wed Sep 02 2009 Thierry Vignaud <tv@mandriva.org> 1.0.1-4mdv2010.0
+ Revision: 424984
- rebuild

* Wed Jul 23 2008 Thierry Vignaud <tv@mandriva.org> 1.0.1-3mdv2009.0
+ Revision: 243657
- rebuild

* Fri Dec 21 2007 Olivier Blin <oblin@mandriva.com> 1.0.1-1mdv2008.1
+ Revision: 136345
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request
    - fix man pages

* Thu Apr 26 2007 Nicolas Vigier <nvigier@mandriva.com> 1.0.1-1mdv2008.0
+ Revision: 18419
- Import copyfs



* Wed Apr 25 2007 Nicolas Vigier <nvigier@mandriva.com>
- first version
