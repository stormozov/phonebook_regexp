import os

from ..validators.fs_validate import validate_path_segments


def get_absolute_path(path_segments: list[str]) -> str:
    """Returns an absolute path from a list of path segments.

    Args:
        path_segments: A list of path segments.

    Returns:
        An absolute path.

    Raises:
        ValueError: If path_segments is not a list.
        ValueError: If path_segments is an empty list.
        TypeError: If path_segments contains non-string elements.
    """
    validate_path_segments(path_segments)
    file_path = os.path.join(*path_segments)

    return os.path.abspath(file_path)
