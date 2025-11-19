import sys

# Check if all required arguments are provided
if len(sys.argv) != 5:
    print("\n--- Product Details (Default) ---")
    print("Product Name       : karthika")
    print("Manufacturing Date : 18/03/2023")
    print("Expiry Date        : 8/8/2024")
    print("Batch Number       : 83838")
else:
    # Assign arguments
    product_name = sys.argv[1]
    manufacturing_date = sys.argv[2]
    expiry_date = sys.argv[3]
    batch_number = sys.argv[4]

    # Print product details
print("\n--- Product Details ---")
print(f"Product Name       : {product_name}")
print(f"Manufacturing Date : {manufacturing_date}")
print(f"Expiry Date        : {expiry_date}")
print(f"Batch Number       : {batch_number}")
