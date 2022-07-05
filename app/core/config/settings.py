from os.path import abspath, join, dirname


class Settings:

    ROOT_PATH = dirname(dirname(dirname(abspath(__file__))))
