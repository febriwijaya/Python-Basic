def say_hello(name):
    return f"Hello {name}"

def be_awesome(name):
    return f"Yo {name}, together we are the awesomest!"

def greet_bob(greeter_func):
    return greeter_func("Bob")

def weather_talk(name):
  return f"The weather is nice, {name}"

print(say_hello('febri'))
print(greet_bob(be_awesome))
print(greet_bob(say_hello))
print(greet_bob(weather_talk))