import glob
import os
import uuid

from src.dto.scan_result import ScanResult
from fosslight_scanner.fosslight_scanner import run_main


class FosslightScanner:

    # input: project path
    def scan_all(self, path: str) -> ScanResult:
        uid = uuid.uuid4()
        output_path = os.path.expanduser(f'~/.fosslightcli/temp/scan/{uid}')
        run_main(
            mode='all',
            path_arg=[path],
            dep_arguments='',
            output_file_or_dir=output_path,
            file_format='',
            url_to_analyze='',
            db_url='',
        )
        glob.glob(f"{output_path}/*")
        return ScanResult()
