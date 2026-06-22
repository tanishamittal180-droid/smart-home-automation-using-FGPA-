module smart_home_controller(

input clk,
input reset,

input motion_sensor,
input light_sensor,
input temp_high,
input door_open,

input manual_override,
input security_mode,

input [1:0] scene_select,

input force_light,
input force_fan,
input force_ac,

output alarm,
output light_pwm,
output fan_pwm,

output reg ac,
output reg energy_save

);

reg [7:0] light_level;
reg [7:0] fan_speed;

always @(posedge clk or posedge reset)

begin

if(reset)

begin

light_level<=0;
fan_speed<=0;

ac<=0;

energy_save<=0;

end

else

begin

if(force_light)
light_level<=255;

else if(motion_sensor && !light_sensor)
light_level<=200;

else
light_level<=0;


if(force_fan)

fan_speed<=255;

else if(temp_high)

fan_speed<=180;

else

fan_speed<=0;


if(force_ac)

ac<=1;

else

ac<=temp_high;

end

end

assign alarm=(security_mode && door_open);

pwm light_unit(

.clk(clk),
.reset(reset),
.duty_cycle(light_level),
.pwm_out(light_pwm)

);

pwm fan_unit(

.clk(clk),
.reset(reset),
.duty_cycle(fan_speed),
.pwm_out(fan_pwm)

);

endmodule