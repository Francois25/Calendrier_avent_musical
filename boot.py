# This file is executed on every boot (including wake-boot from deepsleep)
import gc
import esp

gc.collect()
gc.enable()
esp.osdebug(None)