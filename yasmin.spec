Summary:	8051 simulator
Summary(pl):	Symulator 8051
Name:		yasmin
Version:	0.6.0
Release:	1
Epoch:		1
License:	GPL
Group:		X11/Applications
Group(de):	X11/Applikationen
Group(pl):	X11/Aplikacje
Source0:	http://home.tiscalinet.be/genglebi/packages/%{name}-%{version}.tar.gz
Patch0:		%{name}-make.patch
Patch1:		%{name}-c++.patch
URL:		http://home.tiscalinet.be/genglebi/
BuildRequires:	qt-devel
BuildRequires:	libpng-devel
BuildRequires:	zlib-devel
BuildRequires:	libstdc++-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6

%description
Yasmin (which stands for Yet Another Simulating Interpreter) is a
simple yet powerfull interpreted 80c51 simulator. The program reads
your assembler code, and simulates the execution of this on an intel
8051 microcontroler. The simulator contains a complete development
environment, which includes breakpoints, stepwise running through the
program (Step in, step out, step over), overview of the data memory,
clear overview of the special function registers, etc...

%description -l pl
Yasmin jest prostym ale o du¿ych mo¿liwo¶ciach symulatorem
mikrokontrolera 80c51. Program czyta Twój kod asemblera i symuluje
jego wykonanie na mikrokontrolerze. Symylator zawiera pe³ne ¶rodowisko
developerskie w³±czaj±c w to breakpointy, pracê krokow±, przegl±d
pamiêci danych, rejestrów itp.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
touch *.h
OPT_FLAGS="%{?debug:-O0 -g}%{!?debug:$RPM_OPT_FLAGS}" %{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}

install %{name} $RPM_BUILD_ROOT%{_bindir}

gzip -9nf AUTHORS BUGS README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz examples
%attr(755,root,root) %{_bindir}/*
