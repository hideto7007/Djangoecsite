from rest_framework import status, views, generics, viewsets
from django.http import JsonResponse

from originsite.sample_const import *
from originsite.sample_post_common import *



class SampleDataPostListAPIView(views.APIView):
    """SampleData登録"""

    def post(self, request, *args, **kwargs):

        result_code = ApiResultKind.RESULT_SUCCESS
        detail = {}

        # バリデート一つでもエラーがあれば中断
        result_array = check_valid_sample_request(request)
        if 0 < len(result_array):
            result_code = ApiResultKind.RESULT_ERROR
            message = "バリデーションエラー"
            detail["error_list"] = result_array
        else:
            result_code = result_code
            message = "Success"

        # print(request.data[RequestDateType.ENTRY_DATA.value]) # Debug用
        if ApiResultKind.RESULT_SUCCESS == result_code:
            db_result_array = db_insert_sampledata_request(request)
            if 0 == int(db_result_array):
                message = "Success"
            elif "serializerの構文エラー" == db_result_array:
                result_code = ApiResultKind.RESULT_ERROR
                message = "例外によるDB登録エラー"
                detail = db_result_array
            else:
                result_code = ApiResultKind.RESULT_ERROR
                message = "DB登録エラー"
                detail = db_result_array

        return JsonResponse(
            {"result_code": result_code, "message": message, "detail": detail}, safe=False
        )