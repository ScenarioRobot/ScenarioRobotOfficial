@echo off
TITLE SCENARIO ROBOT
:: Enables virtual env mode and then start ScenarioRobot
env\scripts\activate.bat && py -m ScenarioRobot
