from jupyter_client import LocalProvisioner


class RBACProvisioner(LocalProvisioner):
    role: str = Unicode(config=True)

    async def pre_launch(self, **kwargs: Any) -> Dict[str, Any]:
        """
        Pre Launch
        """

        print("doing prelaunch")
        return await super().pre_launch(**kwargs)
