options = []

def register(option):
  options.append(option)

def available_options():
  # creates a dict from an array, like {1: option[0], 2: option[1], ..}
  return {i + 1: options[i] for i in range(0, len(options))}