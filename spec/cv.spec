Summary:    cloudview configure tool 
Name:       cv
Version:    1.0
Release:    1
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
%setup -q
%build
%install
mkdir -p %{buildroot}/opt/cv/
cp -dpr * %{buildroot}/opt/cv/
read -n2 -p nihao

%files
%defattr(-,root,root,-)
/opt/cv/*
%post
rm /usr/local/bin/cv   
ln -s   /opt/cv/cv /usr/local/bin/cv 
