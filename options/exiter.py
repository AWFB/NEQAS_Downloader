from registry import register

def handle_exit(opts):
    print('Cya!')
    exit()

register({
    'name': 'Exit',
    'handler': handle_exit,
})
