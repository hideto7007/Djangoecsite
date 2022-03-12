"""
API 定数定義
"""

from enum import IntEnum, Enum

class ApiResultKind(IntEnum):
    """API応答結果"""
    RESULT_SUCCESS = 0
    RESULT_ERROR = 1

class SampleRequestStatusType(IntEnum):
    """sampleデータステータス"""
    REQUEST = 0
    REQUEST_SUCCESS = 1
    REQUEST_ERROR = 2


class Sample1Kind(IntEnum):
    """サンプル1識別"""
    OPTION_1 = 0
    OPTION_2 = 1
    OPTION_3 = 2
    OPTION_4 = 3

class StatusKind(Enum):
    """サンプル1識別"""
    REGISTER = "登録済み"
    Fix = "修正中"

class StatusType(Enum):
    """サンプル1識別"""
    VALUE = "value"
    LABEL = "label"

class DataColumnName(Enum):
    """表示用カラムデータ"""
    ID = "id"
    PARAM_ID = "param_id"
    SAMPLE1 = "sample1"
    SAMPLE2 = "sample2"
    CODE1 = "code1"
    CODE2 = "code2"
    CODE3 = "code3"
    CODE4 = "code4"
    SAMPLE3 = "sample3"
    SAMPLE4 = "sample4"
    STATUS = "status"
    NUM = "num"


class Sample1PulldownResposeType(Enum):
    """サンプル1のレスポンスキー定義"""
    KEY = "key"
    VALUE = "value"

class Sample2PulldownResposeType(Enum):
    """サンプル2のレスポンスキー定義"""
    NAME = "name"
    APPLY_FOR = "apply_for"
    LIST_NUM = "list_num"
    TEST_ID = "test_id"
    TESTID = DataColumnName.NUM.value

class RequestDateType(Enum):
    """登録データ"""
    ENTRY_DATA = "data"
    PARAM_ID = "param_id"

COLUMN_NAME_DIC = {
    DataColumnName.ID.value: "id",
    DataColumnName.SAMPLE1.value: "sample1",
    DataColumnName.SAMPLE2.value: "sample2",
    DataColumnName.CODE1.value: "code1",
    DataColumnName.CODE2.value: "code2",
    DataColumnName.CODE3.value: "code3",
    DataColumnName.CODE4.value: "code4",
    DataColumnName.SAMPLE3.value: "sample3",
    DataColumnName.SAMPLE4.value: "sample4",
    DataColumnName.STATUS.value: "status",
    DataColumnName.NUM.value: "num",
}

STATUS_DIC = [
    {
        StatusType.VALUE.value: StatusKind.REGISTER.value,
        StatusType.LABEL.value: StatusKind.REGISTER.value
    },
    {
        StatusType.VALUE.value: StatusKind.Fix.value,
        StatusType.LABEL.value: StatusKind.Fix.value
    }
]

class ColumnType(Enum):
    """画面表示情報"""
    KEY = "key"
    COL = "col"
    ALIGN = "align"
    WIDTH = "width"

"""表示データカラム"""
REQUEST_COLUMNS = [
    {
        ColumnType.KEY.value: DataColumnName.ID.value,
        ColumnType.COL.value: COLUMN_NAME_DIC[DataColumnName.ID.value],
        ColumnType.ALIGN.value: "center",
        ColumnType.WIDTH.value: "125",
    },
    {
        ColumnType.KEY.value: DataColumnName.SAMPLE1.value,
        ColumnType.COL.value: COLUMN_NAME_DIC[DataColumnName.SAMPLE1.value],
        ColumnType.ALIGN.value: "center",
        ColumnType.WIDTH.value: "200",
    },
    {
        ColumnType.KEY.value: DataColumnName.SAMPLE2.value,
        ColumnType.COL.value: COLUMN_NAME_DIC[DataColumnName.SAMPLE2.value],
        ColumnType.ALIGN.value: "center",
        ColumnType.WIDTH.value: "200",
    },
    {
        ColumnType.KEY.value: DataColumnName.CODE1.value,
        ColumnType.COL.value: COLUMN_NAME_DIC[DataColumnName.CODE1.value],
        ColumnType.ALIGN.value: "center",
        ColumnType.WIDTH.value: "160",
    },
    {
        ColumnType.KEY.value: DataColumnName.CODE2.value,
        ColumnType.COL.value: COLUMN_NAME_DIC[DataColumnName.CODE2.value],
        ColumnType.ALIGN.value: "center",
        ColumnType.WIDTH.value: "160",
    },
    {
        ColumnType.KEY.value: DataColumnName.CODE3.value,
        ColumnType.COL.value: COLUMN_NAME_DIC[DataColumnName.CODE3.value],
        ColumnType.ALIGN.value: "center",
        ColumnType.WIDTH.value: "160",
    },
    {
        ColumnType.KEY.value: DataColumnName.CODE4.value,
        ColumnType.COL.value: COLUMN_NAME_DIC[DataColumnName.CODE4.value],
        ColumnType.ALIGN.value: "center",
        ColumnType.WIDTH.value: "160",
    },
    {
        ColumnType.KEY.value: DataColumnName.SAMPLE3.value,
        ColumnType.COL.value: COLUMN_NAME_DIC[DataColumnName.SAMPLE3.value],
        ColumnType.ALIGN.value: "center",
        ColumnType.WIDTH.value: "200",
    },
    {
        ColumnType.KEY.value: DataColumnName.SAMPLE4.value,
        ColumnType.COL.value: COLUMN_NAME_DIC[DataColumnName.SAMPLE4.value],
        ColumnType.ALIGN.value: "center",
        ColumnType.WIDTH.value: "200",
    },
    {
        ColumnType.KEY.value: DataColumnName.STATUS.value,
        ColumnType.COL.value: COLUMN_NAME_DIC[DataColumnName.STATUS.value],
        ColumnType.ALIGN.value: "center",
        ColumnType.WIDTH.value: "237",
    }

]

