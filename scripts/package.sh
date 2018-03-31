#!/bin/bash

mkdir -p $HOME/rpmbuild/SOURCES
rm $HOME/rpmbuild/SOURCES/root.tar.gz
tar -zcvf $HOME/rpmbuild/SOURCES/root.tar.gz ./config ./public

rpmbuild -bb package.spec --define "_release $TRAVIS_JOB_ID"

mkdir -p ./travis-build
mv $HOME/rpmbuild/RPMS/noarch/*.rpm ./travis-build/myelin-website.rpm
