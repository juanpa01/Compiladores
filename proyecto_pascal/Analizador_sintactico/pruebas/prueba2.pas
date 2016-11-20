program forstatement;
var x,sum:int;
var c:char;
begin
  sum:=0;
  for x := 1 to 10 do
    sum:=sum+x;
  writeln(sum);

  sum:=0;
  for x := 10 downto 1 do
    sum:=sum+x;
  writeln(sum);

  for c := 'a' to 'c' do
    write(c);
  writeln;
  for c := 'c' downto 'a' do
    write(c);
  writeln;
end.
