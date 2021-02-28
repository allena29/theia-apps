ARG NODE_VERSION=12.18.3

FROM node:${NODE_VERSION}
ARG version=latest
WORKDIR /home/theia
ADD $version.package.json ./package.json
ARG GITHUB_TOKEN
RUN yarn --pure-lockfile && \
    NODE_OPTIONS="--max_old_space_size=4096" yarn theia build && \
    yarn theia download:plugins && \
    yarn --production && \
    yarn autoclean --init && \
    echo *.ts >> .yarnclean && \
    echo *.ts.map >> .yarnclean && \
    echo *.spec.* >> .yarnclean && \
    yarn autoclean --force && \
    yarn cache clean


# Install Python 3 from a pre-compiled tar

# Install Python 3 from source 
#ARG VERSION=3.7.3
#
#RUN apt-get update \
#    && apt-get upgrade -y \
#    && apt-get install -y make build-essential libssl-dev \
#    && apt-get install -y libbz2-dev libreadline-dev libsqlite3-dev wget curl llvm \
#    && apt-get install -y libncurses5-dev  libncursesw5-dev xz-utils tk-dev \
#    && wget https://www.python.org/ftp/python/$VERSION/Python-$VERSION.tgz \
#    && tar xvf Python-$VERSION.tgz \
#    && cd Python-$VERSION \
#    && ./configure --prefix=/usr/local \
#    && make -j8 \
#    && make install \
#    && cd .. \
#    && rm -rf Python-$VERSION \
#    && rm Python-$VERSION.tgz

#RUN apt-get update && \
#    apt-get install -y openjdk-8-jre  \
#    && rm -rf /var/cache/apt/* \
#    && rm -rf /var/lib/apt/lists/* \
#    && rm -rf /tmp/*

#ARG PRE_COMPILED_PYTHON_URL=http://mycrap.mellon-collie.net/docker-tools/python-3.7-debian-9.tar.gz
#RUN wget -O /dev/stdout $PRE_COMPILED_PYTHON_URL | tar xvfz - -C /usr/local && \
#    pip3 install python-language-server flake8 autopep8 pylint 

#RUN curl https://bootstrap.pypa.io/3.5/get-pip.py  | python3 && \
#    pip3 install python-language-server flake8 autopep8 pylint 

RUN mkdir -p /home/theia \
    && mkdir -p /home/project
ENV HOME /home/theia
WORKDIR /home/theia
#COPY --from=0 /home/theia /home/theia
#COPY  /home/theia /home/theia
EXPOSE 3000
ENV SHELL=/bin/bash \
    THEIA_DEFAULT_PLUGINS=local-dir:/home/theia/plugins
ENV USE_LOCAL_GIT true
ENTRYPOINT [ "node", "/home/theia/src-gen/backend/main.js", "/home/project", "--hostname=0.0.0.0" ]
