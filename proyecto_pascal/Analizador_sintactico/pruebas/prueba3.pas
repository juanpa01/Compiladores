program bar;
fun f(sum,x:int):int;
  begin
    if x<>0 then
       begin
         f(sum+x,x-1);
       end
    else
      f:=sum;
  end
begin
  writeln(f(0,10));
end.
