Summary: IOzone Filesystem Benchmark
Name: iozone
%define real_version 3_482
Version: 3.482
Release: 1%{?dist}
License: Freeware
Group: Applications/System
URL: http://www.iozone.org/

Source: http://www.iozone.org/src/current/iozone%{real_version}.tar
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
Requires: perl-Readonly, perl-List-MoreUtils
%description
IOzone is a filesystem benchmark tool. The benchmark generates and
measures a variety of file operations. Iozone has been ported to
many machines and runs under many operating systems.

Iozone is useful for performing a broad filesystem analysis of a vendors
computer platform. The benchmark tests file I/O performance for the following
operations: Read, write, re-read, re-write, read backwards, read strided,
fread, fwrite, random read, pread ,mmap, aio_read, aio_write.

%prep
%setup -n %{name}%{real_version}

%build
%{__make} %{?_smp_mflags} -C src/current linux

%install
%{__rm} -rf %{buildroot}
%{__install} -Dp -m0755 src/current/iozone %{buildroot}%{_bindir}/iozone
%{__install} -Dp -m0755 src/current/Generate_Graphs %{buildroot}%{_datadir}/iozone/Generate_Graphs
%{__install} -Dp -m0755 src/current/gengnuplot.sh %{buildroot}%{_datadir}/iozone/gengnuplot.sh
%{__install} -Dp -m0755 src/current/gnu3d.dem %{buildroot}%{_datadir}/iozone/gnu3d.dem

%{__install} -Dp -m0644 docs/iozone.1 %{buildroot}%{_mandir}/man1/iozone.1

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc src/current/Changes.txt src/current/Gnuplot.txt
%doc src/current/*.pl src/current/*.sh docs/*
%doc %{_mandir}/man1/iozone.1*
%{_bindir}/iozone
%{_datadir}/iozone/

