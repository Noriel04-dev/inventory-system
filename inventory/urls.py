from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('docs/', views.docs_view, name='docs'),
    path('docs/print/', views.print_doc_view, name='print_doc'),
    path('docs/save/', views.save_doc_item, name='save_doc_item'),

    # Specific inventory routes BEFORE the wildcard category route
    path('inventory/', views.inventory_list, name='inventory_list'),
    path('inventory/export/excel/', views.export_excel, name='export_excel'),
    path('inventory/import-export/', views.import_export, name='import_export'),
    path('inventory/upload/excel/', views.upload_excel, name='upload_excel'),
    path('inventory/download/template/', views.download_excel_template, name='download_excel_template'),
    path('inventory/delete-all/', views.delete_all_items, name='delete_all_items'),

    # Wildcard category routes (must come AFTER specific routes)
    path('inventory/<str:category>/', views.inventory_list, name='inventory_by_category'),
    path('inventory/<str:category>/<str:classification>/', views.inventory_list, name='inventory_by_classification'),

    # Item CRUD
    path('item/add/', views.add_item, name='add_item'),
    path('item/<int:pk>/edit/', views.edit_item, name='edit_item'),
    path('item/<int:pk>/get/', views.get_item, name='get_item'),
    path('item/<int:pk>/delete/', views.delete_item, name='delete_item'),

    # Barcode
    path('item/<int:pk>/barcode/', views.barcode_view, name='barcode_view'),
    path('barcode/scan/', views.barcode_scan, name='barcode_scan'),

    # Import history
    path('import-history/', views.import_history, name='import_history'),
    path('import-history/<str:batch_id>/delete/', views.delete_import_batch, name='delete_import_batch'),
]
