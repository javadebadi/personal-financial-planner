from pfp.views import AssetsListView
from rest_framework.views import APIView
from rest_framework.response import Response
from pfp.models import (
    Asset,
    AssetCategory,
    AssetSubCategory,
)
from rest_framework import serializers
from pfp.business_rules.asset import AssetBR
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from rest_framework.pagination import PageNumberPagination
from pfp.business_rules.asset import AssetListSerializer




@method_decorator(csrf_exempt, name='dispatch')
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

class AssetSubCategoryCreateAPIView(APIView):

    def post(self, request):
        br = AssetBR(user=request.user)
        category_id = request.data['category_id']
        name = request.data['name']
        result = br.add_subcategory(
            category=category_id,
            name=name,
        )
        return Response(
            data={
                "result": result,
                "detail": "Subcategory added successfully!",
            },
            status=201,
        )

class AssetSubCategoryDeleteAPIView(APIView):

    def delete(self, request, pk):
        br = AssetBR(user=request.user)
        br.delete_subcategory(asset_subcategory_id=pk)
        return Response(
            data={
                "result":  {"asset_subcategory_id": pk},
                "detail": "Subcategory deleted successfully!",
            },
            status=200,
        )

class AssetsCreateAPIView(APIView):

    def post(self, request):
        br = AssetBR(user=request.user)
        record = br.add(
            sub_category_id=request.data.get('asset_sub_category_id'),
            amount=request.data.get('amount'),
            unit_value=request.data.get('unit_value'),
            unit_value_currency_code=request.data.get('unit_value_currency_code'),
        )
        return Response(
            data={
            "result": "OK",
            "detail": record,
            }
        )

class AssetsListAPIView(APIView):

    PAGE_SIZE = 1000

    def get(self, request):
        page_size = self.request.query_params.get(
            'page_size',
            AssetsListAPIView.PAGE_SIZE,
            )

        br = AssetBR(user=request.user)
        assets_list_queryset = br.get_queryset()

        paginator = PageNumberPagination()
        paginator.page_size = page_size
        result_page = paginator.paginate_queryset(assets_list_queryset, request)
        serializer = AssetListSerializer(result_page, many=True)
        print(paginator.get_paginated_response(serializer.data).data)
        data = paginator.get_paginated_response(serializer.data).data
        data.update({"detail": "Get list of assets successfully"})

        return Response(
            data=data,
            status=200,
        )


