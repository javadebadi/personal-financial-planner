from rest_framework.views import APIView
from rest_framework.serializers import ModelSerializer, SerializerMethodField
from rest_framework.pagination import PageNumberPagination
from pfp.models import Transaction


class TransactionRecordsSerializer(ModelSerializer):
    inflow = SerializerMethodField()

    def get_inflow(self, obj):
        if obj.inflow == 'I':
            return 'inflow'
        elif obj.inflow == 'O':
            return 'outflow'
        else:
            return 'none'

    class Meta:
        model = Transaction
        fields = [
            'transaction_datetime',
            'amount',
            'inflow',
        ]


class TransactionRecordsAPIView(APIView):

    PAGE_SIZE = 10

    def get(self, request, bank_account_id):
        page_size = self.request.query_params.get(
            'page_size',
            TransactionRecordsAPIView.PAGE_SIZE,
            )
        transactions = self.request.user.transactions.filter(
            bank_account__bank_account_id=bank_account_id
            )
        paginator = PageNumberPagination()
        paginator.page_size = page_size
        result_page = paginator.paginate_queryset(transactions, request)
        serializer = TransactionRecordsSerializer(result_page, many=True)
        return paginator.get_paginated_response(serializer.data)
