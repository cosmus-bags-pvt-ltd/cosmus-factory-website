from django.contrib import admin

# Register your models here.

from . models import AccountGroup, AccountSubGroup,   Product ,  gst,MainCategory ,Color , ProductImage,PProduct_Creation, StockItem, item_godown_quantity_through_table,Finished_goods_transfer_records,Item_Creation, product_2_item_through_table, purchase_order, purchase_order_for_puchase_voucher_rm, purchase_order_for_raw_material, purchase_order_for_raw_material_cutting_items, purchase_order_master_for_puchase_voucher_rm, purchase_order_raw_material_cutting, purchase_order_to_product_cutting, raw_material_product_ref_items, raw_material_production_estimation,finishedgoodsbinallocation

class PProductCreationInline(admin.TabularInline):
    model = PProduct_Creation
    extra = 1


class ProductAdmin(admin.ModelAdmin):
    inlines = [PProductCreationInline]

# admin.site.register(Product, ProductAdmin)

# admin.site.register(Color)
# admin.site.register(ProductImage)
# admin.site.register(MainCategory)
# admin.site.register(PProduct_Creation)
# admin.site.register(AccountGroup)
# admin.site.register(AccountSubGroup)
# admin.site.register(StockItem)
# admin.site.register(gst)
# admin.site.register(item_godown_quantity_through_table)
admin.site.register(purchase_order_master_for_puchase_voucher_rm)
admin.site.register(purchase_order_for_puchase_voucher_rm)


















