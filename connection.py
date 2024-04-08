class Connection:
    def __init__(self, **kwargs):
        self.driver: str = kwargs['driver']
        self.use_ssh: bool = kwargs.get("use_ssh", False)
        self.ssh_config: str = kwargs.get('ssh_config', "")
        self.host: str = kwargs.get('host', "localhost")
        self.port: str = kwargs.get('port', "3306")
        self.user: str = kwargs.get('user', "root")
        self.password: str = kwargs.get('password', "password")

        self.__verify_driver()

    def __verify_driver(self):
        pass
