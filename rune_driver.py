"""
https://github.com/calvin-mcdowell/rune-driver
"""
from lcu_client.lcu_client import LcuClient

def main():
    client = LcuClient()
    client.download_root_certificate()

if __name__ == '__main__':
    main()