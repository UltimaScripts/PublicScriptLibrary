#Over Head Timer With Formatting
#Credit to Reetus
SetTimer("shmoo", 2121)
HeadMsg("Timer: {:.1f}s".format(float(Timer('shmoo'))/1000), "self")