from pfp.models.asset import asset_category
from rest_framework.views import APIView
from rest_framework.response import Response
from pfp.models import (
    Asset,
    AssetCategory,
    AssetSubCategory,
)
from rest_framework import serializers
from pfp.business_rules.asset import AssetBR




class AssetCategoyListAPIView(APIView):

    def get(self, request):
        """
        Response Example
        ----------------
        HTTP 200 OK
        Allow: GET, HEAD, OPTIONS
        Content-Type: application/json
        Vary: Accept

        {
            "results": [
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
            "detail": "got user assets categories successfully"
        }
        """
        br = AssetBR(user=request.user)
        return Response(
            data={
                "results": br.get_categories(),
                "detail": "got user assets categories successfully",
                }
                )

class AssetsListAPIView(APIView):

    def get(self, request):
        return Response(
            data={
                "result": {
                    "cash": "IRR 15,876,250",
                    "gold": "IRR 120,000,000",
                    "land": "IRR 1,000,000,000",
                }
            }
        )