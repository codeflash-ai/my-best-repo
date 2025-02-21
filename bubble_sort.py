def parse_version(version: str) -> str:
    """Parse and convert version specifiers."""
    if version.startswith("^"):
        split_versions = version[1:].split(",")
        main_lib_version = split_versions[0]
        addtional_lib_version = split_versions[1] if len(split_versions) > 1 else None

        return f">={main_lib_version}" + (
            f",{addtional_lib_version}" if addtional_lib_version else ""
        )
