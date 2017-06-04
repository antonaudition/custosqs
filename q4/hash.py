import bcrypt
import hashlib


def hash_bcrypt(to_hash, rounds):
    return bcrypt.hashpw(to_hash, bcrypt.gensalt(int(rounds)))


def hash_md5sum(to_hash):
    m = hashlib.md5()
    m.update(to_hash)
    return m.hexdigest()


class Bcrypter:
    def __init__(self, db):
        self.db = db

    def hash(self, to_hash, rounds):
        md5_sum = hash_md5sum(to_hash)
        pre_calc = self.db.lookup(md5_sum, rounds)
        if pre_calc is not None:
            return pre_calc
        calc = hash_bcrypt(to_hash, rounds)
        self.db.insert(md5_sum, rounds, calc)
        return calc

    def close(self):
        self.db.close()
