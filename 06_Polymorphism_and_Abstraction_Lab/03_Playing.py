def start_playing(instance):
    return instance.play()


# Example usage
class ExampleClass:
    def play(self):
        return "Playing now..."


example_instance = ExampleClass()
play_function = start_playing(example_instance)
print(play_function)  # This will print "Playing now..."
