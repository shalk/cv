Summary:    cloudview configure tool 
Name:       cv
Version:    1.0
Release:    20150327
License:    GPL
Packager:   shalk
Source:     cv-1.0.tar.gz
Group:      Application  
URL:        http://www.sugon.com    
BuildRoot:      /tmp/%{name}-%{version}
Autoreq:    0

%description
This is  cloudview configure tool  rpm package for cloudview 1.8    
%prep
%setup -q cv
%build
%install
mkdir -p %{buildroot}/opt/cv/
cp -dpr * %{buildroot}/opt/cv/

%files
%defattr(-,root,root,-)
/opt/cv/*
%post
rm /usr/local/bin/cv  >& /dev/null 
ln -s   /opt/cv//bin/cv /usr/local/bin/cv 
mkdir -p /cloudview/cv/spool/import
mkdir -p /cloudview/cv/spool/iso
