module uart_controller(

input clk,
input reset,

input [7:0] command,

output reg force_light,
output reg force_fan,
output reg force_ac

);

always @(posedge clk or posedge reset)

begin

if(reset)

begin
force_light<=0;
force_fan<=0;
force_ac<=0;
end

else

begin

case(command)

8'd76: force_light<=1; //L

8'd70: force_fan<=1; //F

8'd65: force_ac<=1; //A

default:

begin
force_light<=0;
force_fan<=0;
force_ac<=0;
end

endcase

end

end

endmodule