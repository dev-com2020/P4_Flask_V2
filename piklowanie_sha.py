import pickle
import hmac
import hashlib

secret_key = b'hfu673*&Tfgdyu'


def create_sig_pickle(data, filename='dane.pickle'):
    pkl_data = pickle.dumps(data)
    signature = hmac.new(secret_key, pkl_data, hashlib.sha256).hexdigest()
    with open(filename, 'wb') as file:
        file.write(pkl_data)
    return signature


def load_sig_pickle(file_path, signature):
    with open(file_path, 'rb') as file:
        pkl_data = file.read()
    if hmac.new(secret_key, pkl_data, hashlib.sha256).hexdigest() != signature:
        raise ValueError("Nieprawidłowy podpis!")
    return pickle.loads(pkl_data)


data = {"imie": 'Tomek'}
signature = create_sig_pickle(data)

try:
    loaded_data = load_sig_pickle('dane.pickle', signature)
    print(loaded_data)
except ValueError as e:
    print(e)
