from dataclasses import dataclass


@dataclass
class ScanResult:
    binary_file_path: str
    report_file_path: str
    lint_file_path: str

    raw_src_file_path: str
    raw_dep_file_path: str
    raw_bin_file_path: str
    raw_lint_file_path: str
