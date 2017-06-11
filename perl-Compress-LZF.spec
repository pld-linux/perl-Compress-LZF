#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Compress
%define		pnam	LZF
Summary:	Compress::LZF Perl module - extremely leight-weight Lev-Zimpel-Free compression
Summary(pl.UTF-8):	Moduł Perla Compress::LZF - ekstremalnie lekka kompresja Lev-Zimpel-Free
Name:		perl-Compress-LZF
Version:	3.43
Release:	11
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Compress/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	b9dcb1bae6dc48ec45dd370e75000c05
URL:		http://search.cpan.org/dist/Compress-LZF/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
LZF is an extremely fast (not that much slower than a pure memcpy)
compression algorithm. It is ideal for applications where you want to
save *some* space but not at the cost of speed. It is ideal for
repetitive data as well. The module is self-contained and very small
(no large library to be pulled in). It is also free, so there should
be no problems incoporating this module into commercial programs. It
is believed that it is free from any patents.

%description -l pl.UTF-8
LZF jest ekstremalnie szybkim (nie tak dużo wolniejszym od memcpy)
algorytmem kompresji. Jest idealny dla programów, które chcą
zaoszczędzić *trochę* miejsca, ale nie kosztem szybkości. Jest idealny
dla powtarzających się danych. Moduł jest mały i nie wymaga żadnej
dodatkowej dużej biblioteki. Jest wolnodostępny, więc nie powinno być
problemów z wykorzystaniem go w komercyjnych programach. Według
aktualnego stanu wiedzy jest wolny od patentów.

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

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorarch}/Compress/LZF.pm
%dir %{perl_vendorarch}/auto/Compress/LZF
%attr(755,root,root) %{perl_vendorarch}/auto/Compress/LZF/*.so
%{_mandir}/man3/Compress::LZF.3pm*
