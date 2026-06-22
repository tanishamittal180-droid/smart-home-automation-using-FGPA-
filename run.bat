@echo off

echo Compiling Verilog files...

iverilog -o smarthome ^
tb/smart_home_tb.v ^
rtl/pwm.v ^
rtl/uart_controller.v ^
rtl/sensor_generator.v ^
rtl/smart_home_controller.v

echo Running simulation...

vvp smarthome

echo Opening waveform...

gtkwave smart_home.vcd

pause