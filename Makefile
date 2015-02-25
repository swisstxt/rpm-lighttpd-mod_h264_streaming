HOME=$(shell pwd)
VERSION="1.4.35"
NAME=lighttpd-mod_h264_streaming
RELEASE=$(shell /opt/buildhelper/buildhelper getgitrev .)
SPEC=$(shell /opt/buildhelper/buildhelper getspec ${NAME})
ARCH=$(shell /opt/buildhelper/buildhelper getarch)
OS_RELEASE=$(shell /opt/buildhelper/buildhelper getosrelease)


all: build

clean:
	rm -rf ./rpmbuild
	rm -rf ./SOURCES/lighttpd-*
	mkdir -p ./rpmbuild/SPECS/ ./rpmbuild/SOURCES/
	mkdir -p ./SPECS ./SOURCES

get-source:
	wget http://download.lighttpd.net/lighttpd/releases-1.4.x/lighttpd-${VERSION}.tar.gz -O ./SOURCES/lighttpd-${VERSION}.tar.gz

build: clean get-source
	cp -r ./SPECS/* ./rpmbuild/SPECS/ || true
	cp -r ./SOURCES/* ./rpmbuild/SOURCES/ || true
	rpmbuild -ba ${SPEC} \
	--define "ver ${VERSION}" \
	--define "rel ${RELEASE}" \
	--define "name ${NAME}" \
	--define "os_rel ${OS_RELEASE}" \
	--define "arch ${ARCH}" \
	--define "_topdir %(pwd)/rpmbuild" \
	--define "_builddir %{_topdir}" \
	--define "_rpmdir %{_topdir}" \
	--define "_srcrpmdir %{_topdir}" \

publish: 
	/opt/buildhelper/buildhelper pushrpm yum-01.stxt.media.int:8080/swisstxt-centos
