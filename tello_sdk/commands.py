from typing import Optional, Sequence, Union


class ValidationError(Exception):
    pass


class ValueValidator:
    @staticmethod
    def check_boundries(value: int, minimum: int, maximum: int):
        if not minimum <= value <= maximum:
            raise ValidationError

    @staticmethod
    def check_options(value: Union[str, int], options: Sequence[Union[str, int]]):
        if value not in options:
            raise ValidationError


class TelloSDK:
    COMMAND = "command"
    TAKEOFF = "takeoff"
    LAND = "land"
    STREAMON = "streamon"
    STREAMOFF = "streamoff"
    EMERGENCY = "emergency"
    UP = "up"
    DOWN = "down"
    LEFT = "left"
    RIGHT = "right"
    FORWARD = "forward"
    BACK = "back"
    CW = "cw"
    CCW = "ccw"
    FLIP = "flip"
    GO = "go"
    STOP = "stop"
    CURVE = "curve"
    JUMP = "jump"
    SPEED = "speed"
    RC = "rc"
    WIFI = "wifi"
    MON = "mon"
    MOFF = "moff"
    MDIRECTION = "mdirection"
    AP = "ap"
    GET_SPEED = "speed?"
    GET_BATTERY = "battery?"
    GET_TIME = "time?"
    GET_WIFI = "wifi?"
    GET_SDK = "sdk?"
    GET_SN = "sn?"

    validator = ValueValidator

    def takeoff(self) -> str:
        return self.TAKEOFF

    def land(self) -> str:
        return self.LAND

    def streamon(self) -> str:
        return self.STREAMON

    def streamoff(self) -> str:
        return self.STREAMOFF

    def emergency(self) -> str:
        return self.EMERGENCY

    def up(self, value: int) -> str:
        self.validator.check_boundries(value=value, minimum=20, maximum=500)
        return f"{self.UP} {value}"

    def down(self, value: int) -> str:
        self.validator.check_boundries(value=value, minimum=20, maximum=500)
        return f"{self.DOWN} {value}"

    def left(self, value: int) -> str:
        self.validator.check_boundries(value=value, minimum=20, maximum=500)
        return f"{self.LEFT} {value}"

    def right(self, value: int) -> str:
        self.validator.check_boundries(value=value, minimum=20, maximum=500)
        return f"{self.RIGHT} {value}"

    def forward(self, value: int) -> str:
        self.validator.check_boundries(value=value, minimum=20, maximum=500)
        return f"{self.FORWARD} {value}"

    def back(self, value: int) -> str:
        self.validator.check_boundries(value=value, minimum=20, maximum=500)
        return f"{self.BACK} {value}"

    def cw(self, value: int) -> str:
        self.validator.check_boundries(value=value, minimum=1, maximum=3600)
        return f"{self.CW} {value}"

    def ccw(self, value: int) -> str:
        self.validator.check_boundries(value=value, minimum=1, maximum=3600)
        return f"{self.CCW} {value}"

    def flip(self, value: str) -> str:
        options: Sequence[str] = ["l", "r", "f", "b"]
        self.validator.check_options(value=value, options=options)
        return f"{self.FLIP} {value}"

    def go(self, x: int, y: int, z: int, speed: int, mid: Optional[str] = None) -> str:
        self.validator.check_boundries(value=x, minimum=20, maximum=500)
        self.validator.check_boundries(value=y, minimum=20, maximum=500)
        self.validator.check_boundries(value=z, minimum=20, maximum=500)
        self.validator.check_boundries(value=speed, minimum=10, maximum=100)
        return f"{self.GO} {x} {y} {z} {speed}"

    def stop(self) -> str:
        return self.STOP

    def curve(
        self,
        x1: int,
        y1: int,
        z1: int,
        x2: int,
        y2: int,
        z2: int,
        speed: int,
        mid: Optional[str] = None,
    ) -> str:
        self.validator.check_boundries(value=x1, minimum=20, maximum=500)
        self.validator.check_boundries(value=y1, minimum=20, maximum=500)
        self.validator.check_boundries(value=z1, minimum=20, maximum=500)
        self.validator.check_boundries(value=x2, minimum=20, maximum=500)
        self.validator.check_boundries(value=y2, minimum=20, maximum=500)
        self.validator.check_boundries(value=z2, minimum=20, maximum=500)
        self.validator.check_boundries(value=speed, minimum=10, maximum=100)
        return f"{self.CURVE} {x1} {y1} {z1} {x2} {y2} {z2} {speed}"

    def jump(
        self, x: int, y: int, z: int, speed: int, yaw: int, mid1: str, mid2: str
    ) -> str:
        pass

    def speed(self, value: int) -> str:
        self.validator.check_boundries(value=value, minimum=10, maximum=100)
        return f"{self.SPEED} {value}"

    def rc(self, a: int, b: int, c: int, d: int) -> str:
        self.validator.check_boundries(value=a, minimum=-100, maximum=100)
        self.validator.check_boundries(value=b, minimum=-100, maximum=100)
        self.validator.check_boundries(value=c, minimum=-100, maximum=100)
        self.validator.check_boundries(value=d, minimum=-100, maximum=100)
        return f"{self.RC} {a} {b} {c} {d}"

    def wifi(self, ssid: str, password: str) -> str:
        return f"{self.WIFI} {ssid} {password}"

    def mon(self) -> str:
        return f"{self.MON}"

    def moff(self) -> str:
        return f"{self.MOFF}"

    def ap(self, ssid: str, password: str) -> str:
        return f"{self.AP} {ssid} {password}"

    def get_speed(self) -> str:
        return self.GET_SPEED

    def get_battery(self) -> str:
        return self.GET_BATTERY

    def get_time(self) -> str:
        return self.GET_TIME

    def get_wifi(self) -> str:
        return self.GET_WIFI

    def get_sdk(self) -> str:
        return self.GET_TIME

    def get_sn(self) -> str:
        return self.GET_SN
