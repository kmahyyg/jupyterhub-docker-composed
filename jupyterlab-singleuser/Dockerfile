FROM jupyter/scipy-notebook:2023-09-11

LABEL MAINTAINER="Patrick Young <16604643+kmahyyg@users.noreply.github.com>"
LABEL BUILT_ON="20230916"

VOLUME [ "/home/${NB_USER}/public", "/home/${NB_USER}/work" ]

COPY --chown=${NB_USER}:${NB_USER} .condarc "/home/${NB_USER}"

USER root
RUN sed -i 's/security.ubuntu.com/mirrors.ustc.edu.cn/g' /etc/apt/sources.list && \
    sed -i 's/archive.ubuntu.com/mirrors.ustc.edu.cn/g' /etc/apt/sources.list && \
    curl -L -o /tmp/pwsh.deb "https://github.com/PowerShell/PowerShell/releases/download/v7.2.15/powershell-lts_7.2.15-1.deb_amd64.deb" && \
    dpkg -i /tmp/pwsh.deb && \
    apt update -y && \
    apt install -f -y && \
    rm -rf /tmp/pwsh.deb /var/cache/apt && \
    ln -sf /usr/bin/pwsh /usr/bin/powershell && \
    pwsh -NonInteractive -command 'Set-PsRepository -Name PSGallery -InstallationPolicy trusted; Install-Module Microsoft.Graph; Install-Module Microsoft.Graph.Beta; Install-Module ExchangeOnlineManagement' && \
    unset http_proxy https_proxy

USER ${NB_USER}
RUN pip3 config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple && \
    conda clean -i && \
    mamba install -c conda-forge --yes 'elasticsearch==8.9.0' \
    'elasticsearch-dsl==8.9.0' \
    'jupyterhub==4.0.2' && \
    mamba clean --all -f -y && \
    mkdir -p /home/jovyan/.config/powershell && \
    echo 'Set-PSReadLineOption -HistorySaveStyle SaveNothing' > /home/jovyan/.config/powershell/Microsoft.PowerShell_profile.ps1

USER root
RUN fix-permissions "${CONDA_DIR}" && \
    fix-permissions "/home/${NB_USER}"

USER ${NB_USER}
