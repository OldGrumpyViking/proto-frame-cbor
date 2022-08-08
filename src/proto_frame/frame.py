import abc


class BaseFrame(abc.ABC):
    @abc.abstractclassmethod
    def from_bytes(cls, frame_bytes: bytes):
        pass

    @classmethod
    def from_hex(cls, frame_hex: str):
        if len(frame_hex) % 2:
            raise ValueError("Hex string must be even number of chars.")
        if frame_hex.startswith("0x"):
            frame_hex = frame_hex[2:]
        return cls.from_bytes(bytes.fromhex(frame_hex))

    @classmethod
    def from_bin(cls, frame_bin: str):
        if frame_bin.startswith("0b"):
            frame_bin = frame_bin[2:]
        return cls.from_bytes(int(frame_bin, 2).to_bytes((len(frame_bin) + 7) // 8, byteorder="big"))

    @abc.abstractmethod
    def to_bytes(self) -> bytes:
        return b""

    def to_hex(self, prefix: bool = False) -> str:
        if prefix:
            return f"0x{self.to_bytes().hex().upper()}"
        return self.to_bytes().hex().upper()

    def to_bits(self, prefix: bool = False) -> str:
        frame_bytes = self.to_bytes()
        if prefix:
            return f"0b{format(int.from_bytes(frame_bytes, byteorder='big'), f'0{len(frame_bytes)*8}b')}"
        return format(int.from_bytes(frame_bytes, byteorder="big"), f"0{len(frame_bytes)*8}b")


def Frame(BaseFrame):
    pass
