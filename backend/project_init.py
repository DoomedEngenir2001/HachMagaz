from sys import path
#-------------------------------------------------------------#
from side_methods import add_folderToSysPath, create_folderIfNotExists
from backend_configuration import Backend_Configuration
#-------------------------------------------------------------#

def init(debug: bool = False):
    create_folderIfNotExists(Backend_Configuration.LOG_FOLDER)
    create_folderIfNotExists(Backend_Configuration.IMAGES_FOLDER)
    add_folderToSysPath(Backend_Configuration.ENDPOINTS_FOLDER)
    add_folderToSysPath(Backend_Configuration.DB_FOLDER)
    add_folderToSysPath(Backend_Configuration.DTO_FOLDER)
    add_folderToSysPath(Backend_Configuration.ORM_FOLDER)
    add_folderToSysPath(Backend_Configuration.LOGIC_FOLDER)

    if debug: 
        print( "Папки и пути успешно инициализированы.")
        print( f"Текущий sys.:path: {path}")