import os, sys

class Backend_Configuration:
    b_host        = '127.0.0.1'
    b_port        = 8000
    b_debug       = True
    b_reloader    = True

    BASEDIR       = os.path.abspath(os.path.dirname(__file__))
    LOG_FOLDER    = os.path.join(BASEDIR, 'logs')
    IMAGES_FOLDER = os.path.join(BASEDIR, 'images')
    ORM_FOLDER    = os.path.join(BASEDIR, 'orm_models')