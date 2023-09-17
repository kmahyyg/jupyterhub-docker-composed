# Configuration file for jupyterhub.

c = get_config()  #noqa

c.JupyterHub.active_server_limit = 30
c.JupyterHub.active_user_window = 900
c.JupyterHub.activity_resolution = 30

import os, nativeauthenticator
c.JupyterHub.authenticator_class = 'native'
c.JupyterHub.template_paths = [f"{os.path.dirname(nativeauthenticator.__file__)}/templates/"]
c.Authenticator.delete_invalid_users = True
c.Authenticator.refresh_pre_spawn = True
c.Authenticator.username_pattern = r'^dev-'
c.Authenticator.admin_users = {"dev-admin"}
c.NativeAuthenticator.check_common_password = True
c.NativeAuthenticator.minimum_password_length = 12
c.NativeAuthenticator.allowed_failed_logins = 5
c.NativeAuthenticator.seconds_before_next_try = 1800
c.NativeAuthenticator.allow_2fa = True
c.NativeAuthenticator.ask_email_on_signup = True
c.NativeAuthenticator.tos = "I accept the ToS and promise to keep my account safe as possible as I can."

c.JupyterHub.cookie_max_age_days = 7
c.JupyterHub.db_url = 'sqlite:///db/jupyterhub.sqlite'
c.JupyterHub.upgrade_db = True
c.JupyterHub.hub_ip = os.getenv("MY_PAAS_JHUB_IP") or '127.0.0.1'
c.JupyterHub.load_roles = [
    {
        "name": "jupyterhub-idle-culler-role",
        "scopes": [
            "list:users", "read:users:activity",
            "read:servers", "delete:servers",
        ],
        "services": ["jupyterhub-idle-culler-service"],
    }
]
import sys
c.JupyterHub.services = [
    {
        "name": "jupyterhub-idle-culler-service",
        "command": [sys.executable, "-m", "jupyterhub_idle_culler", "--timeout=3600"]
    }
]

c.JupyterHub.concurrent_spawn_limit = 8
c.JupyterHub.spawner_class = 'dockerspawner.DockerSpawner'
notebook_dir = os.getenv("DOCKER_NOTEBOOK_DIR") or '/home/jovyan/work'
c.DockerSpawner.notebook_dir = notebook_dir
c.DockerSpawner.volumes = { 
    '/userdata/isolation/{username}': notebook_dir
}
c.DockerSpawner.image = 'jupyterlab-singleuser'
c.DockerSpawner.read_only_volumes = {
    '/userdata/public': '/home/jovyan/public',
}
c.DockerSpawner.remove = True
c.DockerSpawner.pull_policy = 'never'
c.DockerSpawner.use_internal_ip = True
c.DockerSpawner.network_name = os.getenv("DOCKER_NETWORK_NAME")
c.Spawner.default_url = '/lab'
c.Spawner.disable_user_config = True
c.Spawner.mem_limit = "1G"
c.Spawner.cpu_limit = 2
c.Spawner.start_timeout = 60
