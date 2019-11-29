import logging
import sys

# 創建日誌的實例
logger = logging.getLogger("testLogger")

#定制Logger的輸出格市
formatter = logging.Formatter("%(asctime)s %(levelname)s %(message)s")

# 創建日誌:文件日誌
file_handler = logging.FileHandler('testLogger.log')
file_handler.setFormatter(formatter)

 #創建日誌:終端機的日誌
consle_handler = logging.StreamHandler(sys.stdout)
consle_handler.setFormatter(formatter)

#設置默認的日誌級別
logger.setLevel(logging.INFO)

#把文件日誌和終端機日誌添加到日誌處理器中
logger.addHandler(file_handler)
logger.addHandler(consle_handler)

logger.critical("Test Critical log")
logger.error("Test Error log")
logger.warning("Test Warning log")
logger.info("Test Info log")
logger.debug("Test Debug log")

#不再使用這日誌時要remove
logger.removeHandler(file_handler)
logger.removeHandler(consle_handler)
