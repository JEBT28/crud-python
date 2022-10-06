import logging as log

log.basicConfig(level=log.DEBUG,
                format="%(asctime)s: %(levelname)s: [%(filename)s]: %(lineno)s",
                datefmt="%I:%M:%s %p",
                handlers=[log.FileHandler('log.log'),log.StreamHandler()]
                )


if __name__ == '__main__':
    log.debug('Mensaje debug')