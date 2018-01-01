
"""
The rider module contains the Rider class. It also contains
constants that represent the status of the rider.

=== Constants ===
@type WAITING: str
    A constant used for the waiting rider status.
@type CANCELLED: str
    A constant used for the cancelled rider status.
@type SATISFIED: str
    A constant used for the satisfied rider status
"""

WAITING = "waiting"
CANCELLED = "cancelled"
SATISFIED = "satisfied"


class Rider:

    def __init__(self, identifier, origin, destination, patience):
        """Initialize a Rider.

        @type self: Rider
        @type identifier: str
        @type origin: Location
        @type destination: Location
        @type patience: int
        @rtype: None
        """

        self.id = identifier
        self.origin = origin
        self.destination = destination
        self.patience = patience
        self.status = WAITING

    def __str__(self):
        """Return a string representation.

        @type self: Rider
        @rtype: str
        """

        return self.id

    def __eq__(self, other):
        """Return True if self equals other, and false otherwise.

        @type self: Rider
        @rtype: bool
        """

        return self.id == other.id
