# CNEscualos (c) 2019 Baltasar MIT License <baltasarq@gmail.com>


from model.member import Member
from model.record_entry import RecordEntry
from model.swim_styles import SwimStyles


def import_records_csv_file(file_contents):
    summary = ""
    i = 0

    for row in file_contents.split('\n'):
        i += 1
        row = row.strip().lower()
        data = row.split(',')

        print("Row:", i, ":", data)
        if len(data) < 4:
            summary += "\nNo contents in row: " + str(i)
            continue

        # Skip header, if found
        if data[0] == "nif":
            summary += "\nHeader skipped in row: " + str(i)
            continue

        # Find member
        m = Member.query(Member.dni == data[0].upper()).get()
        print("Member:", m)
        if not m:
            summary += "\nMember not found for NIF: '" + data[0] + "' in row: " + str(i)
            continue

        # Decode data
        style_id = SwimStyles.id_from_abbrev(data[2].strip().lower())
        millis = int(data[3])
        distance = int(data[1])
        where = data[4] if len(data) > 4 else ""

        # Store data
        record_entry = RecordEntry(
                            style_id=style_id,
                            distance=distance,
                            milliseconds=millis,
                            where=where)
        m.records.append(record_entry)
        m.put()

    summary += "\nProcessed " + str(i) + " row(s)."
    return summary
