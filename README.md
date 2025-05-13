# Varint

Implementing the Base 128 Varint encoding used in Protocol Buffers. This is mostly an excuse to play with a fun data encoding, while exposing you to some basic concepts in working with binary data such as reading hexadecimal, byte ordering and bitwise operations.

# Context

Protocol Buffers (Protobuf) are a language-neutral, platform-neutral, extensible mechanism developed by Google for serializing structured data — similar to XML or JSON, but smaller, faster, and simpler.
A Base 128 Varint (variable-length integer) is a way of encoding integers so that smaller numbers use fewer bytes. It's a compact binary encoding used by Protocol Buffers and other systems (like SQLite and Bitcoin).

# How it works

Each byte stores 7 bits of the number.

The most significant bit (MSB) of each byte is a continuation bit:
1 if there's another byte after it.
0 if it's the last byte.

https://protobuf.dev/programming-guides/encoding/#varints
