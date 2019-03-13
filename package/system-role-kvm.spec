#
# spec file for package system-role-kvm
#
# Copyright (c) 2017 SUSE LINUX GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


######################################################################
#
# IMPORTANT: Please do not change the control file or this spec file
#   in build service directly, use
#   https://github.com/yast/system-role-kvm repository
#
#   See https://github.com/yast/skelcd-control-server-role/blob/master/CONTRIBUTING.md
#   for more details.
#
######################################################################

%define role_name kvm
Name:           system-role-%{role_name}
# xmllint (for validation)
BuildRequires:  libxml2-tools
# RNG validation schema
BuildRequires:  yast2-installation-control >= 4.0.0

Url:            https://github.com/yast/system-role-kvm
AutoReqProv:    off
Version:        15.1.2
Release:        0
Summary:        Server KVM role definition
License:        MIT
Group:          Metapackages
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
Source:         %{name}-%{version}.tar.bz2
Provides:       installer_module_extension() = system-role-kvm
Provides:       extension_for_product() = SLES
Provides:       extension_for_product() = SLES_BCL
Provides:       extension_for_product() = SLES_SAP

%description
Meta package for Server KVM role definition.
It is not intended for installation.

%prep

%setup -n %{name}-%{version}

%check
#
# Verify syntax
#
make -C control check

%install

mkdir -p $RPM_BUILD_ROOT
#
# Add control file
#
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/system-roles
install -m 644 control/installation.xml $RPM_BUILD_ROOT/%{_datadir}/system-roles/%{role_name}.xml

# install LICENSE (required by build service check)
mkdir -p $RPM_BUILD_ROOT/%{_prefix}/share/doc/packages/%{name}
install -m 644 LICENSE $RPM_BUILD_ROOT/%{_prefix}/share/doc/packages/%{name}

%files
%defattr(644,root,root,755)
%{_datadir}/system-roles
%doc %dir %{_prefix}/share/doc/packages/%{name}
%doc %{_prefix}/share/doc/packages/%{name}/LICENSE

%changelog
