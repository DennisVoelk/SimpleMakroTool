from pynput.keyboard import Key, Listener, Controller

class KeyFunctions(object):
    def __init__(self):
        self.keys = []

    def addKey(self, key):
        if key != Key.esc:
            self.keys.append(key)

    def on_press(self, key):
        print('{0} pressed'.format(key))
        self.addKey(key)

    def on_release(self, key):
        if key == Key.esc:
            return False

    def listen(self):
        with Listener(on_press=self.on_press,on_release=self.on_release) as listener:
            listener.join()

    def start(self):
        self.keys = []
        self.listen()
        return self.keys

    def execute(self, keyList):
        keyboard = Controller()
        for key in keyList:
            keyboard.press(key)
            keyboard.release(key)