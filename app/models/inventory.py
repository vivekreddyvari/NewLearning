""" Inventory models """

from OOP.Project3.app.utils.validators import validate_integer


class Resource:
    """ Base class for resources """

    def __init__(self, name, manufacturer, total, allocated):
        """

        Args:
            name: (str) display name of resource
            manufacturer: (str) resource manufacturer
            total: (int) current total amount of resources
            allocated:(int) current count of in-use resources

        Note:
            `allocated` cannot exceed `total`
        """
        self._name = name
        self._manufacturer = manufacturer

        validate_integer('total', total, min_value=0)
        self._total = total

        validate_integer(
            'allocated', allocated, 0, total,
            custom_max_message='Allocated inventory cannot exceed total inventory'
                         )
        self._allocated = allocated

    @property
    def name(self):
        """

            Args:
               self: The resource name
        """
        return self._name

    @property
    def manufacturer(self):
        """

            Args:
            self: The manufacturer
        """
        return self._manufacturer

    @property
    def total(self):
        """

        Args:
        self: The total resources


        """
        return self._total

    @property
    def allocated(self):
        """

            Args:
                self: The allocated quantity

        Returns:

        """
        return self._allocated

    @property
    def category(self):
        """

            Args:
                self: The resource category

            Returns:

        """
        return type(self).__name__.lower()

    @property
    def available(self):
        """

            Args:
                int: number of resources available for use
        """
        return self.total - self.allocated

    def __str__(self):
        return self.name

    def __repr__(self):
        return (f'{self.name} ({self.category} - {self.manufacturer}): '
                f'total={self.total}, allocated={self.allocated}'
                )

    def claim(self, num):
        """

            Args:
                self:
                num (int) : Number of inventory items to claim

        Returns:

        """
        validate_integer(
            'num', num, 1, self.available,
            custom_max_message='cannot claim more than available'
            )
        self._allocated += num

    def freeup(self, num):
        """

        Args:
                self:
                num (int) : Number of items to return (cannot exceed number in use)

        Returns:

        """
        validate_integer(
            'num', num, 1, self.allocated,
            custom_max_message='You cannot return more than allocated'
        )
        self._allocated -= num

    def died(self, num):
        """

        Args:
                self:
                num (int): Number of items that are died / destroyed

        """
        validate_integer('num', num, 1, self.allocated,
                         custom_max_message='Cannot retire more than allocated')
        self._total -= num
        self._allocated -= num

    def purchased(self, num):
        """

        Args:
                self:
                num (int) : Number of items to add to the pool
        """
        validate_integer('num', num, 1)
        self._total += num


class CPU(Resource):
    """ Resource subclass used to track specific CPU inventory pools """

    def __init__(
            self, name, manufacturer, total, allocated, cores, socket, power_watts
    ):
        """

        Args:
            name:
            manufacturer:
            total:
            allocated:
            cores:
            socket:
            power_watts:
        """
        super().__init__(name, manufacturer, total, allocated)

        validate_integer('cores', cores, 1)
        validate_integer('power_watts', power_watts, 1)

        self._cores = cores
        self._socket = socket
        self._power_watts = power_watts

    @property
    def cores(self):
        """
        The number cores for a CPU
        Returns:
            int
        """
        return self._cores

    @property
    def socket(self):
        """
        The socket type of the CPU
        Returns:
            str
        """
        return self._socket

    @property
    def power_watts(self):
        """
        The power of the CPU in watts (rated in wattage)
        Returns:
            int
        """
        return self._power_watts

    def __repr__(self):
        return f'{self.category}: {self.name} ({self.socket} -x{self.cores})'


class Storage(Resource):
    """
    A base class for storage devices - probably not used directly
    """

    def __init__(self, name, manufacturer, total, allocated, capacity_gb):
        """

        Args:
            name: (str) display name of resource
            manufacturer: (str) resource manufacturer
            total: (int) current total amount of resources
            allocated:(int) current count of in-use resources
            capacity_gb: (int) storage capacity (in GB)
        """
        super().__init__(name, manufacturer, total, allocated)
        validate_integer('capacity_gb', capacity_gb, 1)
        self._capacity_gb = capacity_gb

    @property
    def capacity_gb(self):
        """
        Indicates the memory in Gigabytes of the storage device
        Returns:
            int
        """
        return self._capacity_gb

    def __repr__(self):
        return f"{self.category}: {self.capacity_gb} GB"


class HDD(Storage):
    """
    Class used for HDD Type resources
    """
    def __init__(
            self,name, manufacturer, total, allocated, capacity_gb, size, rpm
    ):
        """

        Args:
           name (str): display name of resource
            manufacturer (str): resource manufacturer
            total (int): current total amount of resources
            allocated (int): current count of in-use resources
            capacity_gb (int): storage capacity (in GB)
            size (str): indicates the device size (must be either 2.5" or 3.5")
            rpm (int): disk rotation speed (in rpm)
        """
        super().__init__(name, manufacturer, total, allocated, capacity_gb)

        allowed_sizes = ['2.5"', '3.5"']
        if size not in allowed_sizes:
            raise ValueError(f'Invalid HDD Size.'
                             f'Must be one of {",".join(allowed_sizes)}')
        validate_integer('rpm', rpm, min_value=1_000, max_value=50_000)
        self._size = size
        self._rpm = rpm

    @property
    def size(self):
        """
        THe HDD size (2.5"/3.5")
        Returns:
            str

        """
        return self._size

    @property
    def rpm(self):
        """
        HDD Spin speed (RPM)
        Returns:
            int
        """
        return self._rpm

    def __repr__(self):
        s = super().__repr__()
        return f"{s} ({self.size}, {self.rpm} rpm)"


class SSD(Storage):
    """
    Class used for SSD type resources
    """
    def __init__(
            self, name, manufacturer, total, allocated, capacity_gb,
            interface
    ):
        """

        Args:
            name (str): display name of resource
            manufacturer (str): resource manufacturer
            total (int): current total amount of resources
            allocated (int): current count of in-use resources
            capacity_gb (int): storage capacity (in GB)
            interface (str): indicates the device interface (e.g. PCIe NVMe 3.0 x4)
        """
        super().__init__(name, manufacturer, total, allocated, capacity_gb)

        self._interface = interface

    @property
    def interface(self):
        """
        Interface used by SSD (e.g. PCIe NVMe 3.0 x4)

        Returns:
            str
        """
        return self._interface

    def __repr__(self):
        s = super().__repr__()
        return f'{s} ({self.interface})'
