import struct

files = ["1.uint64", "150.uint64", "maxint.uint64"]


def read_uint64_file(path):
    with open(path, "rb") as f:
        data = f.read()
    # Each uint64 is 8 bytes, big-endian
    count = len(data) // 8
    return [struct.unpack(">Q", data[i * 8 : (i + 1) * 8])[0] for i in range(count)]


def encode(n):
    if n < 0 or n > 2**64 - 1:
        raise ValueError("Value must be a uint64 (0 ≤ n ≤ 2^64 - 1)")

    result = bytearray()

    while True:
        byte = n & 0x7F
        n >>= 7

        if n:
            result.append(byte | 0x80)
        else:
            result.append(byte)
            break

    return bytes(result)


def decode(n):
    result = 0
    shift = 0

    for byte in n:
        value = byte & 0x7F
        result |= value << shift

        if byte & 0x80 == 0:
            break

        shift += 7

    return result


def test_varint_round_trip():
    all_values = []
    for filename in files:
        values = read_uint64_file(filename)
        all_values.extend(values)

    for i, value in enumerate(all_values):
        encoded = encode(value)
        decoded = decode(encoded)
        assert decoded == value, f"Mismatch at index {i}: {value} → {decoded}"
        print(f"✅ {value} → {encoded} → {decoded}")


if __name__ == "__main__":
    test_varint_round_trip()
