fun main()
	v:INT[8192];
	i:INT;
	n:INT;
begin
	print("Entre n: ");
	READ(n);
	i := 0 ;
	WHILE i < n DO
	BEGIN
		READ(v[i]);
		i := i+1
	END;
	quicksort( 0 , n-1 , v );
	i := 0  ;
	WHILE i < n-1 DO
	BEGIN
		WRITE(v[i]); PRINT(" ");
		IF 0 < v[i] + v[i+1] THEN
		BEGIN
			PRINT("Quicksort falló");
			write(i);
			PRINT("\n");
			RETURN 0
		END
		ELSE
			i := i + 1
	END;
	WRITE(v[i]);
	PRINT("Éxito\n")
END
