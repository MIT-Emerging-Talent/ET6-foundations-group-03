def get_last_element(lst: list) -> object:
    """
    Returns the last element of a given list.

    This function will return the last item of the list if the list is non-empty.
    If the list is empty, it will return None.

    Parameters:
    lst (list): A list from which the last element is to be returned. The list can contain any type of element.

    Returns:
    object: The last element in the list. Returns None if the list is empty.

    Raises:
    TypeError: If the input is not a list.

    Example:
    >>> get_last_element([1, 2, 3, 4])
    4
    >>> get_last_element(['apple', 'banana', 'cherry'])
    'cherry'
    >>> get_last_element([])
    None
    >>> get_last_element('not a list')
    Traceback (most recent call last):
        ...
    TypeError: Input must be a list
    """
    # Defensive assertion: Ensure input is a list
    if not isinstance(lst, list):
        raise TypeError("Input must be a list")

    return lst[-1] if lst else None
