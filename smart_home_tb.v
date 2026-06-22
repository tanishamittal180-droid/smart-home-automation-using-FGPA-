`timescale 1ns/1ps

module smart_home_tb;

reg clk=0;
reg reset;

wire motion_sensor;
wire light_sensor;
wire temp_high;
wire door_open;

wire alarm;
wire light_pwm;
wire fan_pwm;
wire ac;
wire energy_save;

always #5 clk=~clk;

sensor_generator SENSOR(

.clk(clk),
.reset(reset),

.motion_sensor(motion_sensor),
.light_sensor(light_sensor),
.temp_high(temp_high),
.door_open(door_open)

);

smart_home_controller DUT(

.clk(clk),
.reset(reset),

.motion_sensor(motion_sensor),
.light_sensor(light_sensor),
.temp_high(temp_high),
.door_open(door_open),

.manual_override(0),
.security_mode(1),

.scene_select(0),

.force_light(0),
.force_fan(0),
.force_ac(0),

.alarm(alarm),

.light_pwm(light_pwm),
.fan_pwm(fan_pwm),

.ac(ac),
.energy_save(energy_save)

);

initial
begin

$dumpfile("smart_home.vcd");
$dumpvars(0,smart_home_tb);

reset=1;

#20;

reset=0;

#1000;

$finish;

end

always @(posedge clk)

begin

$display(
"%0t,%0d,%0d,%0d,%0d,%0d",
$time,
light_pwm,
fan_pwm,
ac,
alarm,
energy_save
);

end

endmodule