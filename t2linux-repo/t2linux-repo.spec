Name: t2linux-repo
Version: 5.0.1
Release: 2%{?dist}
Summary: DNF Repo for linux on t2 macs.
License: MIT

URL: https://github.com/t2linux/t2linux-fedora-kernel
Source0: t2linux-fedora.pub
Source1: t2linux-fedora-new.pub
Source2: t2linux-fedora.repo

%description
DNF repo files for linux on t2 macs.

%prep

%build

%install
install -d -m 755 %{_builddir}/etc/pki/rpm-gpg
install -m 644 t2linux-fedora.pub $RPM_BUILD_ROOT/etc/pki/rpm-gpg/
install -m 644 t2linux-fedora-new.pub $RPM_BUILD_ROOT/etc/pki/rpm-gpg/

install -d -m 755 %{_builddir}/etc/yum.repos.d
install -m 644 t2linux-fedora.repo $RPM_BUILD_ROOT/etc/yum.repos.d
	
%files
/etc/yum.repos.d/t2linux-fedora.repo
/etc/pki/rpm-gpg/t2linux-fedora.pub
/etc/pki/rpm-gpg/t2linux-fedora-new.pub

%changelog

* Mon Apr 24 2023 Sharpened Blade <sharpenedblade@proton.me>
- Made public GPG key ascii-armored