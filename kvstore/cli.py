from kvstore.store import KeyValueStore

CMD_IDX = 0
KEY_IDX = 1
VALUE_IDX = 2

GET_CMD = "get"
SET_CMD = "set"
EXIT_CMD = "exit"
OTHER_CMD = "unknown"

class KVApp:
    def __init__(self, path):
        self.store = KeyValueStore(path)
        print("Welcome to KV Store. Use commands get, set, and exit")
        print("Example: get 'mykey'")
        print("Example: set 'mykey' 'myvalue'")

    def get_input(self):
        return input(">>> ")
    
    def run(self):
        while True:
            try:
                input = self.get_input()
                self.handle_input(input)
            except KeyboardInterrupt:
                self.handle_exit()

    def handle_input(self, input):
        command = self._classify_input(input)
        if command == GET_CMD:
            self.handle_get(input)
        elif command == SET_CMD:
            self.handle_set(input)
        elif command == EXIT_CMD:
            self.handle_exit()
        else:
            self.handle_unknown()

    def handle_get(self, input):
        elements = self._parse_input(input)
        if len(elements) < 2:
            print("Invalid get command")

        key = elements[KEY_IDX]
        value = self.store.get(key)

        if value is None:
            print(f"Key {key} not found")
        else:
            print(f"Value: {value}")
    
    def handle_set(self,input ):
        elements = self._parse_input(input)
        if len(elements) < 3:
            print("Invalid set command")
        
        key = elements[KEY_IDX]
        value = elements[VALUE_IDX]

        self.store.set(key, value)
        print(f"Key {key} set to {value}")

    def handle_exit(self):
        print("\nSaving...")
        self.store.shutdown()
        print("\nShutting down...")
        exit(0)
    
    def handle_unknown(self):
        print("Unknown command")

    def _parse_input(self, input):
        return input.split(" ")
    
    def _classify_input(self, input):
        elements = self._parse_input(input)
        if len(elements) < 1:
            return None
        command = elements[0]
        if command == GET_CMD:
            return GET_CMD
        elif command == SET_CMD:
            return SET_CMD
        elif command == EXIT_CMD:
            return EXIT_CMD
        else:
            return OTHER_CMD


def main():
    app = KVApp("kvstore.pkl")
    app.run()

if __name__ == "__main__":
    main()