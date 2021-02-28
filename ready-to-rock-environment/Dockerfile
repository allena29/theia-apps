FROM allena29/theia-python:latest


#RUN apt-get update \
#    && apt-get install -y libprotobuf-c1 libev4 libavl1 curl openssh-client git screen cmake build-essential \
#    supervisor libpcre3-dev pkg-config libavl-dev libev-dev libprotobuf-c-dev protobuf-c-compiler libssl-dev \
#    libcurl4-openssl-dev libxslt-dev libxml2-dev libtool libtool-bin libreadline-dev libprotobuf-dev zlib1g-dev \
#    bison libboost-thread1.62-dev autoconf automake libffi-dev vim git tmux python3-dev libffi-dev libssl-dev \
#    openssh-server telnet sudo git \ 
#    && rm -rf /var/cache/apt/* \
#    && rm -rf /var/lib/apt/lists/* \
#    && rm -rf /tmp/* && \
#    mkdir /run/sshd && \
#    dpkg-reconfigure openssh-server

#RUN apt-get update \
#    && apt-get install -y openssh-client git tmux telnet openssh-server sudo vim \
#    libpcre3-dev pkg-config libavl-dev libev-dev cmake libxml2-dev libxslt-dev libffi-dev \ 
#    && rm -rf /var/cache/apt/* \
#    && rm -rf /var/lib/apt/lists/* \
#    && rm -rf /tmp/* && \
#    mkdir /run/sshd && \
#    dpkg-reconfigure openssh-server 

RUN apt-get update \
    && apt-get install -y openssh-client git tmux telnet openssh-server sudo vim \
    libpcre3-dev libavl-dev libev-dev cmake libxml2-dev libxslt-dev libffi-dev \ 
    && rm -rf /var/cache/apt/* \
    && rm -rf /var/lib/apt/lists/* \
    && rm -rf /tmp/* && \
    mkdir /run/sshd && \
    dpkg-reconfigure openssh-server 
ADD dot-theia /home/theia/.theia 

RUN \
  curl http://mystuff.mellon-collie.net/docker-tools/libyang-debian-v1.0.184.tar.gz | tar xvfz - -C / && \
  ldconfig


COPY  example /home/project/example

ENV RUN_THEILA=Y
arg UID=1002
arg USER=developer
arg PASSWD=somepassword
RUN useradd -u $UID $USER && \
    usermod -s /bin/bash -d /home/project $USER && \
    echo "$USER:$PASSWD" | chpasswd && \
    mkdir /pyenv && \
    touch /example-home.tar && \
    chown $USER /home -R && \
    chown $USER /pyenv && \
    chown $USER /example-home.tar && \
    echo "$USER ALL=(ALL) NOPASSWD: /usr/bin/make" >>/etc/sudoers && \
    echo "$USER ALL=(ALL) NOPASSWD: /sbin/ldconfig" >>/etc/sudoers && \
    echo "$USER ALL=(ALL) NOPASSWD: /usr/sbin/sshd" >>/etc/sudoers && \ 
    echo 'export PYENV_ROOT="/pyenv"' >/pyenv-activate && \
    echo 'export PATH="$PYENV_ROOT/bin:$PATH"' >>/pyenv-activate && \
    echo 'eval "$(pyenv init -)"' >>/pyenv-activate && \
    echo 'eval "$(pyenv virtualenv-init -)"' >>/pyenv-activate  && \
    echo 'export PYENV_VIRTUALENV_DISABLE_PROMPT=1' >>/pyenv-activate && \
    echo "#!/bin/bash" > /startup && \
    echo 'source /pyenv-activate' >>/startup && \
    echo 'source /pyenv-activate' >/home/theia/.bashrc && \
    echo 'source ~/.bashrc' >>~/.profile && \
    echo "sudo /usr/sbin/sshd" >> /startup && \
    echo 'if [ "$RUN_THEILA" == "Y" ]' >>/startup && \
    echo 'then' >>/startup && \
    echo "  node /home/theia/src-gen/backend/main.js /home/project --hostname 0.0.0.0" >> /startup && \
    echo 'else' >>/startup && \
    echo '  sleep infinity' >>/startup && \
    echo "fi" >> /startup && \
    mkdir -p /home/$USER/.ipython/profile_default && \
    echo "c.TerminalInteractiveShell.confirm_exit = False" >/home/$USER/.ipython/profile_default/ipython_config.py && \
    echo "c.Completer.use_jedi = False" >> /home/$USER/.ipython/profile_default/ipython_config.py && \
    chmod 755 /startup  && \
    cp /home/theia/.profile /home/project

USER $USER


#arg PYTHON_VERSION=3.7.3
#RUN \
#    git clone https://github.com/pyenv/pyenv.git /pyenv && \
#    git clone https://github.com/pyenv/pyenv-virtualenv.git /pyenv/plugins/pyenv-virtualenv  && \
#    export PATH=/pyenv/bin:$PATH && \
#    eval "$(pyenv init -)" && \
#    export PYENV_ROOT="/pyenv" && \
#    pyenv install $PYTHON_VERSION
#    rm -fr pyenv/versions/3.7.3/lib/python3.7/test
#    tar cvpfz /tmp/pyenv-3.7.3.tar.gz --exclude *.pyc --exclude __pycache__ --exclude test_* /pyenv
#

 

RUN \
     curl http://mystuff.mellon-collie.net/docker-tools/pyenv-3.7.3.tar.gz | tar xvfz - -C / && \
     echo "3.7.3/envs/example" >/home/project/.python-version && \
     export PYENV_ROOT="/pyenv" && \
     export PATH=/pyenv/bin:$PATH && \
     eval "$(pyenv init -)" && \
     pyenv virtualenv 3.7.3 example  && \
     pyenv activate example && \ 
     pip3 install python-language-server flake8 autopep8 pylint ipython==7.6.1 behave==1.2.6 pytest==6.2.1 && \
     pip3 install http://mystuff.mellon-collie.net/docker-tools/libyang-0.16.79.dev77-cp37-cp37m-linux_x86_64.whl && \
     pip3 install http://mystuff.mellon-collie.net/docker-tools/yangvoodoo-0.0.8.6-py3-none-any.whl && \
     echo 'source /pyenv-activate' >>/home/project/.bashrc  && \
     echo 'export YANGPATH="/home/project/example/yang"' >>/home/project/.bashrc  && \
     cd /home/ && \
     tar cvpf /example-home.tar project && \
     cd /home/project/example && \
     git init . && \
     git config --global user.email "fred.flintstone@example" && \
     git config --global user.name "Fred Flinstone" && \
     git add . && \
     git commit -m 'First commit - the example'



#     mkdir -p /home/project/example/yang



#arg LIBYANG_BRANCH="v1.0.184"
#RUN \
#  git clone -b $LIBYANG_BRANCH https://github.com/CESNET/libyang.git && \
#  cd libyang && \
#  mkdir build && \
#  cd build && \
#  cmake .. && \
#  make && \
#  mkdir /tmp/clean-libyang && \
#  DESTDIR=/tmp/clean-libyang/ make install && \
#  cd /tmp/clean-libyang && \
#  tar cvpfz /tmp/libyang-debian-1.0.184.tar.gz .


ENTRYPOINT [ "/startup" ]


# At this point we can log into the container and tar up the pyenv to extract to avoid
# bloating the container compling pytenv from source
