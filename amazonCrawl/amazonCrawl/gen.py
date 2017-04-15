source = "https://www.amazon.com/gp/goldbox/ref=gbps_ftr_s-3_596a_page_"
end = "?gb_f_GB-SUPPLE=page:"
ls = []
for i in range(1, 159):
	ls.append(source+str(i)+end+str(i))

def retriveLS():
	return ls