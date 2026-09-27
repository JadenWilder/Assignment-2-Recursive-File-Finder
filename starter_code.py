"""
Recursion Assignment Starter Code
Complete the recursive functions below to analyze the compromised file system.
"""

import os

# ============================================================================
# PART 1: RECURSION WARM-UPS
# ============================================================================

def sum_list(numbers):
    """
    Recursively calculate the sum of a list of numbers.
    """
    if len(numbers) == 0:
        return 0

    return numbers[0] + sum_list(numbers[1:])


print("\nTest sum_list:")
print(f"  sum_list([1, 2, 3, 4]) = {sum_list([1, 2, 3, 4])} (expected: 10)")
print(f"  sum_list([]) = {sum_list([])} (expected: 0)")
print(f"  sum_list([5, 5, 5]) = {sum_list([5, 5, 5])} (expected: 15)")


def count_even(numbers):
    """
    Recursively count how many even numbers are in a list.
    """
    if len(numbers) == 0:
        return 0

    if numbers[0] % 2 == 0:
        return 1 + count_even(numbers[1:])

    return count_even(numbers[1:])


print("\nTest count_even:")
print(f"  count_even([1, 2, 3, 4, 5, 6]) = {count_even([1, 2, 3, 4, 5, 6])} (expected: 3)")
print(f"  count_even([1, 3, 5]) = {count_even([1, 3, 5])} (expected: 0)")
print(f"  count_even([2, 4, 6]) = {count_even([2, 4, 6])} (expected: 3)")


def find_strings_with(strings, target):
    """
    Recursively find all strings that contain a target substring.
    """
    if len(strings) == 0:
        return []

    results = find_strings_with(strings[1:], target)

    if target in strings[0]:
        return [strings[0]] + results

    return results


print("\nTest find_strings_with:")

result = find_strings_with(
    ["hello", "world", "help", "test"],
    "hel"
)

print(
    f"  find_strings_with(['hello', 'world', 'help', 'test'], 'hel') = {result}"
)

print("  (expected: ['hello', 'help'])")

result = find_strings_with(
    ["cat", "dog", "bird"],
    "z"
)

print(
    f"  find_strings_with(['cat', 'dog', 'bird'], 'z') = {result}"
)

print("  (expected: [])")


# ============================================================================
# PART 2: COUNT ALL FILES
# ============================================================================

def count_files(directory_path):
    """
    Recursively count all files in a directory and its subdirectories.
    """

    # Base case: if the path is a file, count it as 1
    if os.path.isfile(directory_path):
        return 1

    total = 0

    # Look at everything inside the directory
    for item in os.listdir(directory_path):

        # Create the complete path
        full_path = os.path.join(directory_path, item)

        # If it is a file, add 1
        if os.path.isfile(full_path):
            total += 1

        # If it is a directory, recursively count its files
        elif os.path.isdir(full_path):
            total += count_files(full_path)

    return total


# ============================================================================
# PART 3: FIND INFECTED FILES
# ============================================================================

def find_infected_files(directory_path, extension=".encrypted"):
    """
    Recursively find all files with a specific extension in a directory tree.
    """

    # Base case: if this is a file, check its extension
    if os.path.isfile(directory_path):

        if directory_path.endswith(extension):
            return [directory_path]

        return []

    infected_files = []

    # Look at everything inside the directory
    for item in os.listdir(directory_path):

        # Create the complete path
        full_path = os.path.join(directory_path, item)

        # If it is a file, check whether it is infected
        if os.path.isfile(full_path):

            if full_path.endswith(extension):
                infected_files.append(full_path)

        # If it is a directory, recursively search it
        elif os.path.isdir(full_path):

            infected_files.extend(
                find_infected_files(full_path, extension)
            )

    return infected_files


# ============================================================================
# TESTING & BENCHMARKING
# ============================================================================

if __name__ == "__main__":

    print("\n" + "=" * 60)
    print("RECURSION ASSIGNMENT - TESTING")
    print("=" * 60)

    # ------------------------------------------------------------------------
    # 1. Test count_files function
    # ------------------------------------------------------------------------

    print("\nCOUNT FILES TESTS:")

    print(
        "Total files (Test Case 1):",
        count_files("test_cases/case1_flat")
    )

    print(
        "Total files (Test Case 2):",
        count_files("test_cases/case2_nested")
    )

    print(
        "Total files (Test Case 3):",
        count_files("test_cases/case3_infected")
    )

    # ------------------------------------------------------------------------
    # 2. Count files in the breached file system
    # ------------------------------------------------------------------------

    print("\nBREACH FILE SYSTEM:")

    total_breach_files = count_files("breach_data")

    print(
        "Total files (breached files):",
        total_breach_files
    )

    # ------------------------------------------------------------------------
    # 3. Test find_infected_files function
    # ------------------------------------------------------------------------

    print("\nINFECTED FILE TESTS:")

    infected_case1 = find_infected_files(
        "test_cases/case1_flat"
    )

    print(
        "Total Infected Files (Test Case 1):",
        len(infected_case1)
    )

    infected_case2 = find_infected_files(
        "test_cases/case2_nested"
    )

    print(
        "Total Infected Files (Test Case 2):",
        len(infected_case2)
    )

    infected_case3 = find_infected_files(
        "test_cases/case3_infected"
    )

    print(
        "Total Infected Files (Test Case 3):",
        len(infected_case3)
    )

    # ------------------------------------------------------------------------
    # 4. Find infected files in the breached file system
    # ------------------------------------------------------------------------

    print("\nBREACH INFECTED FILES:")

    infected_breach = find_infected_files(
        "breach_data"
    )

    print(
        "Total Infected Files (breached files):",
        len(infected_breach)
    )

    # ------------------------------------------------------------------------
    # 5. Determine infected files by department
    # ------------------------------------------------------------------------

    print("\nINFECTED FILES BY DEPARTMENT:")

    hr_infected = find_infected_files(
        "breach_data/HR"
    )

    operations_infected = find_infected_files(
        "breach_data/Operations"
    )

    print(
        "HR infected files:",
        len(hr_infected)
    )

    print(
        "Operations infected files:",
        len(operations_infected)
    )

    print("\n" + "=" * 60)
    print("TESTING COMPLETE")
    print("=" * 60)