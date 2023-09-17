# Jupyter Hub (Docker Compose-based)

Use "Docker Compose" to build a Jupyter Hub for Internal Service.

## Architecture

- JupyterHub container will be responsible for managing users and spawning containers, means orchestration. This image is based on [jupyterhub/jupyterhub](https://hub.docker.com/r/jupyterhub/jupyterhub) . This container will proxy services offered by new container to end user.
- JupyterLab_ImageBuilder container is only used to build Single User server image for further usage, which is highly customized based on [jupyter/scipy-notebook](https://hub.docker.com/r/jupyter/scipy-notebook/tags/) and pinned down for specific version of JupyterHub. This image can be seen as the same of [jupyterhub/singleuser](https://github.com/jupyterhub/jupyterhub/blob/main/singleuser/Dockerfile).

All containers and images mentioned above are changed to use China Mainland mirrors of Conda and Pypi, which is useful for censored network environment.

- SideCar_NetShoot is a sidecar container which may be helpful for you to diagnose network issues, optional.
- Reverse_Proxy is a traefik v2 container, Reverse Proxy proxied all traffic to backend and added TLS support in a easy way.

## Build And Usage

- Copy `.env.example` to `.env` and modify stuffs. Set `COMPOSE_PROJECT_NAME` as you want, `MY_PAAS_JHUB_HOST` should be set to public domain that JupyterHub will use.
- Change `jupyterhub/jupyterhub_config.py` according to your needs, to generate a new config and start from scratch, use `jupyterhub --generate-config`. For reference, click [here](https://jupyterhub.readthedocs.io/en/stable/reference/config-reference.html) .
- Customize Dockerfile under each directory and customize `docker-compose.yaml` to meet you needs.
- Create all underlying folders mentioned in `docker-compose.yaml` and `jupyterhub/jupyterhub_config.py` before you start.
- Replace your TLS certificate under `traefik/certs`, make sure use fullchain certificate.
- Change traefik dashboard authentication by using `htpasswd` and update `traefik/certs/usersFile`, make sure to use `bcrypt`. Default password is: `admin/admin`.
- Change traefik domain from `example.com` to the one you use in: `traefik/conf.d/dynrouter.toml`.
- Run `docker compose build` and `docker compose up -d` by root.
- Enjoy.

To isolate networking, add `internal: true` under `networks` of specific network definition.

## Known Issue

- https://github.com/jupyterhub/dockerspawner/issues/453 Volumes Permission Incorrect when creating for new users and bound to directory on local disk.

Workaround on host: (Make sure `fixperm-isolation.sh` can only be running by root and owned by root and permission should be 0755.)
```bash
root@debian:~/jobs# cat ./fixperm-isolation.sh
#!/bin/bash
chown -R 1000:1000 /userdata/isolation
root@debian:~/jobs# crontab -l
# Edit this file to introduce tasks to be run by cron.
# For more information see the manual pages of crontab(5) and cron(8)
#
# m h  dom mon dow   command
*/2 * * * * bash /root/jobs/fixperm-isolation.sh
```

## FAQ

Go: 
- https://jupyter-docker-stacks.readthedocs.io/en/latest/using/troubleshooting.html
- https://jupyter-docker-stacks.readthedocs.io/en/latest/using/recipes.html

## License

Licensed under [BuSL-1.1](https://spdx.org/licenses/BUSL-1.1.html), check [LICENSE](./LICENSE) for more information.

Copyright (C) 2023 PatMeow Inc.
Use of this software is govered by the Business Source License included in the [LICENSE](./LICENSE) file and at www.mariadb.com/bsl11.

Change Date: Three Years After Released Date of Each Version.

On the date above, in accordance with the Business Source License, use of this software will be governed by the open source license (ALv2) specified in the [LICENSE](./LICENSE) file.

## Credits

Check [CREDIT.md](./CREDIT.md).
