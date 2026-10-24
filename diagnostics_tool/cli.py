import platform
import shutil
import json
import os
import sys


def main():
    try:
        disk = shutil.disk_usage(os.getcwd())
        
        developer_tools = {}

        for tool in ["python", "git"]:
            developer_tools[tool] = shutil.which(tool)

        report = {
            "system": platform.system(),
            "python_version": platform.python_version(),
            "machine": platform.machine(),
            "disk_total_gb": round(disk.total / (1024 ** 3), 2),
            "disk_free_gb": round(disk.free / (1024 ** 3), 2),
            "current_directory": os.getcwd(),
            "python_executable": sys.executable,
            "environment_variables_count": len(os.environ),
            "developer_tools": developer_tools,
        }

        print("=== SYSTEM DIAGNOSTICS REPORT ===")
        print(json.dumps(report, indent=4))

        with open("diagnostics_report.json", "w", encoding="utf-8") as file:
            json.dump(report, file, indent=4)

        print("\nReport saved as diagnostics_report.json")

        with open("diagnostics_report.txt", "w", encoding="utf-8") as file:
            file.write("SYSTEM DIAGNOSTICS REPORT\n")
            file.write("=========================\n")
            for key, value in report.items():
                file.write(f"{key}: {value}\n")

        print("Text report saved as diagnostics_report.txt")
        return 0

    except OSError as error:
        print(f"Diagnostics failed: {error}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    sys.exit(main())
