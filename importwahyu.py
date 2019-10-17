import tugasgeometri

def main():
	s = float(input("masukkan jarak tempuh : "))
	t = float(input("masukkan waktu tempuh : "))
	v = float(input("masukkan kecepatan rata-rata : "))
	kecepatan = tugasgeometri.menghitungkecepatanratarata(s,t)
	
	print("\nkecepatan rata-rata kendaraan " )

	print("hasil : ",kecepatan, " km/jam")
	
	
	print ("\nMenghitung jarak tempuh " )
	
	
	
	jarak = tugasgeometri.menghitungjaraktempuh(t, v)
	
	print("jarak yang di tempuh ")
	print("hasil : ",jarak, "km")
	
	print("\nMenghitung waktu yang di tempuh ")
	
	waktu = tugasgeometri.menghitungwaktutempuh(s,v )
	
	print("\nWaktu yang di tempuh adalah",waktu, "menit" )
	
	
if __name__ =="__main__":
	main()
