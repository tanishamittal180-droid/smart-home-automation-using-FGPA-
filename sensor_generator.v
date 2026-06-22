module sensor_generator(

input clk,
input reset,

output reg motion_sensor,
output reg light_sensor,
output reg temp_high,
output reg door_open

);

reg [7:0] counter;

always @(posedge clk or posedge reset)

begin

if(reset)

begin

counter<=0;

motion_sensor<=0;
light_sensor<=1;
temp_high<=0;
door_open<=0;

end

else

begin

counter<=counter+1;

case(counter)

10:
begin
motion_sensor<=1;
light_sensor<=0;
end

30:
temp_high<=1;

50:
door_open<=1;

70:
begin
motion_sensor<=0;
temp_high<=0;
door_open<=0;
end

endcase

end

end

endmodule