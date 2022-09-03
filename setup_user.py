import os
from django import setup

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'pfp_project.settings')
setup()


from pfp.models import AssetCategory
from pfp.models.asset.asset_subcategory import AssetSubCategory
from django.contrib.auth import get_user_model

User = get_user_model()

def setup_user(user_id: int):
    ASSET_CATEGORY_SUB_CATEGORY = {
        'Cash': [
            {
                'name': 'Cash',
                },
            {
                'name': 'Checking Account',
                },
            {
                'name': 'Saving Account',
                },
            {
                'name': 'Money Market Account',
                },
            {
                'name': 'Certificates of Deposit (CDs)',
                },
            {
                'name': 'U.S. government Treasury bill',
                },
        ],
        'Personal Property': [
            {
                'name': 'Cars',
                },
            {
                'name': 'Boats',
                },
            {
                'name': 'Art',
                },
            {
                'name': 'Jewelry',
                },
            {
                'name': 'Collections',
                },
            {
                'name': 'Computers',
                },
            {
                'name': 'Phones',
                },
            {
                'name': 'TVs',
                },
            {
                'name': 'Other stuff',
                },
        ],
        'Real Estate': [
            {
                'name': 'Residental Land',
                },
            {
                'name': 'Residental Building',
                },
            {
                'name': 'Commercial Land',
                },
            {
                'name': 'Commercial Building',
                },
        ],
        'Investment': [
            {
                'name': 'Stocks',
                },
            {
                'name': 'Bonds',
                },
            {
                'name': 'Annuities',
                },
            {
                'name': 'Mutual Funds',
                },
            {
                'name': 'Exchange-Traded Funds (ETF)',
                },
            {
                'name': 'Cryptocurrency',
                },
        ],
    }
    for asset_category_name in ASSET_CATEGORY_SUB_CATEGORY.keys():
        a = AssetCategory()
        a.user = User.objects.get(pk=user_id)
        a.name = asset_category_name
        a.save()


        for asset_subcategory in ASSET_CATEGORY_SUB_CATEGORY[asset_category_name]:
            b = AssetSubCategory()
            b.user = a.user
            b.name = asset_subcategory['name']
            b.category = a
            b.save()


for user_id in [user.id for user in User.objects.all()]:
    setup_user(user_id)