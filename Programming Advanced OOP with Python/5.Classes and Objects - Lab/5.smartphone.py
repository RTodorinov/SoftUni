class Smartphone:
    def __init__(self, memory: int,):
        self.memory = memory
        self.apps = []
        self.is_on = False

    def power(self):
        ''' This turns on or off the phone '''
        if self.is_on:
            self.is_on = False
        else:
            self.is_on = True
    # self.is_on = True if not self.is_on else False

    def install(self, app: str, app_memory: int):
        if app_memory <= self.memory and self.is_on:
            self.apps.append(app)
            self.memory -= app_memory
            return f"Installing {app}"
        elif app_memory <= self.memory and not self.is_on:
            return f"Turn on your phone to install {app}"
        return f"Not enough memory to install {app}"

    def status(self):
        return f"Total apps: {len(self.apps)}. Memory left: {self.memory}"


smartphone = Smartphone(100)
print(smartphone.install("Facebook", 60))
smartphone.power()
print(smartphone.install("Facebook", 60))
print(smartphone.install("Messenger", 20))
print(smartphone.install("Instagram", 40))
print(smartphone.status())
print(Smartphone.power.__doc__)
print(Smartphone.__dict__)
p = Smartphone(100)
print(p.__dict__)

