import datetime
import re

from originsite.sample_const import *
from originsite.sample_post_common import value_check
from originsite.serializer.serializers import SampleDataSerializer
from originsite.model.models import SampleData



def dbvalue_to_str(value):
    """db取得項目を文字列に変換して返す"""

    result = ""
    if value is not None:
        result = str(value)

    return result


def get_request_db_list(param_id_val):
    """画面表示用データ取得"""

    # 引数のバリデーション
    # 実装について
    # パラメータ値が""だった場合、クエリパラメータ不正
    # クエリパラメータが指定以外の値の場合、dataが[]で返す
    # クエリパラメータが指定の値の場合、dataの中身を返す
    if not value_check(param_id_val):
        result = "クエリパラメータが不正です"
    else:
        # DB取得
        sample_request = SampleData.objects.filter(
            param_id=param_id_val,
            delete_flag=0
        )
        result = []
        for res in SampleDataSerializer(sample_request, many=True).data:
            result.append(
                {
                    DataColumnName.ID.value: dbvalue_to_str(res["id"]),
                    DataColumnName.SAMPLE1.value: dbvalue_to_str(res["sample1"]),
                    DataColumnName.SAMPLE2.value: dbvalue_to_str(res["sample2"]),
                    DataColumnName.CODE1.value: dbvalue_to_str(res["code1"]),
                    DataColumnName.CODE2.value: dbvalue_to_str(res["code2"]),
                    DataColumnName.CODE3.value: dbvalue_to_str(res["code3"]),
                    DataColumnName.CODE4.value: dbvalue_to_str(res["code4"]),
                    DataColumnName.SAMPLE3.value: dbvalue_to_str(res["sample3"]),
                    DataColumnName.SAMPLE4.value: dbvalue_to_str(res["sample4"]),
                    DataColumnName.STATUS.value: dbvalue_to_str(res["status"]),
                }
            )

    return result