"""プルダウン1内容"""
SAMPLE1_PULLDOWN = [
    {
        Sample1PulldownResposeType.KEY.value: "Option1",
        Sample1PulldownResposeType.VALUE.value: Sample1Kind.OPTION_1.value
    },
    {
        Sample1PulldownResposeType.KEY.value: "Option2",
        Sample1PulldownResposeType.VALUE.value: Sample1Kind.OPTION_2.value
    },
    {
        Sample1PulldownResposeType.KEY.value: "Option3",
        Sample1PulldownResposeType.VALUE.value: Sample1Kind.OPTION_3.value
    },
    {
        Sample1PulldownResposeType.KEY.value: "Option4",
        Sample1PulldownResposeType.VALUE.value: Sample1Kind.OPTION_4.value
    }
]

class RequiredKeyType(Enum):
    """入力対象項目定義"""
    KEY = "key"
    REQUIRED = "required"


# sample1のプルダウン選択毎に応じた表示項目一覧(Trueは必須項目、Falseは任意項目とする)
ENABLE_COLUMNS_DIC = {
    SAMPLE1_PULLDOWN[Sample1Kind.OPTION_1.value][Sample1PulldownResposeType.VALUE.value]: [
        {
            RequiredKeyType.KEY.value: DataColumnName.ID.value,
            RequiredKeyType.REQUIRED.value: True
        },
        {
            RequiredKeyType.KEY.value: DataColumnName.SAMPLE2.value,
            RequiredKeyType.REQUIRED.value: True
        },
        {
            RequiredKeyType.KEY.value: DataColumnName.CODE1.value,
            RequiredKeyType.REQUIRED.value: True
        },
        {
            RequiredKeyType.KEY.value: DataColumnName.CODE2.value,
            RequiredKeyType.REQUIRED.value: True
        },
        {
            RequiredKeyType.KEY.value: DataColumnName.STATUS.value,
            RequiredKeyType.REQUIRED.value: True
        }
    ],
    SAMPLE1_PULLDOWN[Sample1Kind.OPTION_2.value][Sample1PulldownResposeType.VALUE.value]: [
        {
            RequiredKeyType.KEY.value: DataColumnName.ID.value,
            RequiredKeyType.REQUIRED.value: True
        },
        {
            RequiredKeyType.KEY.value: DataColumnName.SAMPLE2.value,
            RequiredKeyType.REQUIRED.value: True
        },
        {
            RequiredKeyType.KEY.value: DataColumnName.CODE3.value,
            RequiredKeyType.REQUIRED.value: True
        },
        {
            RequiredKeyType.KEY.value: DataColumnName.CODE4.value,
            RequiredKeyType.REQUIRED.value: False
        },
        {
            RequiredKeyType.KEY.value: DataColumnName.SAMPLE4.value,
            RequiredKeyType.REQUIRED.value: False
        },
        {
            RequiredKeyType.KEY.value: DataColumnName.STATUS.value,
            RequiredKeyType.REQUIRED.value: True
        }

    ],
    SAMPLE1_PULLDOWN[Sample1Kind.OPTION_3.value][Sample1PulldownResposeType.VALUE.value]: [
        {
            RequiredKeyType.KEY.value: DataColumnName.ID.value,
            RequiredKeyType.REQUIRED.value: True
        },
        {
            RequiredKeyType.KEY.value: DataColumnName.SAMPLE2.value,
            RequiredKeyType.REQUIRED.value: True
        },
        {
            RequiredKeyType.KEY.value: DataColumnName.SAMPLE3.value,
            RequiredKeyType.REQUIRED.value: False
        },
        {
            RequiredKeyType.KEY.value: DataColumnName.SAMPLE4.value,
            RequiredKeyType.REQUIRED.value: False
        },
        {
            RequiredKeyType.KEY.value: DataColumnName.STATUS.value,
            RequiredKeyType.REQUIRED.value: True
        }

    ],
    SAMPLE1_PULLDOWN[Sample1Kind.OPTION_4.value][Sample1PulldownResposeType.VALUE.value]: [
        {
            RequiredKeyType.KEY.value: DataColumnName.ID.value,
            RequiredKeyType.REQUIRED.value: True
        },
        {
            RequiredKeyType.KEY.value: DataColumnName.SAMPLE2.value,
            RequiredKeyType.REQUIRED.value: True
        },
        {
            RequiredKeyType.KEY.value: DataColumnName.CODE1.value,
            RequiredKeyType.REQUIRED.value: True
        },
        {
            RequiredKeyType.KEY.value: DataColumnName.STATUS.value,
            RequiredKeyType.REQUIRED.value: True
        }
    ]
}







