import pickle

class KeyValueStore:
    def __init__(self, path: str='kvstore.pkl'):
        self.path: str = path
        self.store: dict = self._load()

    def get(self, key: str):
        if key in self.store:
            return self.store[key]

        return None

    def set(self, key: str, value: str):
        self.store[key] = value
    
    def _persist(self):
        with open(self.path, 'wb') as f:
            pickle.dump(self.store, f)

    def _get_persisted_data(self): 
        with open(self.path, 'rb') as f:
            return pickle.load(f)

    def _load(self) -> dict:
        try:
            return self._get_persisted_data()
        except FileNotFoundError:
            return dict()
    
    def shutdown(self):
        self._persist()