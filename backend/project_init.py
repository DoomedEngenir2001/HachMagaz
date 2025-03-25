#-------------------------------------------------------------#
from side_methods import add_folderToSysPath, create_folderIfNotExists
from backend_configuration import Backend_Configuration
#-------------------------------------------------------------#

def init():
    create_folderIfNotExists(Backend_Configuration.LOG_FOLDER)
    create_folderIfNotExists(Backend_Configuration.IMAGES_FOLDER)
    add_folderToSysPath(Backend_Configuration.ORM_FOLDER)