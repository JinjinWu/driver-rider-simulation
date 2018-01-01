
from driver import Driver
from rider import Rider
from location import manhattan_distance


class Dispatcher:
    """A dispatcher fulfills requests from riders and drivers for a
    ride-sharing service.

    When a rider requests a driver, the dispatcher assigns a driver to the
    rider. If no driver is available, the rider is placed on a waiting
    list for the next available driver. A rider that has not yet been
    picked up by a driver may cancel their request.

    When a driver requests a rider, the dispatcher assigns a rider from
    the waiting list to the driver. If there is no rider on the waiting list
    the dispatcher does nothing. Once a driver requests a rider, the driver
    is registered with the dispatcher, and will be used to fulfill future
    rider requests.
    """

    def __init__(self):
        """Initialize a Dispatcher.

        @type self: Dispatcher
        @rtype: None
        """

        self.id = "dispatcher"
        self.driver_fleet = []
        self.rider_queue = []

    def __str__(self):
        """Return a string representation.

        @type self: Dispatcher
        @rtype: str
        """

        return self.id

    def request_driver(self, rider):
        """Return a driver for the rider, or None if no driver is available.

        Add the rider to the waiting list if there is no available driver.

        @type self: Dispatcher
        @type rider: Rider
        @rtype: Driver | None
        """

        # set variable of closest driver to None
        closest = None
        # iterate through fleet of drivers
        for driver in self.driver_fleet:
            # check if driver is available
            if driver.is_idle:
                if closest is None:
                    # assign first available driver as closest
                    closest = driver
                else:
                    # compare Manhattan distances of current closest driver, and next available driver
                    if manhattan_distance(closest.location, rider.origin) > manhattan_distance(driver.location, rider.origin):
                        # if next available driver is closer, assign new closest as this driver
                        closest = driver

        # add rider to waiting list if there's no available driver
        if closest is None:
            self.rider_queue.append(rider)

        return closest

    def request_rider(self, driver):
        """Return a rider for the driver, or None if no rider is available.

        If this is a new driver, register the driver for future rider requests.

        @type self: Dispatcher
        @type driver: Driver
        @rtype: Rider | None
        """

        if driver not in self.driver_fleet:
            self.driver_fleet.append(driver)

        if len(self.rider_queue) != 0:
            return self.rider_queue[0]

    def cancel_ride(self, rider):
        """Cancel the ride for rider.

        @type self: Dispatcher
        @type rider: Rider
        @rtype: None
        """

        if rider in self.rider_queue:
            self.rider_queue.remove(rider)
