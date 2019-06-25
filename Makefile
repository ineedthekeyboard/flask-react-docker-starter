.DEFAULT_GOAL := help


### QUICK
# ¯¯¯¯¯¯¯

startprod: server.startprod

startdev: server.startdev

stop: server.stop


include makefiles/server.mk
include makefiles/test.mk
include makefiles/database.mk
include makefiles/format.mk
include makefiles/help.mk
