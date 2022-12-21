select "PAYS"."pays", count(*) as nbfacture
	from "FACTURE" 
	inner join "DTLFACT" on "FACTURE"."numFacture" = "DTLFACT"."numFacture"
	inner join "PAYS" on "PAYS"."pays" = "FACTURE"."pays"
	group by "PAYS"."pays"; 
	limit 5;