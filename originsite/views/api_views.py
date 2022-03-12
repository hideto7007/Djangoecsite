from django.shortcuts import render, get_object_or_404
from rest_framework import views, generics, viewsets
from rest_framework.response import Response
from rest_framework.views import APIView
from django.http import JsonResponse

from originsite.model.models import SampleData
from originsite.serializer.serializers import SampleDataSerializer
from originsite.sample_const import *
from originsite.sample_get_common import *


class SampleDataListAPIView(views.APIView):
    """SampleDataの取得(一覧)・登録APIクラス"""

    def get(self, request, *args, **kwargs):
        """Sampleモデルの取得"""

        result = get_request_db_list(request.GET.get("param_id"))

        if isinstance(result, list):
            detail_dic = {"fields": REQUEST_COLUMNS,
                          "result": result,
                          "sample1_pull": SAMPLE1_PULLDOWN,
                          "enable_column_dic": ENABLE_COLUMNS_DIC,
                          "status": STATUS_DIC}
            result_code = ApiResultKind.RESULT_SUCCESS
            message = "Success"
        else:
            detail_dic = {}
            result_code = ApiResultKind.RESULT_ERROR
            message = result

        request = {"result_code": result_code, "message": message, "detail": detail_dic}

        return JsonResponse(request, safe=False)










