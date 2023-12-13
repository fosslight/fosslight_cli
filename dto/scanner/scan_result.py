from dataclasses import dataclass


@dataclass
class ScanResult:
    lint_file_path: str
    binary_file_path: str
    report_file_path: str

    raw_src_file_path: str
    raw_dep_file_path: str
    raw_bin_file_path: str
