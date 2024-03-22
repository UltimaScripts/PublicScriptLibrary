mob_serial = 0x1234
timeout = 1000
print(WaitForContext(mob_serial, "Rename", timeout))
CancelPrompt()