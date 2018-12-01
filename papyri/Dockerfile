FROM python:3
RUN apt-get update && apt-get install -y --no-install-recommends \
	libvips \
	glib2.0-dev \
	libffi-dev
RUN pip install nbt Pillow requests pyvips
RUN git clone https://github.com/jason-green-io/minecraftmap \
	&& cd /minecraftmap \
	&& python setup.py build \
	&& python setup.py install \
	&& rm -rf /minecraftmap
RUN git clone https://github.com/jason-green-io/papyri /app
COPY run.sh /
WORKDIR /app
CMD /run.sh
