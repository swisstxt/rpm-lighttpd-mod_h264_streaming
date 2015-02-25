Name:           %{name}
Version:        %{ver}
Release:        %{rel}%{?dist}
Summary:        H264 Streaming Module for Lighttpd
BuildArch:      %{arch}
Group:          Application/Internet
License:        BSD License
URL:            http://h264.code-shop.com/trac/wiki/Mod-H264-Streaming-Lighttpd-Version2
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n) 

Source0:        http://download.lighttpd.net/lighttpd/releases-1.4.x/lighttpd-%{ver}.tar.gz

Source1:        mod_h264_streaming.c
Source2:        mod_streaming_export.h
Source3:        moov.c
Source4:        moov.h
Source5:        mp4_io.c
Source6:        mp4_io.h
Source7:        mp4_process.c
Source8:        mp4_process.h
Source9:        mp4_reader.c
Source10:       mp4_reader.h
Source11:       mp4_writer.c
Source12:       mp4_writer.h
Source13:       output_bucket.c
Source14:       output_bucket.h
Source15:       output_mp4.c
Source16:       output_mp4.h

Patch0:         Makefile.patch

Requires:       lighttpd

%description
H264 Streaming Module for Lighttpd

%prep
%setup -q -n lighttpd-%{version}
%patch0 -p0
cp -p %SOURCE1 ./src/
cp -p %SOURCE2 ./src/
cp -p %SOURCE3 ./src/
cp -p %SOURCE4 ./src/
cp -p %SOURCE5 ./src/
cp -p %SOURCE6 ./src/
cp -p %SOURCE7 ./src/
cp -p %SOURCE8 ./src/
cp -p %SOURCE9 ./src/
cp -p %SOURCE10 ./src/
cp -p %SOURCE11 ./src/
cp -p %SOURCE12 ./src/
cp -p %SOURCE13 ./src/
cp -p %SOURCE14 ./src/
cp -p %SOURCE15 ./src/
cp -p %SOURCE16 ./src/

%build
./autogen.sh
./configure --enable-maintainer-mode
make

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/lib64/lighttpd/
cp -r ./src/.libs/mod_h264_streaming.so $RPM_BUILD_ROOT/usr/lib64/lighttpd/

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%attr(0755,root,root) /usr/lib64/lighttpd/mod_h264_streaming.so

%changelog
* Mon Feb 25 2015 Daniel Menet <daniel.menet@swisstxt.ch> - 1.4.35
Initial creation

