import Pyro4

@Pyro4.expose
class Greeting:
    def say_hello(self, name):
        return f"Hello, {name}!"

if __name__ == "__main__":
    # Setup daemon and name server
    daemon = Pyro4.Daemon()
    ns = Pyro4.locateNS()

    # Register object instance
    greeting_uri = daemon.register(Greeting())

    # Register with name server
    ns.register("example.greeting", greeting_uri)

    print("Server is ready...")
    daemon.requestLoop()
