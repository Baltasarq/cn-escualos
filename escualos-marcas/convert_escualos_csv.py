# cn-escualos (c) 2019 Baltasar MIT License <baltasarq@gmail.com>


import csv


def to_float(s):
    f = 0.0
    s = s.strip()
    
    if s:
        f = float(s.strip())
        
    return f


def create_csv_file(fn, key, dist, style):
    with open(fn, "wt") as out_csv_file:
        field_names = ["nif", "dist", "style", "millis"]
        writer = csv.DictWriter(out_csv_file, field_names)

        for info_entry in all_info.items():
            info = info_entry[1]
            record = int(to_float(info[key]) * 1000.0)
            
            if record > 0:
                row_dict = {}
                row_dict["nif"] = info["nif"]
                row_dict["dist"] = dist
                row_dict["style"] = style
                row_dict["millis"] = str(record)
            
                writer.writerow(row_dict)
    

if __name__ == "__main__":
    all_info = {}
    with open("marcas.csv", newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        
        for row in reader:
            info = {}
            
            for key in row.keys():
                value = row[key]
                if key.lower() == "nif":
                    info["nif"] = value
                elif key[0].isdigit():
                        info[key] = value
                    
            all_info[info["nif"]] = info
        
    create_csv_file("marcas_50mrps.csv", "50M", 50, "mrps")
    create_csv_file("marcas_50esp.csv", "50E", 50, "esp")
    create_csv_file("marcas_50brz.csv", "50B", 50, "brz")
    create_csv_file("marcas_50crl.csv", "50C", 50, "crl")

    create_csv_file("marcas_100mrps.csv", "100M", 100, "mrps")
    create_csv_file("marcas_100esp.csv", "100E", 100, "esp")
    create_csv_file("marcas_100brz.csv", "100B", 100, "brz")
    create_csv_file("marcas_100crl.csv", "100C", 100, "crl")
