%define upstream_name    Language-Ook
%define upstream_version 1.0.2

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	6

Summary:	An Ook! interpreter
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		https://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Language/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(Test::More)

BuildArch:	noarch

%description
A programming language should be writable and readable by orang-utans. So
Ook! is a programming language designed for orang-utans.

Ook! is bijective with BrainFuck, and thus, Turing-complete.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files
%doc LICENSE Changes README
%{_mandir}/man3/*
%{perl_vendorlib}/*


%changelog
* Mon Apr 18 2011 Funda Wang <fwang@mandriva.org> 1.0.2-3mdv2011.0
+ Revision: 655040
- rebuild for updated spec-helper

* Fri Feb 12 2010 Jérôme Quelin <jquelin@mandriva.org> 1.0.2-2mdv2011.0
+ Revision: 504932
- rebuild using %%perl_convert_version

* Fri May 15 2009 Jérôme Quelin <jquelin@mandriva.org> 1.0.2-1mdv2010.0
+ Revision: 375948
- import perl-Language-Ook


* Sat Feb 28 2009 cpan2dist 1.0.2-1mdv
- initial mdv release, generated with cpan2dist

