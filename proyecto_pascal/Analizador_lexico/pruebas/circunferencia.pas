program lecccion6;
const Pi = 3.14156;
var
    radio : integer;
    entrada : char;

begin
  {esto es un
  comentario }
  write("¿necesitas saber la circunferencia? [S/N]"); readln(entrada);
  if(entrada = "s") or (entrada = "S") then
  begin
      write("Escribe el radio: "); readln(radio);
      write("la circunferencia es ");
      write(2*Pi*radio);
  end
  else writeln("No se ha calculado la circunferencia. ");
  (*Esto es otro
  comentario*)
end.
