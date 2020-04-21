import openpyxl

def write_to_excel_file(filename,sheet_name,row,col,data):
	colrow= chr(int(col)+64) + str(row)
	xfile = openpyxl.load_workbook(filename)
	sheet = xfile.get_sheet_by_name(sheet_name)
	sheet[colrow] = data
	xfile.save(filename)
	xfile.close

	
def Read_From_Excel(filename,sheet_name,row,col):
	colrow= chr(int(col)+64) + str(row)
	xfile = openpyxl.load_workbook(filename)
	sheet = xfile.get_sheet_by_name(sheet_name)
	cell_value = sheet[colrow]
	xfile.close
	return cell_value.value

