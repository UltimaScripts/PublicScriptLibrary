# Name: Herding Training
# Author: Ultimascripts
# Notes: Avoid using around impassable objects.
# Goat 40, Stag 90, Moose 100
# You may have to find the same animal-
# to find one that gives gains.
from Assistant import Engine

crook = 0x400a8ba7

PromptAlias("herdmob")
if GetAlias("herdmob") <= 0:
    Stop()

while not Dead("self"):  
    UseObject(crook)
    WaitForTarget(5000)
    Target("herdmob")
    WaitForTarget(5000)
    TargetXYZ(Engine.Player.X + 2, Engine.Player.Y + 2, 0)
    Pause(1000+Ping())
    UseObject(crook)
    WaitForTarget(5000)
    Target("herdmob")
    WaitForTarget(5000)
    TargetXYZ(Engine.Player.X - 2, Engine.Player.Y - 2, 0)
    Pause(1000+Ping())