import requests
import time
import csv

data = [
  {
    "nama": "JAWA TENGAH",
    "id": 191097,
    "kode": "33",
    "tingkat": 1
  }
]
def saveData(writer, wilayah, data):
    chart = data["chart"]
    paslon1 = chart.get("100025", 0)
    paslon2 = chart.get("100026", 0)
    paslon3 = chart.get("100027", 0)
    totalPaslon = paslon1 + paslon2 + paslon3
    if totalPaslon != data["administrasi"]["suara_sah"]:
        print(wilayah["prov"], ">",
            wilayah["kota"], ">",
            wilayah["kec"], ">",
            wilayah["kel"], ">",
            wilayah["tps"], "Is Invalid. Suara Sah: ", data["administrasi"]["suara_sah"], "Total Paslon: ", totalPaslon
        )
        writer.writerow([
            wilayah["prov"],
            wilayah["kota"],
            wilayah["kec"],
            wilayah["kel"],
            wilayah["tps"],
            data["administrasi"]["suara_sah"],
            data["administrasi"]["suara_total"],
            paslon1, paslon2, paslon3,
            data["images"][1]
        ])

with open("Sirekap_Sulbar.csv", 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["Prov", "Kota", "Kec", "Kel", "TPS", "Suara Sah", "Total Suara", "Paslon 1", "Paslon 2", "Paslon 3", "Link Dokumen"])
    
    for prov in data:
        print(prov['nama'])
        urlKota = "https://sirekap-obj-data.kpu.go.id/wilayah/pemilu/ppwp/{}.json".format(prov["kode"])
        kotas = requests.get(urlKota).json()
        for kota in kotas:
            # print(prov['nama'], " > ", kota['nama'])
            urlKec = "https://sirekap-obj-data.kpu.go.id/wilayah/pemilu/ppwp/{}/{}.json".format(prov["kode"], kota["kode"])
            kecs = requests.get(urlKec).json()
            for kec in kecs:
                print(prov['nama'], ">", kota['nama'], ">", kec["nama"])
                urlKel = "https://sirekap-obj-data.kpu.go.id/wilayah/pemilu/ppwp/{}/{}/{}.json".format(prov["kode"], kota["kode"], kec["kode"])
                kels = requests.get(urlKel).json()
                for kel in kels:
                    # print(prov['nama'], " > ", kota['nama'], " > ", kec["nama"], kel["nama"])
                    urlTps = "https://sirekap-obj-data.kpu.go.id/wilayah/pemilu/ppwp/{}/{}/{}/{}.json".format(prov["kode"], kota["kode"], kec["kode"], kel["kode"])
                    tpss = requests.get(urlTps).json()
                    for tps in tpss:
                        # print(prov['nama'], " > ", kota['nama'], " > ", kec["nama"], kel["nama"], tps["nama"])
                        urlTps = "https://sirekap-obj-data.kpu.go.id/pemilu/hhcw/ppwp/{}/{}/{}/{}/{}.json".format(prov["kode"], kota["kode"], kec["kode"], kel["kode"], tps["kode"])
                        dataTps = requests.get(urlTps).json()
                        if dataTps is not None and dataTps["administrasi"] is not None and dataTps["chart"] is not None:
                            # print("Saving data")
                            wilayah = {
                                "prov": prov["nama"],
                                "kota": kota["nama"],
                                "kec": kec["nama"],
                                "kel": kel["nama"],
                                "tps": tps["nama"]
                            }
                            saveData(writer,wilayah, dataTps)
                        # time.sleep(0.25)
