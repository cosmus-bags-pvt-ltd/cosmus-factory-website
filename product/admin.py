from django.contrib import admin

# Register your models here.

from . models import AccountGroup, AccountSubGroup, Finished_goods_Stock_TransferMaster, Picklist_process_in_outward, Picklist_voucher_master,   Product, Product_bin_quantity_through_table, finished_goods_warehouse_racks, finished_product_warehouse_bin ,  gst,MainCategory ,Color , ProductImage,PProduct_Creation, StockItem, item_godown_quantity_through_table,Finished_goods_transfer_records,Item_Creation, item_purchase_voucher_master, labour_work_in_master, labour_work_in_product_to_item, labour_workin_approval_report, product_2_item_through_table, product_purchase_voucher_items, product_purchase_voucher_master, product_to_item_labour_workout, purchase_order, purchase_order_for_puchase_voucher_rm, purchase_order_for_raw_material, purchase_order_for_raw_material_cutting_items, purchase_order_master_for_puchase_voucher_rm, purchase_order_raw_material_cutting, purchase_order_to_product, purchase_order_to_product_cutting, purchase_voucher_items, raw_material_product_ref_items, raw_material_product_to_items, raw_material_product_wise_qty, raw_material_production_estimation,finishedgoodsbinallocation, raw_material_production_total

class PProductCreationInline(admin.TabularInline):
    model = PProduct_Creation
    extra = 1


class ProductAdmin(admin.ModelAdmin):
    inlines = [PProductCreationInline]

admin.site.register(Product, ProductAdmin)

# admin.site.register(Color)
# admin.site.register(ProductImage)
# admin.site.register(MainCategory)
# admin.site.register(PProduct_Creation)
# admin.site.register(AccountGroup)
# admin.site.register(AccountSubGroup)
# admin.site.register(StockItem)
# admin.site.register(gst)
# admin.site.register(item_godown_quantity_through_table)

admin.site.register(Product_bin_quantity_through_table)
admin.site.register(Picklist_process_in_outward)











 























