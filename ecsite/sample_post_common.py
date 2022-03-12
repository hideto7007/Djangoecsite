import datetime
import re

from ecsite.sample_const import *
from ecsite.serializer.serializers import SampleDataSerializer
from ecsite.model.request_models import SampleData


def value_check(value):
    """
    　　値チェック
       --------
    　　value_checkの説明
       値があれば真、無ければ偽
    """

    valid = True
    if value is None or len(value) == 0:
        valid = False

    return valid


def valid_date(value, required):
    """
       妥当性チェック
    -------
    required: boolean
       True = 必須/False = 任意

    -------
    """

    valid = False
    # 任意項目かつ入力値が入っていれば返す
    if not required and value_check(value):
        valid = True

    # 必須項目かつ入力値が入っている場合
    if required and value_check(value):
        valid = True

    return valid


def valid_date_digit_int(value, required, min, max):
    """
       整数一桁からの妥当性チェック
       -------
       required: boolean
          True = 必須/False = 任意
    """

    valid = False
    # 任意項目かつ入力値が入っていれば返す
    if not required and value_check(value):
        if re.match(r"^[0-9]*$", value) is not None:
            val = int(value)
            if min <= val <= max:
                valid = True

    # 必須項目かつ入力値が入っている場合
    if required and value_check(value):
        if re.match(r"^[0-9]*$", value) is not None:
            val = int(value)
            if min <= val <= max:
                valid = True

    return valid


def valid_date_double_digit_int(value, required, min, max):
    """
       整数二桁からの妥当性チェック
       -------
       required: boolean
          True = 必須/False = 任意
    """

    valid = False
    # 任意項目かつ入力値が入っていれば返す
    if not required and value_check(value):
        if re.match(r"^[1-9][0-9]*$", value) is not None:
            val = int(value)
            if min <= val <= max:
                valid = True

    # 必須項目かつ入力値が入っている場合
    if required and value_check(value):
        if re.match(r"^[1-9][0-9]*$", value) is not None:
            val = int(value)
            if min <= val <= max:
                valid = True

    return valid


def valid_float(value, required, min, max):
    """小数点を含むバリデーションチェック"""

    valid = False
    # 任意項目かつ入力値が入っていれば返す
    if not required and value_check(value):
        if re.match(r"^[+]?[0-9]*[.]?[0-9]+$", value) is not None:
            val = float(value)
            if min <= val <= max:
                valid = True

    # 必須項目かつ入力値が入っている場合
    if required and value_check(value):
        if re.match(r"^[+]?[0-9]*[.]?[0-9]+$", value) is not None:
            val = float(value)
            if min <= val <= max:
                valid = True

    return valid


def valid_str(value, required):
    """半角整数以外のバリデーションチェック"""

    valid = False
    # 任意項目かつ入力値が入っている場合
    if not required and value_check(value):
        valid = True

    # 必須項目かつ入力値が入っている場合
    if required and value_check(value):
        valid = True
    return valid


def entry_column_validate(column_name, required, column_value):
    """登録項目のバリデーション"""

    msg = ""
    if DataColumnName.ID.value == column_name:
        min = 0
        max = 999
        if not valid_date_digit_int(column_value, required, min, max):
            msg = "{}は{}～{}で設定してください".format(COLUMN_NAME_DIC[column_name], min, max)
    elif DataColumnName.CODE1.value == column_name:
        min = 10
        max = 100
        if not valid_date_double_digit_int(column_value, required, min, max):
            msg = "{}は{}～{}で設定してください".format(COLUMN_NAME_DIC[column_name], min, max)
    elif DataColumnName.CODE2.value == column_name:
        min = 10
        max = 200
        if not valid_date_double_digit_int(column_value, required, min, max):
            msg = "{}は{}～{}で設定してください".format(COLUMN_NAME_DIC[column_name], min, max)
    elif DataColumnName.CODE3.value == column_name:
        min = 10
        max = 300
        if not valid_float(column_value, required, min, max):
            msg = "{}は{}～{}で設定してください".format(COLUMN_NAME_DIC[column_name], min, max)
    elif DataColumnName.CODE4.value == column_name:
        min = 10
        max = 400
        if not valid_float(column_value, required, min, max):
            msg = "{}は{}～{}で設定してください".format(COLUMN_NAME_DIC[column_name], min, max)
    elif DataColumnName.SAMPLE3.value == column_name:
        if not valid_str(column_value, required):
            msg = "{}で設定してください".format(COLUMN_NAME_DIC[column_name])
    return msg


