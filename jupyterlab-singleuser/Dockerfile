FROM jupyter/scipy-notebook:2023-09-11

LABEL MAINTAINER="Patrick Young <16604643+kmahyyg@users.noreply.github.com>"
LABEL BUILT_ON="20230916"

VOLUME [ "/home/${NB_USER}/public", "/home/${NB_USER}/work" ]

COPY --chown=${NB_USER}:${NB_USER} .condarc "/home/${NB_USER}"

USER root
RUN sed -i 's/security.ubuntu.com/mirrors.ustc.edu.cn/g' /etc/apt/sources.list && \
    sed -i 's/archive.ubuntu.com/mirrors.ustc.edu.cn/g' /etc/apt/sources.list

USER ${NB_USER}
RUN pip3 config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple && \
    conda clean -i && \
    mamba install -c conda-forge --yes 'elasticsearch==8.9.0' \
    'elasticsearch-dsl==8.9.0' \
    'jupyterhub==4.0.2' && \
    mamba clean --all -f -y && \
    fix-permissions "${CONDA_DIR}" && \
    fix-permissions "/home/${NB_USER}"
