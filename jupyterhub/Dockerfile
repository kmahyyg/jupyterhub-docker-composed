FROM jupyterhub/jupyterhub:4.0.2

LABEL MAINTAINER="Patrick Young <16604643+kmahyyg@users.noreply.github.com>"
LABEL BUILT_ON="20230916"

COPY jupyterhub_config.py .

VOLUME ["/srv/jupyterhub/db"]

RUN pip3 config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple && \
    sed -i 's/security.ubuntu.com/mirrors.ustc.edu.cn/g' /etc/apt/sources.list && \
    sed -i 's/archive.ubuntu.com/mirrors.ustc.edu.cn/g' /etc/apt/sources.list

RUN pip3 install --no-cache-dir \
    dockerspawner==12.1.0 \
    jupyterhub-idle-culler==1.2.1 \
    jupyterhub-nativeauthenticator==1.2.0