def check_valid_sample_request(request):
    """sampleデータ登録内容が妥当かどうかチェックする"""

    result_array = []
    if not request.data[RequestDateType.ENTRY_DATA.value] and value_check(
            request.data[RequestDateType.PARAM_ID.value]):
        return result_array.append("パラメータ番号が設定されてません")

    line_cnt = 1
    # for rec in request.data[RequestDateType.ENTRY_DATA.value]["detail"]: # Debug用
    for rec in request.data[RequestDateType.ENTRY_DATA.value]:
        if DataColumnName.SAMPLE1.value in rec:
            # sample1のvalue値取得
            sample_value = rec[DataColumnName.SAMPLE1.value]
            # プルダウン毎の有効データ取得
            if sample_value is not None:
                for chk_dic in ENABLE_COLUMNS_DIC[int(sample_value)]:
                    chk_key_name = chk_dic[RequiredKeyType.KEY.value]
                    if chk_key_name not in rec:
                        result_array.append("{}行目 必須項目 {} が未設定です".format(
                            line_cnt, COLUMN_NAME_DIC[chk_key_name]
                        ))
                    else:
                        required = chk_dic[RequiredKeyType.REQUIRED.value]
                        result = entry_column_validate(
                            chk_key_name, required, rec[chk_key_name]
                        )
                        if 0 < len(result):
                            result_array.append("{} 行目 {}".format(line_cnt, result))
            else:
                line_cnt = line_cnt + 1
                result_array.append("{}行目 sample1が異常です".format(line_cnt))


        return result_array


def get_sample_enum(post_value):
    """
       requestで送信されたsample1に対応したEnumを返す
       -------
       対応したEnum。未指定、該当なしならNone
    """
    enum_value = None
    if post_value is not None:
        for chk in Sample1Kind:
            if str(chk.value) == post_value:
                enum_value = chk
                break

    return enum_value


def db_insert_sampledata_request(request):
    """sampleデータをdbに登録する"""

    result = []
    # for index, rec in enumerate(request.data[RequestDateType.ENTRY_DATA.value]["detail"]): # Debug用
    for index, rec in enumerate(request.data[RequestDateType.ENTRY_DATA.value]):
        if DataColumnName.SAMPLE1.value in rec:
            # 処理対象行のみDB登録実施
            sample_value = get_sample_enum(rec[DataColumnName.SAMPLE1.value])
            # 共通項目の設定
            entry_data_dic = {}
            # 登録用データに変換
            # replace_dic = request.data[RequestDateType.ENTRY_DATA.value]["detail"][index] # Debug用
            replace_dic = request.data[RequestDateType.ENTRY_DATA.value][index]
            for dic in replace_dic:
                if replace_dic.get(dic):
                    entry_data_dic[dic] = replace_dic.get(dic)
            # sample1の名称を取得
            entry_data_dic["sample1"] = SAMPLE1_PULLDOWN[sample_value.value][Sample1PulldownResposeType.KEY.value]
            # フラグ取得
            entry_data_dic["delete_flag"] = "0"
            # ユーザー名取得
            entry_data_dic["update_user"] = str(request.user)
            entry_data_dic["created_at"] = datetime.datetime.now()
            # # 1行目insert
            serializer = SampleDataSerializer(data=entry_data_dic)
            if serializer.is_valid():
                serializer.save()
                result = 0
            elif not serializer.save():
                result.append("DB登録失敗:{}".format(entry_data_dic))
            else:
                result.append(
                    "DB登録内容エラー:{} data:{}".format(serializer.errors, entry_data_dic)
                )
    return result


def db_delete_sample_request(request):
    """sampleデータ削除"""




