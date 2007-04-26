%define name copyfs
%define version 1.0.1
%define release %mkrel 1

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
%{_mandir}/man1/copyfs-daemon.1.bz2
%{_mandir}/man1/copyfs-fversion.1.bz2
%{_mandir}/man1/copyfs-mount.1.bz2
%{_mandir}/man1/copyfs.1.bz2
%doc README TODO COPYING
