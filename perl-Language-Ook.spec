%define upstream_name    Language-Ook
Name:		perl-%{upstream_name}
Version:	1.0.2
Release:	8

Summary:	An Ook! interpreter
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		https://metacpan.org/dist/Language-Ook
Source0:	https://cpan.metacpan.org/authors/id/J/JQ/JQUELIN/Language-Ook-%{version}.tar.gz

BuildRequires:	make
BuildRequires:	perl-devel
BuildRequires:	perl(Test::More)

BuildArch:	noarch

%description
A programming language should be writable and readable by orang-utans. So
Ook! is a programming language designed for orang-utans.

Ook! is bijective with BrainFuck, and thus, Turing-complete.

%prep
%setup -q -n %{upstream_name}-%{version}

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
- rebuild using %1.0.2 Fri May 15 2009 Jérôme Quelin <jquelin@mandriva.org> 1.0.2-1mdv2010.0
+ Revision: 375948
- import perl-Language-Ook


* Sat Feb 28 2009 cpan2dist 1.0.2-1mdv
- initial mdv release, generated with cpan2dist

