
%define realname   Language-Ook
%define version    1.0.2
%define release    %mkrel 1

Name:       perl-%{realname}
Version:    %{version}
Release:    %{release}
License:    GPL or Artistic
Group:      Development/Perl
Summary:    An Ook! interpreter
Source:     http://www.cpan.org/modules/by-module/Language/%{realname}-%{version}.tar.gz
Url:        http://search.cpan.org/dist/%{realname}
BuildRoot:  %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires: perl-devel
BuildRequires: perl(Test::More)

BuildArch: noarch

%description
A programming language should be writable and readable by orang-utans. So
Ook! is a programming language designed for orang-utans.

Ook! is bijective with BrainFuck, and thus, Turing-complete.



%prep
%setup -q -n %{realname}-%{version} 

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
rm -rf %buildroot
%makeinstall_std

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%doc LICENSE Changes README
%{_mandir}/man3/*
%perl_vendorlib/*


