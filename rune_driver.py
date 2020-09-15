"""
https://github.com/calvin-mcdowell/rune-driver
"""
from lcu_client.lcu_client import LcuClient

def main():
    """
    rune_driver.main() is just being used for class method verification until a main program loop is established
    """
    client = LcuClient()
    runes = client.get_rune_pages()

    for rune in runes:
        print(f'{rune}\n')

if __name__ == '__main__':
    main()