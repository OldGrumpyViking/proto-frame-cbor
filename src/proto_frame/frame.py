import abc

import bitstring


class BaseFrame(abc.ABC):
    @abc.abstractclassmethod
    def _from_bitstring(cls):
        pass

    @classmethod
    def from_bytes(cls, frame_bytes: bytes):
        return cls._from_bitstring(bitstring.Bits(frame_bytes))

    @classmethod
    def from_hex(cls, frame_hex: str):
        if frame_hex.startswith("0x"):
            return cls._from_bitstring(bitstring.Bits(frame_hex))
        return cls._from_bitstring(f"0x{bitstring.Bits(frame_hex)}")

    @classmethod
    def from_bin(cls, frame_bin: str):
        if frame_bin.startswith("0b"):
            return cls._from_bitstring(bitstring.Bits(frame_bin))
        return cls._from_bitstring(f"0b{bitstring.Bits(frame_bin)}")

    @abc.abstractmethod
    def _to_bitstring(self) -> bitstring.Bits:
        return bitstring.Bits()

    def to_bytes(self) -> bytes:
        return self._to_bitstring.bytes

    def to_hex(self) -> str:
        return self._to_bitstring.hex.upper()

    def to_bits(self) -> str:
        return self._to_bitstring.bin


def Frame(BaseFrame):
    pass
