from inventory import Inventory

def main():
    inventory_open = True
    inv = Inventory()
    inv.load_data()
    while inventory_open:
        print("""========== Inventory Management ==========
1. Add Product
2. View Products
3. Search Product
4. Update Product
5. Delete Product
6. Low Stock Report
7. Total Inventory Value
8. Save & Exit""")
        try:
            b = int(input("Enter Your Choice: "))
            if b==1:
                inv.add_product()
            elif b==2:
                inv.view_products()
            elif b==3:
                inv.search_product()
            elif b==4:
                inv.update_product()
            elif b==5:
                inv.delete_product()
            elif b==6:
                inv.low_stock_report()
            elif b==7:
                inv.inventory_value()
            elif b==8:
                inventory_open = False
            else:
                print("Please Enter From Given Options.")
        except ValueError:
            print("Please Enter Integer")
        
main()