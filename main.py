import function_cefile  as fc_ce
import function_xml as fc_xml
import function_database as fc_db
import function_compare as fc_cp

def main():
    df = fc_ce.read_excel(r'raw_data/LASER_CE.xlsx')
    data =fc_ce.read_sheet(df)
    fc_xml.parse_para_xml(r'raw_data/P3C globals.xml', data, 366)
    fc_xml.parse_para_xml(r'raw_data/S6 plus P3_EL V3 268.xml', data, 366)
    fc_xml.color_cell(data, 366)
    print("SUCCESS")
    fc_ce.save(df)

if __name__ == main:
    main()
