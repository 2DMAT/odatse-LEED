#!/bin/sh

set -e

if [ ! -e leedsatl.zip ]; then
  wget http://www.icts.hkbu.edu.hk/VanHove_files/leed/leedsatl.zip -O leedsatl.zip
fi
rm -rf src
unzip leedsatl.zip -d src
cd src
tr -d '\r' < leedsatl.m1 > satl1.f
tr -d '\r' < leedsatl.m2 > satl2.f
tr -d '\r' < leedsatl.sb > satl_sub.f
patch -up1 < ../leedsatl.patch
patch -up1 < ../leedsatl_pause.patch
patch -up1 < ../leedsatl_arraysize.patch
cat << EOF > Makefile
#FORT=ifort -debug full -O0 -real-size 64 -save -init=zero -traceback -check bounds -threads -fpe0
FORT=gfortran -g -O0 -fdefault-real-8 -finit-local-zero -fbacktrace -fbounds-check -ffpe-trap=invalid,zero,overflow
all: satl1.exe satl2.exe
satl1.exe: satl1.f satl_sub.f
	\$(FORT) -o satl1.exe satl1.f satl_sub.f
satl2.exe: satl2.f satl_sub.f
	\$(FORT) -o satl2.exe satl2.f satl_sub.f
clean:
	rm -rf satl1.exe satl2.exe
EOF
make
cp -p satl1.exe satl2.exe ..
