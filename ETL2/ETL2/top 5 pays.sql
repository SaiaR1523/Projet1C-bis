select "PAYS"."pays", "DTLFACT"."numProduit", count ("FACTURE"."numFacture") as nbfacture
	from "FACTURE" 
	inner join "DTLFACT" on "FACTURE"."numFacture" = "DTLFACT"."numFacture"
	inner join "PAYS" on "PAYS"."pays" = "FACTURE"."pays"
	group by "PAYS"."pays","DTLFACT"."numProduit"
	order by 3 desc
	limit 5;