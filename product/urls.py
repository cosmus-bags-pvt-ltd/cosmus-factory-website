from django.urls import path
from . import views

handler404 = 'product.views.custom_404_view'

urlpatterns = [
    
    #product_routes
    path('editpproduct/<int:pk>',views.edit_production_product , name= 'edit_production_product'),
    path('pproduct_creation/',views.product_color_sku , name='pproduct_creation'),
    path('pproduct_creation_ref_id/<int:ref_id>',views.product_color_sku , name= 'pproduct-creation-with-ref-id'),
    path('pproductlist/',views.pproduct_list ,name= 'pproductlist'),
    path('pproductdelete/<int:pk>',views.pproduct_delete, name= 'pproductdelete'),

    #productandcategory
    path('definemaincategoryproduct/',views.definemaincategoryproduct, name= 'define-main-category-product'),
    path('definemaincategoryupdateproduct/<int:pk>',views.definemaincategoryproduct, name= 'define-main-category-update-product'),
    path('definemaincategoryproductdelete/<int:pk>',views.definemaincategoryproductdelete, name= 'define-main-category-delete-product'),

    path('definesubcategoryproduct/',views.definesubcategoryproduct, name= 'define-sub-category-product'),
    path('definesubcategoryupdateproduct/<int:pk>',views.definesubcategoryproduct, name= 'define-sub-category-update-product'),

    path('assignbintoproductajax/',views.assign_bin_to_product_ajax, name= 'assign-bin-to-product-ajax'),
    path('savebintosubcategory/<int:sub_id>/',views.save_bin_to_subcategory, name= 'save-bin-to-subcategory'),
    path('updatebintosubcategory/<int:sub_id>/<int:r_id>/<int:bin_id>',views.update_bin_to_subcategory, name= 'update-bin-to-subcategory'),
    path('subcategorybinlist/',views.subcategory_bin_list, name= 'subcategory-bin-list'),
    # path('assignbintoproductform/',views.assign_bin_to_product_form, name= 'assign-bin-to-product-form'),



    path('definesubcategoryproductdelete/<int:pk>',views.definesubcategoryproductdelete, name= 'define-sub-category-product-delete'),

    path('product2subcategoryupdate/<int:pk>',views.product2subcategory, name= 'product-2-subcategory-update'),
    path('product2subcategory/',views.product2subcategory, name= 'product-2-subcategory'),
    path('product2subcategoryajax/',views.product2subcategoryajax, name = 'product2subcategory-ajax'),
    path('product2subcategoryproductajax/', views.product2subcategoryproductajax, name = 'product2subcategoryajax'),

    #productImages
    path('product/add_images/<int:pk>/', views.add_product_images, name='add-product-images'),

    #productVideourl
    path('product/add_video_url/<int:pk>/', views.add_product_video_url, name='add-product-video-url'),


    #color routes
    #color modal routes
    # path('colorlist/',views.color_list, name= 'colorlist'),
    path('colordelete/<int:pk>',views.color_delete,name='colordelete'),
    path('colorcreate_update/',views.color_create_update, name='colorlist'),
    path('colorcreate_update/<int:pk>',views.color_create_update, name='coloredit'),

    # color in page
    path('simple_colorcreate_update/',views.color_create_update, name='simplecolorlist'),
    path('simple_colorcreate_update/<int:pk>',views.color_create_update, name='simplecolorlistupdate'),

    #color popup
    path('color_popup/',views.color_create_update, name='color-popup'),

    #rack for raw material
    path('createrackforrawmaterial/',views.create_update_rack_for_raw_material , name= 'create-rack-for-raw-material'),
    path('updaterackforrawmaterial/<int:r_id>/',views.create_update_rack_for_raw_material , name= 'update-rack-for-raw-material'),
    path('deleterackforrawmaterial/<int:r_id>/',views.delete_rack_for_raw_material , name= 'delete-rack-for-raw-material'),

    #bin for raw material
    path('createbinforrawmaterial/<int:r_id>/',views.create_update_bin_for_raw_material , name= 'create-bin-for-raw-material'),
    path('updatebinforrawmaterial/<int:r_id>/<int:b_id>/',views.create_update_bin_for_raw_material , name= 'update-bin-for-raw-material'),
    path('deletebinforrawmaterial/<int:b_id>/',views.delete_bin_for_raw_material , name= 'delete-bin-for-raw-material'),


    #item_routes
    path('itemedit/<int:pk>',views.item_edit , name= 'item-edit'),
    path('itemcreate/',views.item_create , name= 'item-create'),
    path('itemlist/',views.item_list ,name= 'item-list'),
    path('itemdelete/<int:pk>',views.item_delete , name= 'item-delete'),

    path('itemcreatecloneajax/',views.item_clone_ajax , name= 'item-create-clone-ajax'),
    path('itemcreatepopup/',views.item_create , name= 'item-create-popup'),

    #opening_godown_qty
    path('openinggodownquantity/<int:parent_row_id>',views.openingquantityformsetpopup , name= 'opening-godown-qty'),
    path('openinggodownquantitypk/<int:primary_key>/<int:parent_row_id>',views.openingquantityformsetpopup , name= 'opening-godown-qty-pk'),
    path('openinggodownquantityajax/',views.openingquantityformsetpopupajax , name= 'opening-godown-qty-ajax'),

    #itemfabgroup
    path('itemfabricgroupcreateupdate/',views.item_fabric_group_create_update , name= 'item-fabgroup-create-list'),
    path('itemfabricgroupcreateupdate/<int:pk>',views.item_fabric_group_create_update , name= 'item-fabgroup-update'),
    path('itemfabricgroupdelete/<int:pk>',views.item_fabric_group_delete , name= 'item-fabgroup-delete'),
    #popup
    path('fabric_popup/',views.item_fabric_group_create_update, name='fabric-popup'),


    #unitname
    path('unitnamecreate/',views.unit_name_create_update , name= 'unit_name-create_list'),
    path('unitnameupdate/<int:pk>',views.unit_name_create_update , name= 'unit_name-update'),
    path('unitnamedelete/<int:pk>',views.unit_name_delete , name= 'unit_name-delete'),
    #popup
    path('units_popup/',views.unit_name_create_update, name='unit-name-popup'),
    path('itemnamepkajax/',views.unit_name_units_ajax, name='item-name-pk-ajax'),

    #accountsubgrp
    path('accsubgrpcreate/',views.account_sub_group_create_update , name= 'account_sub_group-create'),
    path('accsubgrpupdate/<int:pk>',views.account_sub_group_create_update , name= 'account_sub_group-update'),
    path('accsubgrpdelete/<int:pk>',views.account_sub_group_delete , name= 'account_sub_group-delete'),

    #stockitem
    path('stockitemcreate/', views.stock_item_create_update, name= 'stock-item-create'),
    path('stockitemupdate/<int:pk>', views.stock_item_create_update, name= 'stock_item-update'),
    path('stockitemdelete/<int:pk>', views.stock_item_delete, name= 'stock_item-delete'),


    #ledger
    path('ledgercreate/', views.ledgercreate, name = 'ledger-create'),
    path('ledgerupdate/<int:pk>', views.ledgerupdate, name = 'ledger-update'),
    path('ledgerlist/', views.ledgerlist, name = 'ledger-list'),
    path('ledgerdelete/<int:pk>', views.ledgerdelete, name = 'ledger-delete'),

    path('ledgerpopupcreate/', views.ledgercreate, name = 'ledger-popup-create'),

    path('ledgertypecreate/', views.ledgerTypes_create_update, name = 'ledger-Types-create'),
    path('ledgertypeupdate/<int:pk>', views.ledgerTypes_create_update, name = 'ledger-Types-update'),
    path('ledgertypedelete/<int:pk>', views.ledgerTypes_delete, name = 'ledger-Types-delete'),

    path('ledgertypecreatepopup/', views.ledgerTypes_create_update, name = 'ledger-Types-create-popup'),


    #godown
    path('godowncreate/', views.godowncreate, name = 'godown-create'),
    path('godownupdateraw/<str:str>/<int:pk>', views.godownupdate, name = 'godown-update'),
    path('godownlist/', views.godownlist, name = 'godown-list'),
    path('godowndelete/<str:str>/<int:pk>', views.godowndelete, name = 'godown-delete'),


    # #stocktransfer
    path('stocktransferrawcreate/', views.stockTrasferRaw, name = 'stock-transfer-raw-create'),
    path('stocktransferrawupdate/<int:pk>', views.stockTrasferRaw, name = 'stock-transfer-raw-update'),
    path('stocktransferrawdelete/<int:pk>', views.stockTrasferRawDelete, name = 'stock-transfer-raw-delete'),
    path('stocktransferrawlist/', views.stockTrasferRawList, name = 'stock-transfer-raw-list'),


    #PurchaseVoucher
    path('purchasevouchercreate/', views.purchasevouchercreateupdate, name = 'purchase-voucher-create'),
    path('purchasevoucherupdate/<int:pk>', views.purchasevouchercreateupdate, name = 'purchase-voucher-update'),
    path('purchasevoucherlist/', views.purchasevoucherlist, name = 'purchase-voucher-list'),
    path('purchasevoucherdelete/<int:pk>', views.purchasevoucherdelete, name = 'purchase-voucher-delete'),

    path('uniquevalidcheckajax/', views.UniqueValidCheckAjax, name = 'unique-pk-valid-check-ajax'),

    path('purchasevoucherrmwithpoajax/', views.purchase_voucher_rm_with_po_ajax, name = 'purchase-voucher-rm-with-po-ajax'),

    path('purchasevoucherpopupcreate/<int:shade_id>/<int:prefix_id>/<str:item_rate>/<str:unique_id>', views.purchasevoucherpopup, name='purchase-voucher-popup-create'),
    path('purchasevoucherpopupupdate/<int:shade_id>/<int:prefix_id>/<int:primarykey>', views.purchasevoucherpopup, name='purchase-voucher-popup-update'),
    path('purchasevouchercreategodownpopupurl/',views.purchasevouchercreategodownpopupurl,name = 'purchasevoucher-createpopup-ajax'),
    path('itemdynamicsearchajax/',views.itemdynamicsearchajax,name = 'item-dynamic-search-ajax'),

    #SalesVoucher
    path('salesvouchercreateupdate/', views.salesvouchercreateupdate, name = 'sales-voucher-create'),
    path('salesvouchercreateupdate/<int:s_id>/<int:dc_id>/', views.salesvouchercreateupdate, name = 'sales-voucher-create'),
    # path('salesvouchercreateupdate//', views.salesvouchercreateupdate, name = 'sales-voucher-create'),
    path('salesvoucherlist/', views.salesvoucherlist, name = 'sales-voucher-list'),
    
    path('salesvoucherdelete/<int:pk>/', views.salesvoucherdelete, name = 'sales-voucher-delete'),


    path('salesvouchercreateupdateforwarehouse/', views.sales_voucher_create_update_for_warehouse, name = 'sales-voucher-create-update-for-warehouse'),
    path('salesvouchercreateupdateforwarehouse/<int:s_id>/<str:action>/', views.sales_voucher_create_update_for_warehouse, name = 'sales-voucher-create-update-for-warehouse'),
    path('salesvoucherlistwarehouse/', views.salesvoucherlistwarehouse, name = 'sales-voucher-list-warehouse'),
    path('salesvoucherviewsortwithsalesman/<int:id>/', views.sales_voucher_view_sort_with_salesman, name='sales-voucher-view-sort-with-salesman'),
    path('salesvoucherviewsortwithpartyname/<int:id>/', views.sales_voucher_view_sort_with_partyname, name='sales-voucher-view-sort-with-partyname'),
    path('salesscanproductdynamicajax/', views.sales_scan_product_dynamic_ajax, name = 'sales-scan-product-dynamic-ajax'),

    #picklist
    path('createupdatepicklist/',views.create_update_picklist , name = 'create-update-picklist'),
    path('createupdatepicklist/<int:p_id>/',views.create_update_picklist , name = 'create-update-picklist'),
    path('allpicklistslist/',views.all_picklists_list , name = 'all-picklists-list'),
    path('deletepicklists/<int:pl_id>',views.deletepicklist , name = 'delete-picklists'),
    path('picklistview/<int:pl_id>',views.picklist_view , name = 'picklist-view'),
    path('picklistproductajax/',views.picklist_product_ajax , name = 'picklist-product-ajax'),
    path('downloadpicklistpdf/<int:pl_id>',views.download_picklist_pdf , name = 'download-picklist-pdf'),
    path('downloadpicklistexcel/<int:pl_id>',views.download_picklist_excel , name = 'download-picklist-excel'),
    path('binquantityajax/',views.bin_quantity_ajax , name = 'bin-quantity-ajax'),
    path('deleteformquantityrevert/',views.delete_form_quantity_revert , name = 'delete-form-quantity-revert'),

    #subcategorys
    path('gstcreate/', views.gst_create_update, name = 'gst-create-list'),
    path('gstupdate/<int:pk>', views.gst_create_update, name = 'gst-update'),
    path('gstdelete/<int:pk>', views.gst_delete, name = 'gst-delete'),
    path('gstpopup/',views.gst_create_update, name = 'gst-popup'),


    path('fabricfinishesscreate/', views.fabric_finishes_create_update, name = 'fabric-finishes-create-list'),
    path('fabricfinishesupdate/<int:pk>', views.fabric_finishes_create_update, name = 'fabric-finishes-update'),
    path('fabricfinishesdelete/<int:pk>', views.fabric_finishes_delete, name = 'fabric-finishes-delete'),
    path('fabricfinishespopup/', views.fabric_finishes_create_update, name = 'fabric-finishes-popup'),

    path('packaging_create/', views.packaging_create_update, name = 'packaging-create-list'),
    path('packagingupdate/<int:pk>', views.packaging_create_update, name = 'packaging-update'),
    path('packagingdelete/<int:pk>', views.packaging_delete, name = 'packaging-delete'),
    path('packagingpop/',views.packaging_create_update, name = 'packaging-popup'),

    #Production
    #product2items
    path('product2item/<int:product_refrence_id>',views.product2item, name = 'product-2-item'),
    path('export_Product2Item_excel/<int:product_ref_id>',views.export_Product2Item_excel, name = 'export-Product2Item-excel'),

    path('viewproduct2item_configs/<int:product_sku>',views.viewproduct2items_configs,name ='view-product-2-item-configs'),
    
    #purchase_order
    path('purchaseordercreate/',views.purchaseordercreateupdate, name = 'purchase-order-create'),
    path('purchaseorderupdate/<int:pk>',views.purchaseordercreateupdate, name = 'purchase-order-update'),
    path('purchaseorderlist/',views.purchaseorderlist, name = 'purchase-order-list'),
    path('purchaseorderdelete/<int:pk>',views.purchaseorderdelete, name = 'purchase-order-delete'),



    #purchase_order_for_raw
    path('purchaseorderrawmaterial/<int:p_o_pk>/<int:prod_ref_no>', views.purchaseorderrawmaterial, name = 'purchase-order-rawmaterial'),
    path('purchaseorderrawmaterialupdate/<int:p_o_pk>/<int:prod_ref_no>/<str:model_name>', views.purchaseorderrawmaterial, name = 'purchase-order-rawmaterial-update'),
    path('purchaseorderrawmateriallist/',views.purchase_order_for_raw_material_list, name = 'purchase-order-raw-material-list'),
    path('purchaseorderforrawmaterialdelete/<int:pk>',views.purchase_order_for_raw_material_delete, name = 'purchase-order-for-raw-material-delete'),
    


    #purchase_order_cutting_room
    path('purchaseordercuttinglist/<int:p_o_pk>/<int:prod_ref_no>', views.purchaseordercuttinglist, name = 'purchase-order-cutting-list'),
    path('purchaseordercuttingcreate/<int:p_o_pk>/<int:prod_ref_no>', views.purchaseordercuttingcreateupdate, name = 'purchase-order-cutting-create'),
    path('purchaseordercuttingupdate/<int:p_o_pk>/<int:prod_ref_no>/<int:pk>', views.purchaseordercuttingcreateupdate, name = 'purchase-order-cutting-update'),
    path('purchaseordercuttinglistall/', views.purchaseordercuttinglistall, name = 'purchase-order-cutting-list-all'),
    path('purchaseordercuttingmastercancel',views.purchaseordercuttingmastercancelajax,name = 'purchase-order-cutting-master-cancel'),
    path('pendingapprovall',views.pendingapprovall,name = 'pending-approv-all'),

    path('cuttingroomqty',views.cuttingroomqty,name = 'cutting-room-qty'),

    # factory worker routes
    path('factory_emp_create/',views.factory_employee_create_update_list, name = 'factory-emp-create'),
    path('factory_emp_update/<int:pk>',views.factory_employee_create_update_list, name = 'factory-emp-update'),
    path('factory_emp_delete/<int:pk>',views.factoryempdelete, name = 'factory-emp-delete'),

    #salesman
    path('salesmancreate/',views.salesman_create_update, name = 'salesman-create'),
    path('salesmanupdate/<int:e_id>/',views.salesman_create_update, name = 'salesman-update'),
    path('deletesalesman/<int:e_id>/',views.delete_salesman, name = 'delete-salesman'),

    # cutting Room 
    path('cutting_room_create/',views.cutting_room_create_update_list, name = 'cutting_room-create'),
    path('cutting_room_update/<int:pk>',views.cutting_room_create_update_list, name = 'cutting_room-update'),
    path('cutting_room_delete/<int:pk>',views.cuttingroomdelete, name = 'cutting_room-delete'),

    # approval
    path('purchaseordercuttingpopup/<int:cutting_id>',views.purchaseordercuttingpopup, name = 'purchase-order-cutting-popup'),

    path('purchaseordercuttingapprovalcheckajax/',views.purchaseordercuttingapprovalcheckajax, name='purchase-order-cutting-approval-check-ajax'),
    
    path('purchaseorderlabourworkinapprovecheckajax/', views.purchaseorderlabourworkinapprovecheckajax, name='purchase-order-labour-workin-approve-check-ajax'),

    #labour workout 
    path('labourworkoutall/',views.labourworkoutlistall, name='labour-workout-all'),
    path('labourworkoutsingle/<int:pk>',views.labourworkoutsingle, name = 'labour-workout-single'),
    path('labourworkoutsingleview/<int:labour_workout_child_pk>',views.labourworkoutsingle, name = 'labour-workout-single-view'),
    path('labourworkoutsingledelete/',views.labourworkoutsingledeleteajax, name = 'labour-workout-single-delete'),
    path('labourworkoutchildlist/<int:labour_master_pk>',views.labour_workout_child_list, name = 'labour-workout-child-list'),

    #labour workin
    path('labourworkinlistall/',views.labourworkinlistall, name='labour-workin-list-all'),
    path('labourworkinpurchaseorderlist/<int:p_o_no>',views.labourworkinpurchaseorderlist, name='labour-workin-pur-order-list'),
    path('labourworkincreatelist/<int:l_w_o_id>',views.labourworkincreatelist, name ='labour-workin-list-create'),
    path('labourworkincreate/<int:l_w_o_id>/',views.labourworkincreate, name ='labour-workin-create'),
    path('labourworkincreateupdateview/<int:l_w_o_id>/<int:pk>/<str:approved>',views.labourworkincreate, name ='labour-workin-view-update'),
    path('labourworkinrawcreate/',views.labourworkincreate, name ='labour-workin-create-raw'),

    path('labourworkinsingledelete/',views.labourworkinsingledeleteajax, name = 'labour-workin-single-delete'),

    path('goodsreturnlist/',views.goods_return_pending_list, name = 'goods-return-list'),
    path('goodsreturnpopup/<int:pk>',views.goods_return_popup, name = 'goods_return_popup'),

    # rawmaterial production estimation

    path('rawmaterialestimationlist/',views.rawmaterialestimationlist, name = 'rawmaterial-estimation-list'),
    path('rawmaterialestimationcreate/',views.rawmaterialestimationcreateupdate, name = 'rawmaterial-estimation-create'),
    path('rawmaterialestimationupdate/<int:pk>',views.rawmaterialestimationcreateupdate, name = 'rawmaterial-estimation-update'),
    path('rawmaterialestimationpopup/<int:pk>',views.raw_material_estimation_popup, name = 'raw-material-estimation-popup'),
    path('rawmaterialestimationcalculate/<int:u_id>',views.raw_material_estimation_calculate, name = 'raw-material-estimation-calculate'),
    # path('rawmaterialestimationpopupcalculateinbackend/<int:u_id>',views.raw_material_estimation_pop_up_calculate_in_backend, name = 'raw-material-estimation-pop-up-calculate-in-backend'),

    path('rawmaterialestimatedelete/<int:pk>',views.raw_material_estimate_delete,name= 'raw-material-estimate-delete'),

    path('rawmaterialestimationcalculateexceldownload/',views.raw_material_estimation_calculate_excel_download, name = 'raw-material-estimation-calculate-excel-download'),


    # product_purchase_voucher
    path('productpurchasevouchercreate/',views.product_purchase_voucher_create_update, name = 'product-purchase-voucher-create'),
    path('productpurchasevoucherupdate/<int:pk>',views.product_purchase_voucher_create_update, name = 'product-purchase-voucher-update'),
    path('productpurchasevoucherlist/',views.product_purchase_voucher_list, name = 'product-purchase-voucher-list'),
    path('productpurchasevoucherdelete/<int:pk>',views.product_purchase_voucher_delete, name = 'product-purchase-voucher-delete'),
    
    
    


    # warehouse product transfer
    path('allproducttransfertowarehouse/', views.product_transfer_to_warehouse_list,name='all-product-transfer-to-warehouse'),
    path('producttransfertowarehousedelete', views.product_transfer_to_warehouse_delete,name='product-transfer-to-warehouse-delete'),
    path('warehouseproducttransfercreate/', views.warehouse_product_transfer_create_and_update,name="warehouse-product-transfer-create"),
    path('warehouseproducttransferupdate/<int:pk>', views.warehouse_product_transfer_create_and_update,name="warehouse-product-transfer-update"),
    path('producttransfertowarehouseajax/', views.product_transfer_to_warehouse_ajax,name='product-transfer-to-warehouse-ajax'),
    
    
    #finished_goods

    path('finished-goods-stock-all/', views.finished_goods_stock_all, name = 'finished-goods-stock-all'),
    path('finished-goods-stock-all/<int:pk>', views.finished_goods_stock_all, name = 'finished-goods-stock-single'),
    path('productdynamicsearchajax/',views.productdynamicsearchajax,name = 'product-dynamic-search-ajax'),
    path('scanproductqtylist/', views.scan_product_qty_list, name = 'scan-product-qty-list'),
    path('scanproductlist/<int:pk>/<str:v_type>/', views.scan_product_list, name = 'scan-product-list'),
    path('warehousestock/', views.warehouse_stock, name = 'warehouse-stock'),
    path('productwisesalesreport/<int:sku>/', views.product_wise_sales_report, name = 'product-wise-sales-report'),
    path('productwisesalesreturnreport/<int:sku>/', views.product_wise_sales_return_report, name = 'product-wise-sales-return-report'),
    path('scansingleproductlist/<int:sku>/', views.scan_single_product_list, name = 'scan-single-product-list'),
    path('modelnamewisepurchasetransferreport/<int:sku>/', views.model_name_wise_purchase_transfer_report, name = 'model-name-wise-purchase-transfer-report'),
    path('modelnamewisepurchasetransfersalesreport/<int:sku>/', views.model_name_wise_purchase_transfer_sales_report, name = 'model-name-wise-purchase-transfer-sales-report'),

    #reports
    # path('stocktransferreport/',views.stocktransferreport, name = 'stock-transfer-report'),
    path('creditdebitreport/', views.creditdebitreport, name = 'credit-debit-report'),
    path('godownstockrawmaterialreportfabgrp/<int:g_id>', views.godown_stock_raw_material_report_fab_grp, name = 'godown-stock-raw-material-report_fab_grp'),
    path('godownstockrawmaterialreportfabgrp/<int:g_id>/<int:fab_id>', views.godown_stock_raw_material_report_fab_grp, name = 'godown-stock-raw-material-report_items'),

    path('allrawmaterialstockreport/', views.allrawmaterialstockreport, name = 'all-raw-material-stock-report'),

    path('godownitemreport/<int:shade_id>/<int:g_id>', views.godown_item_report, name = 'godown-item-report'),
    path('godownitemreportallgodown/<int:shade_id>', views.godown_item_report, name = 'godown-item-report-all-godowns'),

    path('rawmaterialexceldownload/', views.raw_material_excel_download, name='raw-material-excel-download'),
    path('rawmaterialexcelupload/', views.raw_material_excel_upload, name='raw-material-excel-upload'),

    path('godownproductreport/<int:g_id>', views.finished_goods_godown_wise_report, name = 'finished-goods-godown-wise-report'),
    path('godownproductreportall/', views.finished_goods_godown_wise_report_all, name = 'finished-goods-godown-wise-report-all'),
    #This
    path('finishedgoodscolorwisereport/', views.finished_goods_color_wise_report, name = 'finished-goods-color-wise-report'),
    path('finishedgoodscolorchallanandgrnvisereport/<int:ref_no>/', views.finished_goods_color_challan_and_grn_vise_report, name = 'finished-goods-color-challan-and-grn-vise-report'),
    path('finishedgoodsgodownproductrefwisereport/<int:ref_no>', views.finished_goods_godown_product_ref_wise_report, name = 'finished-goods-godown-product-ref-wise-report'),
    path('finishedgoodsgodownproductrefvendorwisereport/<int:ref_no>/<int:challan_no>', views.finished_goods_vendor_model_wise_report, name = 'finished-goods-godown-product-ref-vendor-wise-report'),

    path('allfinishedgoodsstockreport/', views.allfinishedgoodsstockreport, name = 'all-finished-goods-stock-report'),
    path('finishedgoodsstockreport/<str:action>/', views.allfinishedgoodsstockreport, name = 'finished-goods-stock-report'),
    path('finishedgoodsmodelwisereport/<int:ref_id>', views.finished_goods_model_wise_report, name = 'finished-goods-model-wise-report'),
    path('qcapprovedmodelwisereport/<int:ref_id>', views.qc_approved_model_wise_report, name = 'qc_approved-goods-model-wise-report'),



    path('labourworkinapprovalsplit/<int:ref_id>', views.labour_workin_approval_split, name= 'labour-workin-approval-split'),
    path('labourworkinpendingsplit/<int:ref_id>/', views.labour_workin_pending_split, name= 'labour-workin-pending-split'),
    
    path('lwoandlwireportvendorwise/', views.lwo_and_lwi_report_vendor_wise, name='lwo-and-lwi-report-vendor-wise'),

    # finished warehouse routes
    path('finishedgoodssortinglist/', views.finished_goods_sorting_list, name='finished-goods-sorting-list'),
    path('stocktransferinstancelistpopup/<int:id>/<str:voucher_type>/', views.stock_transfer_instance_list_and_recieve, name="stock-transfer-instance-list-popup"),
    path('deletesigleentries/<int:e_id>/<str:voucher_type>/', views.delete_sigle_entries, name="delete-sigle-entries"),

    path('addzoneinwarehouse/<int:id>/', views.add_zone_in_warehouse, name="add-zone-in-warehouse"),
    path('editzoneinwarehouse/<int:id>/<int:zone_id>/', views.add_zone_in_warehouse, name="edit-zone-in-warehouse"),
    path('deletezoneinwarehouse/<int:zone_id>/', views.delete_zone_in_warehouse, name="delete-zone-in-warehouse"),

    path('addrackinzone/<int:zone_id>/', views.add_rack_in_zone, name="add-rack-in-zone"),
    path('editrackinzone/<int:zone_id>/<int:rack_id>/', views.add_rack_in_zone, name="edit-rack-in-zone"),
    path('deleterackinzone/<int:rack_id>/', views.delete_rack_in_zone, name="delete-rack-in-zone"),

    path('addbininrack/<int:rack_id>/',views.add_bin_in_rack, name="add-bin-in-rack"),
    path('editbininrack/<int:rack_id>/<int:bin_id>/',views.add_bin_in_rack, name="edit-bin-in-rack"),
    path('deletebininrack/<int:bin_id>/',views.delete_bin_in_rack, name="delete-bin-in-rack"),
    
    path('warehousenavigator/',views.warehouse_navigator, name="warehouse-navigator"),

    path('processserialno/', views.process_serial_no,name="process-serial-no"),


    


    # common Routes
    path('', views.dashboard , name = 'dashboard-main'),
    path('exceldownloadproduction/<str:module_name>/<int:pk>', views.excel_download_production, name ='excel-download-production'),

    path('producttoitemajax/', views.product_2_item_ajax, name='product-2-item-ajax'),
    path('refnosearchajax/', views.ref_no_search_ajax, name='ref_no_search_ajax'),
    path('partynamesearchajax/', views.party_name_search_ajax, name='party-name-search_ajax'),

    # testing
    path('testsession/', views.session_data_test, name='test-session'),

    # purchase order for rawmaterial
    path('purchaseorderforpuchasevoucherrmcreateupdate/', views.purchase_order_for_puchase_voucher_rm_create_update, name = 'purchase-order-for-puchase-voucher-rm-create-update'),
    path('purchaseorderforpuchasevoucherrmcreateupdate/<int:p_id>/', views.purchase_order_for_puchase_voucher_rm_create_update, name = 'purchase-order-for-puchase-voucher-rm-create-update'),
    path('purchaseorderforpuchasevoucherrmlist/', views.purchase_order_for_puchase_voucher_rm_list, name='purchase-order-for-puchase-voucher-rm-list'),
    path('negetivestock/', views.negetive_stock, name='negetive-stock'),
    path('purchaseorderforpuchasevoucherrmdelete/<int:pk>/', views.purchase_order_for_purchase_rm_delete, name = 'purchase-order-for-puchase-voucher-rm-delete'),

    
    path('excel_download_for_purchase_order/<int:p_id>/', views.excel_download_for_purchase_order, name='excel-download-for-purchase-order'),
      

    
    path('outwardscanproductcreate/', views.outward_scan_product_create, name='outward-scan-product-create'),
    path('outwardscanproductupdate/<int:o_id>/', views.outward_scan_product_create, name='outward-scan-product-update'),
    path('outwardscanproductlist/', views.outward_scan_product_list, name='outward-scan-product-list'),
    path('outwardscanserialnoprocess/', views.outward_scan_serial_no_process, name='outward-scan-serial-no-process'),
    path('outwardpicklistnoajax/', views.outward_picklist_no_ajax, name='outward-picklist-no-ajax'),
      
    path('salereturnlist/', views.sale_return_list, name='sale-return-list'),
    path('salesreturninwardtobin/', views.sales_return_inward_to_bin, name='sales-return-inward-to-bin'),
    path('salesreturninwardtobinview/<int:r_id>/', views.sales_return_inward_to_bin, name='sales-return-inward-to-bin-view'),
    path('otwarddataforsalereturnajax/', views.otward_data_for_sale_return_ajax, name='otward-data-for-sale-return-ajax'),
    path('processserialnoforreturnsalesajax/', views.process_serial_no_for_return_sales_ajax, name='process-serial-no-for-return-sales-ajax'),
    path('returnproductwithbinajax/', views.return_product_with_bin_ajax, name='return-product-with-bin-ajax'),
    path('salesreturnvouchercreateupdate/<int:s_id>/<int:sr_id>/<int:sv_id>/<str:action>', views.sales_return_voucher_create_update, name='sales-return-voucher-create-update'),
    path('salesreturnvouchercreateupdate/<int:s_id>/<int:sr_id>/', views.sales_return_voucher_create_update, name='sales-return-voucher-create-update'),
    
    
    path('deliverychallancreate/', views.delivery_challan_create_update, name='delivery-challan-create'),
    path('deliverychallanupdate/<int:d_id>/', views.delivery_challan_create_update, name='delivery-challan-update'),
    path('deliverychallanlist/', views.delivery_challan_list, name='delivery-challan-list'),
    path('deliverychallanproductajax/', views.delivery_challan_product_ajax, name='delivery-challan-product-ajax'),
    path('deletedeliverychallan/<int:pk>/', views.delete_delivery_challan, name='delete-delivery-challan'),
    path('deliverychallanprocessforsalevoucher/', views.delivery_challan_process_for_sale_voucher, name='delivery-challan-process-for-sale-voucher'),
    path('downloaddeliverychallanpdf/<int:dc_id>',views.download_delivery_challan_pdf , name = 'download-delivery-challan-pdf'),
]