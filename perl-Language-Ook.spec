%define upstream_name    Language-Ook
%define upstream_version 1.0.2

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 3

Summary:    An Ook! interpreter
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/Language/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires: perl(Test::More)

BuildArch: noarch
BuildRoot:  %{_tmppath}/%{name}-%{version}-%{release}

%description
A programming language should be writable and readable by orang-utans. So
Ook! is a programming language designed for orang-utans.

Ook! is bijective with BrainFuck, and thus, Turing-complete.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

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
