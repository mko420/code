#constants.py
import os

USER        = 'michael.castaing'
USER_LOGIN8 = 'mcastain'
REPO_SDEV   = f'/home/{USER_LOGIN8}/wd/run-tools/{USER_LOGIN8}/python3/files'
ALL_ZONES   = ['rbx2a', 'rbx2b', 'rbx2d', 'sbg1a', 'lim1c', 'eri1c', 'waw1c']


ENV_FILE_PATH   = f'/home/{USER_LOGIN8}/wd/bootstrapdev/docker/.env'
DEV3_FILE_PATH  = f'/home/{USER_LOGIN8}/wd/bootstrapdev/docker/generated/secure_datas/mozg/rbx2a/secure_data.dev3'

#MySQL Private configuration
#load env files
from dotenv import load_dotenv
load_dotenv(ENV_FILE_PATH)

INFORMATIONS_PRIVATEDB = {    
    "username"      : os.getenv("MYSQL_USER"),
    "password"      : os.getenv("MYSQL_PASSWORD"),
    "ip_address"    : "localhost",
    "zone"          : "privateDb",
    "port"          : os.getenv("FR_MYSQL_PORT"),
    "database_name" : "privateCloud",
    "root_password" : os.getenv("MYSQL_ROOT_PASSWORD"),
    }

FR_MYSQL_PORT               =   os.getenv("FR_MYSQL_PORT")
CA_MYSQL_PORT               =   os.getenv("CA_MYSQL_PORT")
US_MYSQL_PORT               =   os.getenv("US_MYSQL_PORT")
SNC_MYSQL_PORT              =   os.getenv("SNC_MYSQL_PORT")