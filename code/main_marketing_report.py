import sys
from sales_pipeline import (
    get_raw_sales_data,
    clean_sales_data,
    summarize_by_item,
    find_top_entry,
    print_item_table,
)

# --- Seed handling (same three lines as Finance) --------------------------------
seed = None
if len(sys.argv) > 1 and sys.argv[1].strip() != "":
    seed = int(sys.argv[1])

# --- Header ---------------------------------------------------------------------
print("=== MARKETING: Revenue by Item ===")
print()

# 1. Extract
raw_rows = get_raw_sales_data(seed=seed)

# 2. Transform
cleaned_rows = clean_sales_data(raw_rows)
summary = summarize_by_item(cleaned_rows)

top_by_revenue = find_top_entry(summary, "revenue")
top_by_units = find_top_entry(summary, "units_sold")

# 3. Load
print_item_table(summary)
print()
print(
    f"Top seller by revenue: {top_by_revenue['item']} "
    f"(${top_by_revenue['revenue']:,.2f})"
)
print(
    f"Top seller by units:   {top_by_units['item']} "
    f"({top_by_units['units_sold']} units)"
)

