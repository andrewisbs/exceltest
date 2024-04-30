import pandas as pd

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)

# Read the TSV file into a DataFrame
df = pd.read_csv("inventory-snapshot-table_2024-01-15_ 01 - sheet1.tsv", sep="\t")

# Combine `Variant` and `SKU` columns
df["Product Variant SKU"] = df["Variant"] + "-" + df["SKU"]

# Write the output to a new TSV file
df.to_csv("inventory_snapshot_table_with_product_variant_sku.tsv", sep="\t", index=False)