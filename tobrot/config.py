from tobrot.sample_config import Config

#Fill your all data, read readme for reference

#FOR CUSTOM COMMANDS READ REAME AND FILL THEM...

class Config(Config):
    TG_BOT_TOKEN= "1769893770:AAEIvnjKmjwArTZZMJ2TjUek0Fd7_jaoff0"
    APP_ID = 2105857
    API_HASH = "c8aacc9417551dc98e2b2f61fbfb8387"
    OWNER_ID = 1640567687
    AUTH_CHANNEL = [-1001463255443,-1001463600621,1149703834,1323460577,1640567687]
    UPLOAD_AS_DOC = "False"
    LEECH_COMMAND = "leech"
    GLEECH_COMMAND = "gleech" 
    YTDL_COMMAND = "ytdl"
    PYTDL_COMMAND = "pytdl@CerminStreamRobot"
    INDEX_LINK = ""
    TELEGRAM_LEECH_COMMAND_G = "tleech@CerminStreamRobot"
    GET_SIZE_G = "getsize@CerminStreamRobot"
    LOG_COMMAND = "log@CerminStreamRobot"
    RENEWME_COMMAND = "renewme"
    CLONE_COMMAND_G = "gclone@CerminStreamRobot"
    STATUS_COMMAND = "s"
    SAVE_THUMBNAIL = "save@CerminStreamRobot"
    CLEAR_THUMBNAIL = "clearthumbnail@CerminStreamRobot"
    DESTINATION_FOLDER = "Leech" #Name of your folder read readme(not id of the folder)
    #Just don't fill RCLONE_CONFIG vars, insted copy your rclone.conf file in root directory
    #if your wanted to fill -- fill your rclone config like this(Your config may have some extra value or less. so Don't worry)
    RCLONE_CONFIG = """
[TEAM]
type = drive
scope = drive
token = {"access_token":"ya29.a0AfH6SMCJs9VkPcbj_kD-Yzio0ayv2ZMIrjgnVccyyZnyaH-hcTSCCNU51Kgrnqyy3j3CXb2c3Af1ePS_Wt2_Tw2i2gfs31lmnYRA0H8WAa09nIHR_QhHnCN_bH6v_MxZL3yvJl2wcnJL1g-ZFKyteHv78Fpg","token_type":"Bearer","refresh_token":"1//0g86Tbq5gTv3kCgYIARAAGBASNwF-L9IrOS0rHCI3rI5ZhS4hBfq8xqq0Oqn7Rd7uraGZA0aYLuP3BFRGq3du9jUlKKJ2xYw9KVo","expiry":"2021-03-07T22:51:51.479491053Z"}
team_drive = 0AGXuqNLwr3ISUk9PVA
"""

