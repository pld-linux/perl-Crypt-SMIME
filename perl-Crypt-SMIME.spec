#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%define		pdir	Crypt
%define		pnam	SMIME
Summary:	Crypt::SMIME - S/MIME message signing, verification, encryption and decryption
Summary(pl.UTF-8):	Crypt::SMIME - podpisywanie, weryfikacja, szyfrowanie i odszyfrowywanie wiadomości S/MIME
Name:		perl-Crypt-SMIME
Version:	0.25
Release:	1
License:	LGPL v2+
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Crypt/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	7afe3f4dedd6f569efb1effcd432eacc
URL:		http://search.cpan.org/dist/Crypt-SMIME/
BuildRequires:	openssl-devel >= 0.9.9
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	perl(ExtUtils::CChecker)
BuildRequires:	perl(ExtUtils::PkgConfig)
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	openssl
%endif
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module provides a class for handling S/MIME messages. It can
sign, verify, encrypt and decrypt messages. It requires libcrypto
(http://www.openssl.org).

%description -l pl.UTF-8
Ten moduł dostarcza klasę do obsługi wiadomości S/MIME. Potrafi
podpisywać, weryfikować podpisy, szyfrować i odszyfrowywać takie
wiadomości. Wymaga biblioteki libcrypto z pakietu OpenSSL.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make} \
	CC="%{__cc}" \
	OPTIMIZE="%{rpmcflags}"

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__mv} $RPM_BUILD_ROOT%{_mandir}/man3/SMIME.3pm $RPM_BUILD_ROOT%{_mandir}/man3/Crypt::SMIME.3pm

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorarch}/Crypt/SMIME.pm
%dir %{perl_vendorarch}/auto/Crypt/SMIME
%attr(755,root,root) %{perl_vendorarch}/auto/Crypt/SMIME/SMIME.so
%{_mandir}/man3/Crypt::SMIME.3*
