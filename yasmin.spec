Summary:	8051 simulator
Summary(pl.UTF-8):	Symulator 8051
Name:		yasmin
Version:	0.6.0
Release:	2
Epoch:		1
License:	GPL
Group:		X11/Applications
Source0:	http://home.tiscalinet.be/genglebi/packages/%{name}-%{version}.tar.gz
# Source0-md5:	0726b969a1431b0e9f9834defe9fbbe3
Patch0:		%{name}-make.patch
Patch1:		%{name}-c++.patch
Patch2:		%{name}-cast.patch
URL:		http://home.tiscalinet.be/genglebi/
BuildRequires:	libpng-devel
BuildRequires:	libstdc++-devel
BuildRequires:	qt-devel
BuildRequires:	zlib-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)


%description
Yasmin (which stands for Yet Another Simulating Interpreter) is a
simple yet powerfull interpreted 80c51 simulator. The program reads
your assembler code, and simulates the execution of this on an intel
8051 microcontroler. The simulator contains a complete development
environment, which includes breakpoints, stepwise running through the
program (Step in, step out, step over), overview of the data memory,
clear overview of the special function registers, etc...

%description -l pl.UTF-8
Yasmin jest prostym ale o dużych możliwościach symulatorem
mikrokontrolera 80c51. Program czyta Twój kod asemblera i symuluje
jego wykonanie na mikrokontrolerze. Symylator zawiera pełne środowisko
developerskie włączając w to breakpointy, pracę krokową, przegląd
pamięci danych, rejestrów itp.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1

%build
touch *.h
%{__make} \
	SYSCONF_CXX="%{__cxx}" \
	SYSCONF_LINK="%{__cxx}" \
	OPT_FLAGS="%{rpmcflags} -I%{_includedir}/qt -Wno-deprecated" \
	SYSCONF_MOC="%{_bindir}/moc"		\
	SYSCONF_LFLAGS_QT="-L%{_libdir}"	\
	SYSCONF_LIBS_QT="-lqt-mt"		\
	SYSCONF_LFLAGS_X11="-L%{_libdir}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}

install %{name} $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS BUGS README examples
%attr(755,root,root) %{_bindir}/*
