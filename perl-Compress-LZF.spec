%include	/usr/lib/rpm/macros.perl
%define		pdir	Compress
%define		pnam	LZF
Summary:	Compress::LZF Perl module - extremely leight-weight Lev-Zimpel-Free compression
Summary(pl):	Modu� Perla Compress::LZF - ekstremalnie lekka kompresja Lev-Zimpel-Free
Name:		perl-Compress-LZF
Version:	0.1045
Release:	2
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	27a609103341c8b3bff921eef5429e96
BuildRequires:	perl-devel >= 5.6
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

%description -l pl
LZF jest ekstremalnie szybkim (nie tak du�o wolniejszym od memcpy)
algorytmem kompresji. Jest idealny dla program�w, kt�re chc�
zaoszcz�dzi� *troch�* miejsca, ale nie kosztem szybko�ci. Jest idealny
dla powtarzaj�cych si� danych. Modu� jest ma�y i nie wymaga �adnej
dodatkowej du�ej biblioteki. Jest wolnodost�pny, wi�c nie powinno by�
problem�w z wykorzystaniem go w komercyjnych programach. Wed�ug
aktualnego stanu wiedzy jest wolny od patent�w.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
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
%{perl_vendorarch}/Compress/LZF.pm
%dir %{perl_vendorarch}/auto/Compress/LZF
%{perl_vendorarch}/auto/Compress/LZF/*.bs
%attr(755,root,root) %{perl_vendorarch}/auto/Compress/LZF/*.so
%{_mandir}/man3/*
