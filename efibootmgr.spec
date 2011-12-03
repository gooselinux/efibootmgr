Summary: EFI Boot Manager
Name: efibootmgr
Version: 0.5.4
Release: 8%{?dist}
Group: System Environment/Base
License: GPLv2+
URL: http://linux.dell.com/%{name}/
BuildRequires: pciutils-devel, zlib-devel
BuildRoot: %(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXXXX)
# EFI/UEFI don't exist on PPC
ExclusiveArch: %{ix86} x86_64 ia64

# for RHEL / Fedora when efibootmgr was part of the elilo package
Conflicts: elilo <= 3.6-5
Obsoletes: elilo <= 3.6-5

Source0: http://linux.dell.com/%{name}/permalink/%{name}-%{version}.tar.gz
Patch0: efibootmgr-0.5.4-default-to-grub.patch

%description
%{name} displays and allows the user to edit the Intel Extensible
Firmware Interface (EFI) Boot Manager variables.  Additional
information about EFI can be found at
http://developer.intel.com/technology/efi/efi.htm and http://uefi.org/.

%prep
%setup -q
%patch0 -p1 -b .grub-default

%build
make %{?_smp_mflags} EXTRA_CFLAGS='%{optflags}'

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{_sbindir} %{buildroot}%{_mandir}/man8
install -p --mode 755 src/%{name}/%{name} %{buildroot}%{_sbindir}
gzip -9 -c src/man/man8/%{name}.8 > src/man/man8/%{name}.8.gz
touch -r src/man/man8/%{name}.8 src/man/man8/%{name}.8.gz
install -p --mode 644 src/man/man8/%{name}.8.gz %{buildroot}%{_mandir}/man8

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%{_sbindir}/%{name}
%{_mandir}/man8/%{name}.8.gz
%doc README INSTALL COPYING
    
%changelog
* Wed Apr 14 2010 Peter Jones <pjones@redhat.com> - 0.5.4-8
- Make \EFI\redhat\grub.efi the default bootloader
  Resolves: rhbz#579665

* Mon Nov 30 2009 Dennis Gregorovic <dgregor@redhat.com> - 0.5.4-7.1
- Rebuilt for RHEL 6

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.4-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Fri Mar 06 2009 Matt Domsch <Matt_Domsch@dell.com> - 0.5.4-6
- make ExclusiveArch %%{ix86} now that packages are being built as .i586

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Thu Apr 03 2008 Peter Jones <pjones@redhat.com> - 0.5.4-4
- Revert changes in -3, they weren't finalized and we don't need
  the feature at this time.

* Thu Mar 06 2008 Peter Jones <pjones@redhat.com> - 0.5.4-3
- Add support for setting driver related variables.

* Tue Feb  5 2008 Matt Domsch <Matt_Domsch@dell.com> 0.5.4-2
- rebuild with conflicts/obsoletes matching elilo

* Thu Jan  3 2008 Matt Domsch <Matt_Domsch@dell.com> 0.5.4-1
- split efibootmgr into its own RPM for Fedora/RHEL.

* Thu Aug 24 2004 Matt Domsch <Matt_Domsch@dell.com>
- new home linux.dell.com

* Fri May 18 2001 Matt Domsch <Matt_Domsch@dell.com>
- See doc/ChangeLog
