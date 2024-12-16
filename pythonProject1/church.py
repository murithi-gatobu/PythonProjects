import Camelot

# Read PDF and specify page number or "all" for all pages
tables = Camelot.read_pdf("statement.pdf", pages="all")

# Convert each table to a dataframe and export to Excel
for i, table in enumerate(tables):
    table.to_excel(f"statement_page_{i+1}.xlsx", index=False)

