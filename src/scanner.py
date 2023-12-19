import glob
import os
import uuid

from src.dto.scan_result import ScanResult


class FosslightScanner:

    # input: project path
    @classmethod
    def scan_all(cls, path: str) -> ScanResult:
        from fosslight_scanner.fosslight_scanner import run_main
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
        result = ScanResult()
        if bin_files := glob.glob(f"{output_path}/fosslight_binary_bin_*.txt"):
            result.binary_file_path = bin_files[0]

        if report_files := glob.glob(f"{output_path}/fosslight_report_all_*.xlsx"):
            result.report_file_path = report_files[0]
        return result
