from django.urls import path
from pfp.views import (
    AssetCategoyListView,
    DashboardView,
    AssetsListView,
)
from pfp.api import (
    TransactionRecordsAPIView,
    BankAccountAPIView,
    AssetCategoyListAPIView,
    AssetsListAPIView,
    AssetSubCategoryCreateAPIView,
    AssetSubCategoryDeleteAPIView,
    AssetsCreateAPIView,
)
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('', login_required(DashboardView.as_view()), name='pfp_dashboard'),
    path('bank_account/details/<int:bank_account_id>/', login_required(BankAccountAPIView.as_view()), name='pfp_bank_account_details'),
    path('transactions/<int:bank_account_id>/', login_required(TransactionRecordsAPIView.as_view()), name='transaction_list_api'),
    path('assets_categories/list/', login_required(AssetCategoyListView.as_view()), name="assets_categories_list"),
    path('api/assets_categories/list/', login_required(AssetCategoyListAPIView.as_view()), name="assets_categories_list_api"),
    path('assets/list/', AssetsListView.as_view(), name="assets_list"),
    path('api/assets/list/', AssetsListAPIView.as_view(), name="assets_list_api"),
    path('api/assets/create/', AssetsCreateAPIView.as_view(), name="asset_create_api"),
    # [ASSET]
    # create subcategory of an Asset category
    path('assets/create/subcategory/', login_required(AssetSubCategoryCreateAPIView.as_view()), name="assets_create_subcategory_api"),
    path('api/assets/delete/subcategory/<int:pk>/', login_required(AssetSubCategoryDeleteAPIView.as_view()), name="assets_delete_subcategory_api"),
]