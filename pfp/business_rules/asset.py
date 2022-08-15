from rest_framework import serializers
from django.contrib.auth import get_user_model
from pfp.models import (
    AssetCategory,
    AssetSubCategory,
    Asset,
    Currency,
)
User = get_user_model()


class AssetSubCategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = AssetSubCategory
        fields = ['asset_subcategory_id', 'name', 'category']
        depth = 0


class AssetCategorySerializer(serializers.ModelSerializer):
    subcategories = AssetSubCategorySerializer(many=True, read_only=False)

    class Meta:
        model = AssetCategory
        fields = ['asset_category_id', 'name', 'subcategories']
        depth = 1

class AssetSerializer(serializers.ModelSerializer):

    class Meta:
        model = Asset
        fields = "__all__"
        depth = 1


class AssetBR:

    def __init__(
        self,
        user: User,
        ) -> None:
        self.user = user

    @property
    def user(self) -> User:
        return self._user

    @user.setter
    def user(self, user: User) -> None:
        assert isinstance(user, User)
        self._user = user

    def get_categories(self):
        """Returns asset categories of user


        Example
        -------
        >>> br = AssetBR(user=User.objects.get(pk=1))
        >>> br.get_categories()
        [
            {
                "asset_category_id": 117,
                "name": "Cash",
                "subcategories": [
                    {
                        "asset_subcategory_id": 476,
                        "name": "Cash"
                    },
                    {
                        "asset_subcategory_id": 477,
                        "name": "Checking Account"
                    },
                    {
                        "asset_subcategory_id": 478,
                        "name": "Saving Account"
                    },
                    {
                        "asset_subcategory_id": 479,
                        "name": "Money Market Account"
                    },
                    {
                        "asset_subcategory_id": 480,
                        "name": "Certificates of Deposit (CDs)"
                    },
                    {
                        "asset_subcategory_id": 481,
                        "name": "U.S. government Treasury bill"
                    }
                ]
            },
            {
                "asset_category_id": 118,
                "name": "Personal Property",
                "subcategories": [
                    {
                        "asset_subcategory_id": 482,
                        "name": "Cars"
                    },
                    {
                        "asset_subcategory_id": 483,
                        "name": "Boats"
                    },
                    {
                        "asset_subcategory_id": 484,
                        "name": "Art"
                    },
                    {
                        "asset_subcategory_id": 485,
                        "name": "Jewelry"
                    },
                    {
                        "asset_subcategory_id": 486,
                        "name": "Collections"
                    },
                    {
                        "asset_subcategory_id": 487,
                        "name": "Computers"
                    },
                    {
                        "asset_subcategory_id": 488,
                        "name": "Phones"
                    },
                    {
                        "asset_subcategory_id": 489,
                        "name": "TVs"
                    },
                    {
                        "asset_subcategory_id": 490,
                        "name": "Other stuff"
                    }
                ]
            },
            {
                "asset_category_id": 119,
                "name": "Real Estate",
                "subcategories": [
                    {
                        "asset_subcategory_id": 491,
                        "name": "Residental Land"
                    },
                    {
                        "asset_subcategory_id": 492,
                        "name": "Residental Building"
                    },
                    {
                        "asset_subcategory_id": 493,
                        "name": "Commercial Land"
                    },
                    {
                        "asset_subcategory_id": 494,
                        "name": "Commercial Building"
                    }
                ]
            },
            {
                "asset_category_id": 120,
                "name": "Investment",
                "subcategories": [
                    {
                        "asset_subcategory_id": 495,
                        "name": "Stocks"
                    },
                    {
                        "asset_subcategory_id": 496,
                        "name": "Bonds"
                    },
                    {
                        "asset_subcategory_id": 497,
                        "name": "Annuities"
                    },
                    {
                        "asset_subcategory_id": 498,
                        "name": "Mutual Funds"
                    },
                    {
                        "asset_subcategory_id": 499,
                        "name": "Exchange-Traded Funds (ETF)"
                    },
                    {
                        "asset_subcategory_id": 500,
                        "name": "Cryptocurrency"
                    }
                ]
            }
            ],
        
        """
        assets_categories = AssetCategory.objects.filter(user=self.user)
        serializer = AssetCategorySerializer(assets_categories, many=True)
        return serializer.data

    def add_subcategory(
        self,
        category: AssetCategory,
        name: str,
        ) -> None:
        """
        Parameters
        ----------
        category: AssetCategory
            category is either AssetCategory object or integer that determines
            an asset category
        name : str
            name of the subcategory

        """
        if isinstance(category, AssetCategory):
            assert category.user == self.user
        elif type(category) == int:
            category = AssetCategory.objects.get(user=self.user, pk=category)

        subcategory = AssetSubCategory()
        subcategory.name = name
        subcategory.user = self.user
        subcategory.category = category
        subcategory.save()
        return AssetSubCategorySerializer(subcategory, many=False).data

    def delete_subcategory(
        self,
        asset_subcategory_id,
        ) -> None:
        AssetSubCategory.objects.get(
            user=self.user,
            asset_subcategory_id=asset_subcategory_id
            ).delete()
        return None

    def add(
        self,
        sub_category_id: int,
        amount: float,
        unit_value: float,
        unit_value_currency_code: str,
        ):
        """Adds new Asset to Asset table
        """
        a = Asset()
        a.amount = amount
        a.sub_category = AssetSubCategory.objects.get(pk=sub_category_id)
        a.category = a.sub_category.category
        a.unit_value_currency_code = Currency.objects.get(code=unit_value_currency_code)
        a.user = self.user
        a.unit_value = unit_value
        a.save()
        return AssetSerializer(a, many=False).data
        