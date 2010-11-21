all:
	python2.5 setup.py build
clean:
	python2.5 setup.py clean --all
install:
	python2.5 setup.py install \
	--root $(DESTDIR)
