import os, sys

class Backend_Configuration:
    b_host        = '0.0.0.0'
    b_port        = 8000
    b_debug       = True
    b_reloader    = True

    BASEDIR           = os.path.abspath(os.path.dirname(__file__))
    LOG_FOLDER        = os.path.join(BASEDIR, 'logs')
    IMAGES_FOLDER     = os.path.join(BASEDIR, 'images')
    ORM_FOLDER        = os.path.join(BASEDIR, 'orm_models')
    DB_FOLDER         = os.path.join(BASEDIR, 'db_modules')
    DTO_FOLDER        = os.path.join(BASEDIR, 'objects_dto')
    ENDPOINTS_FOLDER  = os.path.join(BASEDIR, 'endpoints')
    LOGIC_FOLDER      = os.path.join(BASEDIR, 'logic')