def sorter(arr):
    for i in range(len(arr)):
        for j in range(len(arr) - 1):
            if arr[j] > arr[j + 1]:
                temp = arr[j]
                arr[j] = arr[j + 1]
                arr[j + 1] = temp
    return arr


def parse_version(version: str) -> str:
    """Parse and convert version specifiers."""
    if version.startswith("^"):
        versions = version[1:].split(",")
        main_lib_version = versions[0]
        additional_lib_version = versions[1] if len(versions) > 1 else ""

        return f">={main_lib_version}" + (
            f",{additional_lib_version}" if additional_lib_version else ""
        )
