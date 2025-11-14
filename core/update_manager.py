"""Bulk Update Manager - Check and update packages"""

import subprocess
import sys
from typing import List, Dict, Tuple


class UpdateManager:
    """Manages package updates"""

    def __init__(self, python_executable=None):
        self.python_executable = python_executable or sys.executable

    def check_outdated_packages(self) -> Tuple[bool, List[Dict]]:
        """
        Check for outdated packages

        Returns:
            tuple: (success: bool, packages: List[Dict])
        """
        try:
            result = subprocess.run(
                [self.python_executable, '-m', 'pip', 'list', '--outdated', '--format', 'json'],
                capture_output=True,
                text=True,
                timeout=60
            )

            if result.returncode == 0:
                import json
                packages = json.loads(result.stdout)
                return True, packages
            else:
                return False, []

        except Exception as e:
            return False, []

    def update_package(self, package_name: str) -> Tuple[bool, str]:
        """
        Update a single package

        Args:
            package_name: Name of the package to update

        Returns:
            tuple: (success: bool, message: str)
        """
        try:
            result = subprocess.run(
                [self.python_executable, '-m', 'pip', 'install', '--upgrade', package_name],
                capture_output=True,
                text=True,
                timeout=300
            )

            if result.returncode == 0:
                return True, f"Successfully updated {package_name}"
            else:
                return False, result.stderr or result.stdout

        except subprocess.TimeoutExpired:
            return False, f"Update timeout for {package_name}"
        except Exception as e:
            return False, str(e)

    def update_multiple_packages(self, package_names: List[str]) -> List[Dict]:
        """
        Update multiple packages

        Args:
            package_names: List of package names to update

        Returns:
            list: Results for each package
        """
        results = []

        for package_name in package_names:
            success, message = self.update_package(package_name)
            results.append({
                'package': package_name,
                'success': success,
                'message': message
            })

        return results

    def update_all_outdated(self) -> Tuple[bool, str]:
        """
        Update all outdated packages at once

        Returns:
            tuple: (success: bool, message: str)
        """
        try:
            # Get list of outdated packages
            success, outdated = self.check_outdated_packages()

            if not success or not outdated:
                return True, "No packages to update"

            package_names = [pkg['name'] for pkg in outdated]

            # Update all at once
            result = subprocess.run(
                [self.python_executable, '-m', 'pip', 'install', '--upgrade'] + package_names,
                capture_output=True,
                text=True,
                timeout=600
            )

            if result.returncode == 0:
                return True, f"Successfully updated {len(package_names)} packages"
            else:
                return False, result.stderr or result.stdout

        except subprocess.TimeoutExpired:
            return False, "Update timeout"
        except Exception as e:
            return False, str(e)

    def get_package_latest_version(self, package_name: str) -> str:
        """
        Get latest version of a package from PyPI

        Args:
            package_name: Name of the package

        Returns:
            str: Latest version or 'Unknown'
        """
        try:
            result = subprocess.run(
                [self.python_executable, '-m', 'pip', 'index', 'versions', package_name],
                capture_output=True,
                text=True,
                timeout=10
            )

            if result.returncode == 0:
                # Parse output to get latest version
                lines = result.stdout.split('\n')
                for line in lines:
                    if 'Available versions:' in line or 'LATEST:' in line:
                        # Extract first version
                        import re
                        versions = re.findall(r'\d+\.\d+\.\d+', line)
                        if versions:
                            return versions[0]

            return 'Unknown'

        except Exception:
            return 'Unknown'
