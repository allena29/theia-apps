ARG NODE_VERSION=12.18.3

FROM node:${NODE_VERSION}
# Install Python 3 from source
ARG VERSION=3.7.3

RUN apt-get update \
    && apt-get upgrade -y \
    && apt-get install -y make build-essential libssl-dev rsync \
    && apt-get install -y libbz2-dev libreadline-dev libsqlite3-dev wget curl llvm \
    && apt-get install -y libncurses5-dev  libncursesw5-dev xz-utils tk-dev \
    && wget https://www.python.org/ftp/python/$VERSION/Python-$VERSION.tgz \
    && tar xvf Python-$VERSION.tgz \
    && cd Python-$VERSION \
    && ./configure --prefix=/usr/local \
    && make -j8 \
    && make install \
    && cd .. \
    && rm -rf Python-$VERSION \
    && rm Python-$VERSION.tgz


RUN \
      mkdir /cleanpython && \
      rsync -avz --exclude='n*' --exclude='yarn*' /usr/local/bin /cleanpython/ && \
      rsync -avz  --exclude='test/' --exclude='__pycache__/' /usr/local/lib/python3.7 /cleanpython/lib/  && \
      rsync -avz  --exclude='test/' --exclude='__pycache__/' /usr/local/lib/pkgconfig /cleanpython/lib/  &&  \
      rsync -avz  --exclude='test/' --exclude='__pycache__/' /usr/local/include/python3.7m /cleanpython/include/  &&  \
      rsync -avz  --exclude='test/' --exclude='__pycache__/' /usr/local/lib/libpython3.7m.a /cleanpython/lib/ && \
      cd /cleanpython && \
      tar cvpfz /python-3.7-debian-9.tar.gz bin include lib

