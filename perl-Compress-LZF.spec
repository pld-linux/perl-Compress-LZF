%include	/usr/lib/rpm/macros.perl
%define		pdir	Compress
%define		pnam	LZF
Summary:	Compress::LZF Perl module - extremely leight-weight Lev-Zimpel-Free compression
Summary(pl):	Modu³ Perla Compress::LZF - ekstremalnie lekka kompresja Lev-Zimpel-Free
Name:		perl-Compress-LZF
Version:	0.1045
Release:	1
License:	Artistic or GPL
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	perl-devel >= 5.6
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
LZF is an extremely fast (not that much slower than a pure memcpy)
compression algorithm. It is ideal for applications where you want to
save *some* space but not at the cost of speed. It is ideal for
repetitive data as well. The module is self-contained and very small
(no large library to be pulled in). It is also free, so there should
be no problems incoporating this module into commercial programs. It
is believed that it is free from any patents.

%description -l pl
LZF jest ekstremalnie szybkim (nie tak du¿o wolniejszym od memcpy)
algorytmem kompresji. Jest idealny dla programów, które chc±
zaoszczêdziæ *trochê* miejsca, ale nie kosztem szybko¶ci. Jest idealny
dla powtarzaj±cych siê danych. Modu³ jest ma³y i nie wymaga ¿adnej
dodatkowej du¿ej biblioteki. Jest wolnodostêpny, wiêc nie powinno byæ
problemów z wykorzystaniem go w komercyjnych programach. Wed³ug
aktualnego stanu wiedzy jest wolny od patentów.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL
%{__make} OPTIMIZE="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_sitearch}/Compress/LZF.pm
%dir %{perl_sitearch}/auto/Compress/LZF
%{perl_sitearch}/auto/Compress/LZF/*.bs
%attr(755,root,root) %{perl_sitearch}/auto/Compress/LZF/*.so
%{_mandir}/man3/*
