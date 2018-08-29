#Created by KshParis (GitHub)
#Utility to export a given SQL querry as EXCEL

import ConnectToOracle as Connection
import xlwt
import os

try:
    def export_to_excel():
        """
        usage: 
            used to export data in a given sql into an excel file.
        return: 
            Path and file name
        """
        row_number = 0
        filename = "Export_objects.xls"

        wb = xlwt.Workbook()
        ws1 = wb.add_sheet("Object_List")
        
        #replace the sample SQL with your SQL
        sql_export = Connection.cur.execute("select max_val, min_val, column_name, data_type, owner, table_name, "
                                            "customer_identifier_col, to_char(info_rec_date, 'dd-mon-yy') "
                                            "from FINAL_REPORT")
        export = sql_export.fetchall()

        for row in export:
            column_num=0
            for item in row: #i.e. for each field in that row
                ws1.write(row_number, column_num, str(item))  #write excel cell from the cursor at row 1
                column_num=column_num+1  #increment the column to get the next field

            row_number=row_number+1 #increment the row number so the next row goes below it...

        wb.save(filename)
        cwd = os.getcwd()
        output = ("File generated and saved at location" + str(cwd) +  "\nFile name: " + filename)
        return output
except:
    print("Error starting application - Export to Excel")
