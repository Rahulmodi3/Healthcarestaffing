import logging
from pathlib import Path

class LogGen:

    @staticmethod
    def loggen():
        logger = logging.getLogger()
        current_dir = Path(__file__)
        project_name = 'EmPower(hshceu)'
        root_dir = next(p for p in current_dir.parents if p.parts[-1] == project_name)
        log_path = str(root_dir) + "\\logs\\automation.log"

        log_file = logging.FileHandler(filename=log_path, mode='a')
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        log_file.setFormatter(formatter)
        logger.addHandler(log_file)
        logger.setLevel(logging.INFO)
        return logger