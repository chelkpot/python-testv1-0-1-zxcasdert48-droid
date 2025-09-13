import sys
import xml.etree.ElementTree as ET

def calculate_score(file_path):
    try:
        tree = ET.parse(file_path)
        root = tree.getroot()

        total_tests = int(root.get('tests', 0))
        failures = int(root.get('failures', 0))
        errors = int(root.get('errors', 0))
        
        passed_tests = total_tests - failures - errors
        
        print(f"Final Grade: {passed_tests}/{total_tests}")

    except Exception as e:
        print(f"Error calculating score: {e}")
        sys.exit(1)

if __name__ == "__main__":
    if len(sys.argv) > 1:
        calculate_score(sys.argv[1])
    else:
        print("Usage: python score.py <path_to_junit_xml>")
        sys.exit(1)