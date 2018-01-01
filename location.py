
class Location:
    def __init__(self, row, column):
        """Initialize a location.

        @type self: Location
        @type row: int
        @type column: int
        @rtype: None

        >>> a = Location(5, 10)
        >>> a.row
        5
        >>> a.column
        10
        """

        self.row = row
        self.column = column

    def __str__(self):
        """Return a string representation.

        @rtype: str

        >>> a = Location(1, 2)
        >>> print(a)
        1,2
        """

        return "{},{}".format(self.row, self.column)

    def __eq__(self, other):
        """Return True if self equals other, and false otherwise.

        @rtype: bool

        >>> a = Location(1, 1)
        >>> b = Location(2, 2)
        >>> a == b
        False
        >>> a = Location(1, 2)
        >>> b = Location(1, 2)
        >>> a == b
        True
        """

        return self.row == other.row and self.column == other.column


def manhattan_distance(origin, destination):
    """Return the Manhattan distance between the origin and the destination.

    @type origin: Location
    @type destination: Location
    @rtype: int

    >>> a = Location(1, 1)
    >>> b = Location(3, 3)
    >>> manhattan_distance(a, b)
    4
    """

    return abs(origin.row - destination.row) + abs(origin.column - destination.column)


def deserialize_location(location_str):
    """Deserialize a location.

    @type location_str: str
        A location in the format 'row,col'
    @rtype: Location

    >>> a = deserialize_location("2,3")
    >>> a.row
    2
    >>> a.column
    3
    """

    # split the string into a list of 2 numbers
    coordinates = location_str.split(",")

    # return a Location object with integer arguments
    return Location(int(coordinates[0]), int(coordinates[1]))
