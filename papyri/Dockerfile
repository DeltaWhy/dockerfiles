FROM alpine:latest

ARG VIPS_VERSION=8.7.1
ARG VIPS_URL=https://github.com/libvips/libvips/releases/download

RUN apk update && apk upgrade

# basic packages libvips likes
RUN apk add \
	build-base \
	autoconf \
	automake \
	libtool \
	bc \
	zlib-dev \
	expat-dev \
	jpeg-dev \
	tiff-dev \
	glib-dev \
	libjpeg-turbo-dev \
	libexif-dev \
	lcms2-dev \
	fftw-dev \
	giflib-dev \
	libpng-dev \
	libwebp-dev \
	orc-dev \
	libgsf-dev

# add these if you like for text rendering, PDF rendering, SVG rendering,
# but they will pull in loads of other stuff
# RUN apk add \
# 	gdk-pixbuf-dev \
# 	poppler-dev \
# 	librsvg-dev

# there are other optional deps you can add for openslide / openexr /
# imagmagick support / Matlab support etc etc

RUN wget -O- ${VIPS_URL}/v${VIPS_VERSION}/vips-${VIPS_VERSION}.tar.gz | tar xzC /tmp
RUN cd /tmp/vips-${VIPS_VERSION} \
	&& ./configure --prefix=/usr --disable-static --disable-debug \
	&& make V=0 \
	&& make install

RUN apk add \
	git \
	python3-dev \
	py3-pip \
	py3-pillow \
	tini

# and now pyvips can go on
RUN pip3 install pyvips nbt requests

ENV SCHEDULE="0 0 * * *"
ENTRYPOINT ["/sbin/tini", "--"]
RUN git clone https://github.com/jason-green-io/minecraftmap \
	&& cd /minecraftmap \
	&& python3 setup.py build \
	&& python3 setup.py install \
	&& rm -rf /minecraftmap
RUN git clone https://github.com/jason-green-io/papyri /app
ADD papyri.sh /
ADD run.sh /
WORKDIR /app
CMD /run.sh

# FROM codechimpio/vips-alpine AS alpine
# ENV SCHEDULE="0 0 * * *"
# RUN apk add --update rsync tini dcron git python3 py3-pillow python3-dev glib-dev libffi-dev jpeg-dev gcc make libc-dev
# ENTRYPOINT ["/sbin/tini", "--"]
# RUN python3 -m pip install nbt requests pyvips
# RUN git clone https://github.com/jason-green-io/minecraftmap \
# 	&& cd /minecraftmap \
# 	&& python3 setup.py build \
# 	&& python3 setup.py install \
# 	&& rm -rf /minecraftmap
# RUN git clone https://github.com/jason-green-io/papyri /app
# #ADD backup.sh /
# ADD run.sh /
# WORKDIR /app
# CMD /run.sh

# FROM python:3
# RUN apt-get update && apt-get install -y --no-install-recommends \
# 	libvips \
# 	glib2.0-dev \
# 	libffi-dev
# RUN pip install nbt Pillow requests pyvips
# RUN git clone https://github.com/jason-green-io/minecraftmap \
# 	&& cd /minecraftmap \
# 	&& python setup.py build \
# 	&& python setup.py install \
# 	&& rm -rf /minecraftmap
# RUN git clone https://github.com/jason-green-io/papyri /app
# COPY run.sh /
# WORKDIR /app
# CMD /run.sh
