import Pyro4

# Connect to the server
greeting_uri = "PYRONAME:example.greeting"
greeting = Pyro4.Proxy(greeting_uri)

# Bind the proxy (optional; Pyro will bind automatically on first use)
greeting._pyroBind()

# Call the method with credentials
print(greeting.say_hello("Alice", "secret"))
