select PRO."numProduit",PRO."nomProduit", count(*)
	FROM "PRODUIT" as PRO 
	inner join "DTLFACT" on PRO."numProduit" = "DTLFACT"."numProduit"
	group by PRO."numProduit" 
	order by 3 desc
	limit 5 