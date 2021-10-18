from datetime import datetime, timedelta, timezone
from enum     import IntEnum
from typing   import Optional
from rmt      import SlottedClass

class Side(IntEnum):
    """Trade side or direction."""

    BUY   = 1
    SELL  = -1

    def __mul__(self, x: float) -> float:
        return self.value * x

    def __rmul__(self, x: float) -> float:
        return x * self.value

class OrderType(IntEnum):
    """Identifies the type of an order."""

    MARKET_ORDER = 0
    LIMIT_ORDER  = 1
    STOP_ORDER   = 2

class OrderStatus(IntEnum):
    """Identifies the status of an order."""

    PENDING          = 0
    CANCELED         = 1
    EXPIRED          = 2
    PARTIALLY_FILLED = 3
    FILLED           = 4
    CLOSED           = 5

class Order(SlottedClass):
    """Stores information about an order."""

    __slots__ = [
        '_symbol',
        '_side',
        '_type',
        '_lots',
        '_status',
        '_open_price',
        '_open_time',
        '_close_price',
        '_close_time',
        '_stop_loss',
        '_take_profit',
        '_expiration',
        '_magic_number',
        '_comment',
        '_commission',
        '_profit',
        '_swap'
    ]

    def __init__(self,
                 symbol:       str,
                 side:         Side,
                 type:         OrderType,
                 lots:         float,
                 status:       OrderStatus,
                 open_price:   float,
                 open_time:    datetime,
                 close_price:  Optional[float]    = None,
                 close_time:   Optional[datetime] = None,
                 stop_loss:    Optional[float]    = None,
                 take_profit:  Optional[float]    = None,
                 expiration:   Optional[datetime] = None,
                 magic_number: int = 0,
                 comment:      str = '',
                 commission:   float = 0.0,
                 profit:       float = 0.0,
                 swap:         float = 0.0
    ):
        self._symbol       = symbol
        self._side         = side
        self._type         = type
        self._lots         = lots
        self._status       = status
        self._open_price   = open_price
        self._open_time    = open_time
        self._close_price  = close_price
        self._close_time   = close_time
        self._stop_loss    = stop_loss
        self._take_profit  = take_profit
        self._expiration   = expiration
        self._magic_number = magic_number
        self._comment      = comment
        self._commission   = commission
        self._profit       = profit
        self._swap         = swap

    def symbol(self) -> str:
        return self._symbol

    def side(self) -> Side:
        return self._side

    def type(self) -> OrderType:
        return self._type
    
    def lots(self) -> float:
        return self._lots

    def status(self) -> OrderStatus:
        return self._status

    def open_price(self) -> float:
        return self._open_price

    def open_time(self) -> datetime:
        return self._open_time

    def close_price(self) -> Optional[float]:
        return self._close_price

    def close_time(self) -> Optional[datetime]:
        return self._close_time

    def stop_loss(self) -> Optional[float]:
        return self._stop_loss

    def take_profit(self) -> Optional[float]:
        return self._take_profit

    def expiration(self) -> Optional[datetime]:
        return self._expiration

    def magic_number(self) -> int:
        return self._magic_number

    def comment(self) -> str:
        return self._comment

    def commission(self) -> float:
        return self._commission

    def profit(self) -> float:
        return self._profit

    def swap(self) -> float:
        return self._swap

    def is_buy(self) -> bool:
        return self._side == Side.BUY

    def is_sell(self) -> bool:
        return self._side == Side.SELL

    def duration(self) -> timedelta:
        if self.close_time() > self.open_time():
            return self.close_time() - self.open_time()
        else:
            return datetime.now(timezone.utc) - self.open_time()