import tarfile, subprocess

class BackupTool:
    def __init__(self, src, backend="s3"): self.src, self.backend = src, backend
    def create(self, name):
        path = f"/tmp/{name}.tar.gz"
        with tarfile.open(path, "w:gz") as t: t.add(self.src, arcname=name)
        return path
    def encrypt(self, path, key):
        enc = f"{path}.enc"
        subprocess.run(["gpg", "--symmetric", "--cipher-algo", "AES256", "--passphrase", key, "-o", enc, path])
        return enc
