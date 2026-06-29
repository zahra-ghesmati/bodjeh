from app.models.admin_costs import AdminCosts
from app.models.rials_row_material_cnsumtion import (
    RialsRowMaterialCnsumtion
)
from app.models.cost_per_ton import CostPerTon
from app.models.adjusted_profit_and_loss import AdjustedProfitAndLoss
from app.models.bsc_indicators import BscIndicators
from app.models.stops import Stops
from app.models.cash_and_credit_sales import CashAndCreditSales
from app.models.some_special_uses import SomeSpecialUses
from app.models.b_t_any_gray_tone import BTAnyGrayTone
from app.models.bt_any_white_tone import BtAnyWhiteTone
from app.models.costs import Costs
from app.models.end_of_course_inventory import EndOfCourseInventory
from app.models.first_period_inventory import FirstPeriodInventory
from app.models.grays_costs import GraysCosts
from app.models.human_resource_1 import HumanResource1
from app.models.human_resource_2 import HumanResource2
from app.models.human_resource_3 import HumanResource3
from app.models.human_resource_4 import HumanResource4
from app.models.human_resource_5 import HumanResource5
from app.models.human_resource_6 import HumanResource6
from app.models.other_expenses import OtherExpenses
from app.models.overload import Overload
from app.models.production import Production
from app.models.raw_material_consumption_price import RawMaterialConsumptionPrice
from app.models.revenues import Revenues
from app.models.sale_amount import SaleAmount
from app.models.sales_income import SalesIncome
from app.models.sales_price import SalesPrice
from app.models.white_costs import WhiteCosts
from app.models.special_use_rates import SpecialUseRates
from app.models.special_uses_in_rials import SpecialUsesInRials
from app.models.standard_cogs import StandardCogs
from app.models.standard_profit_and_loss import StandardProfitAndLoss
from app.models.amount_row_material_cnsumtion import AmountRowMaterialCnsumtion


SERVICE_MAP = {
    "admin_costs": {
        "form_key": "admin_costs",
         "menu_group":
        "هزینه ها",

    "menu_title":
        "اداری و فروش",
        "model": AdminCosts,

        "dimension1_field":
            "mhl_hzynh",

        "dimension2_field":
            "ajza_hzynh_adary_mvmy_v_frvsh",

        "budget_field":
            "hzynh_adary_v_frvsh_bvdjh",

        "actual_field":
            "hzynh_adary_v_frvsh_vaghy_sal_jary",

        "template_distinct_fields": [
            "mhl_hzynh",
            "ajza_hzynh_adary_mvmy_v_frvsh"
        ],

        "meta": {
            "title": "  اداری و فروش",

            "columns": [
                {
                    "key": "dimension1",
                    "title": "محل هزینه"
                },
                {
                    "key": "dimension2",
                    "title": "اجزاء هزینه اداری عمومی و فروش "
                }
            ]
        }
    },
    "raw_material": {

        "form_key": "raw_material",
        "menu_group":"مواد اولیه",

        "menu_title":"مصرف ریالی مواد اولیه",

        "model": RialsRowMaterialCnsumtion,

        "dimension1_field":
            "mvad_avlyh",

        "dimension2_field":
            "nv_klynkrsyman",

        "budget_field":
            "mblgh_msrf_mvad_avlyh_bvdjh",

        "actual_field":
            "mblgh_msrf_mvad_avlyh_vaghy_sal_jary",

        "template_distinct_fields": [
            "mvad_avlyh",
            "nv_klynkrsyman"
        ],

        "meta": {
            "title": "مصرف ریالی مواد اولیه",

            "columns": [
                {
                    "key": "dimension1",
                    "title": "مواد اولیه"
                },
                {
                    "key": "dimension2",
                    "title": "نوع کلینکر/سیمان"
                }
            ]
        }
    },
    "cost_per_ton": {

        "form_key": "cost_per_ton",
        "menu_group":
            "بهای تمام شده",

        "menu_title":
            "بهای تمام شده هر تن",
        "model": CostPerTon,

        "dimension1_field":
            "ajza_bhay_tmam_shdh_hr_tn",

        "budget_field":
            "bhay_tmam_shdh_hr_tn_bvdjh",

        "actual_field":
            "bhay_tmam_shdh_hr_tn_vaghy_sal_jary",

        "template_distinct_fields": [
            "ajza_bhay_tmam_shdh_hr_tn"
        ],

        "meta": {
            "title": "بهای تمام شده هر تن",

            "columns": [
                {
                    "key": "dimension1",
                    "title": "اجزاء بهای تمام شده هر تن"
                }
            ]
        }
    },
    "amount_row_material_cnsumtion": {
    "form_key": "amount_row_material_cnsumtion",

    "menu_group": "مواد اولیه",

    "menu_title": "مصرف مواد اولیه (مقداری)",

    "model": AmountRowMaterialCnsumtion,

    "dimension1_field": "mvad_avlyh",

    "dimension2_field": "nv_klynkrsyman",

    "budget_field": "mghdar_msrf_mvad_avlyh_bvdjh",

    "actual_field": "mghdar_msrf_mvad_avlyh_vaghy_sal_jary",

    "template_distinct_fields": [
        "mvad_avlyh",
        "nv_klynkrsyman"
    ],

    "meta": {
        "title": "مقدار مصرف مواد اولیه",

        "columns": [
            {
                "key": "dimension1",
                "title": "مواد اولیه"
            },
            {
                "key": "dimension2",
                "title": "نوع کلینکر/سیمان"
            }
        ]
    }
},
    "adjusted_profit_and_loss": {
    "form_key": "adjusted_profit_and_loss",

    "menu_group": "سود و زیان",

    "menu_title": "سود و زیان تعدیلی",

    "model": AdjustedProfitAndLoss,

    "dimension1_field": "ajza_svd_v_zyan",

    "budget_field": "mblgh_bvdjh",

    "actual_field": "mblgh_vaghy_sal_jary",

    "template_distinct_fields": [
        "ajza_svd_v_zyan"
    ],

    "meta": {
        "title": "سود و زیان تعدیلی",

        "columns": [
            {
                "key": "dimension1",
                "title": "اجزاء سود و زیان"
            }
        ]
    }
},


"bsc_indicators": {
    "form_key": "bsc_indicators",

    "menu_group": "سایر گزارشات مالی",

    "menu_title": "شاخص های BSC",

    "model": BscIndicators,

    "dimension1_field": "شاخص_bsc",

    "budget_field": "mghdar_shakhs_bvdjh",

    "actual_field": "mghdar_shakhs_vaghy_sal_jary",

    "template_distinct_fields": [
        "شاخص_bsc"
    ],

    "meta": {
        "title": "شاخص های BSC",

        "columns": [
            {
                "key": "dimension1",
                "title": "شاخص BSC"
            }
        ]
    }
},


"stops": {
    "form_key": "stops",

    "menu_group": "تولید",

    "menu_title": "توقفات",

    "model": Stops,

    "dimension1_field": "kvrh",

    "budget_field": "myzan_sat_tvghf_bvdjh",

    "actual_field": "myzan_sat_tvghf_vaghy_sal_jary",

    "template_distinct_fields": [
        "kvrh"
    ],

    "meta": {
        "title": "توقفات",

        "columns": [
            {
                "key": "dimension1",
                "title": "کوره"
            }
        ]
    }
},


"cash_and_credit_sales": {
    "form_key": "cash_and_credit_sales",

    "menu_group": "فروش",

    "menu_title": "فروش نقدی و اعتباری",

    "model": CashAndCreditSales,

    "dimension1_field": "nv_frvsh",

    "budget_field": "frvsh_khals_bvdjh",

    "actual_field": "frvsh_khals_vaghy_sal_jary",

    "template_distinct_fields": [
        "nv_frvsh"
    ],

    "meta": {
        "title": "فروش نقدی و اعتباری",

        "columns": [
            {
                "key": "dimension1",
                "title": "نوع فروش"
            }
        ]
    }
},
"some_special_uses": {
    "form_key": "some_special_uses",

    "menu_group": "مصارف ویژه",

    "menu_title": "مصارف ویژه مقداری",

    "model": SomeSpecialUses,

    "dimension1_field": "msarf_vy_h",

    "dimension2_field": "nv_klynkrsyman",

    "budget_field": "mghdar_msarf_vy_h_bvdjh",

    "actual_field": "mghdar_msarf_vy_h_vaghy_sal_jary",

    "template_distinct_fields": [
        "msarf_vy_h",
        "nv_klynkrsyman"
    ],

    "meta": {
        "title": "مصارف ویژه مقداری",

        "columns": [
            {
                "key": "dimension1",
                "title": "مصارف ویژه"
            },
            {
                "key": "dimension2",
                "title": "نوع کلینکر/سیمان"
            }
        ]
    }
},


"bt_any_gray_tone": {
    "form_key": "bt_any_gray_tone",

    "menu_group": "بهای تمام شده",

    "menu_title": "ب ت هر تن خاکستری",

    "model": BTAnyGrayTone,

    "dimension1_field": "ajza_bhay_tmam_shdh_hr_tn_syman_khakstry",

    "budget_field": "bhay_tmam_shdh_hr_tn_bvdjh",

    "actual_field": "bhay_tmam_shdh_hr_tn_vaghy_sal_jary",

    "template_distinct_fields": [
        "ajza_bhay_tmam_shdh_hr_tn_syman_khakstry"
    ],

    "meta": {
        "title": "بهای تمام شده هر تن سیمان خاکستری",

        "columns": [
            {
                "key": "dimension1",
                "title": "اجزاء بهای تمام شده هر تن سیمان خاکستری"
            }
        ]
    }
},


"bt_any_white_tone": {
    "form_key": "bt_any_white_tone",

    "menu_group": "بهای تمام شده",

    "menu_title": "ب ت هر تن سفید",

    "model": BtAnyWhiteTone,

    "dimension1_field": "ajza_bhay_tmam_shdh_hr_tn_syman_sfyd",

    "budget_field": "bhay_tmam_shdh_hr_tn_bvdjh",

    "actual_field": "bhay_tmam_shdh_hr_tn_vaghy_sal_jary",

    "template_distinct_fields": [
        "ajza_bhay_tmam_shdh_hr_tn_syman_sfyd"
    ],

    "meta": {
        "title": "بهای تمام شده هر تن سیمان سفید",

        "columns": [
            {
                "key": "dimension1",
                "title": "اجزاء بهای تمام شده هر تن سیمان سفید"
            }
        ]
    }
},


"costs": {
    "form_key": "costs",

    "menu_group": "هزینه ها",

    "menu_title": "هزینه ها",

    "model": Costs,

    "dimension1_field": "ajza_bhay_tmam_shdh_jam",

    "budget_field": "mblgh_bvdjh",

    "actual_field": "mblgh_vaghy_sal_jary",

    "template_distinct_fields": [
        "ajza_bhay_tmam_shdh_jam"
    ],

    "meta": {
        "title": "هزینه ها",

        "columns": [
            {
                "key": "dimension1",
                "title": "اجزاء بهای تمام شده جامع"
            }
        ]
    }
},


"end_of_course_inventory": {
    "form_key": "end_of_course_inventory",

    "menu_group": "انبار",

    "menu_title": "موجودی پایان دوره",

    "model": EndOfCourseInventory,

    "dimension1_field": "nam_mhsvl_tvlydy",

    "budget_field": "mvjvdy_payan_dvrh_bvdjh",

    "actual_field": "mvjvdy_payan_dvrh_vaghy_sal_jary",

    "template_distinct_fields": [
        "nam_mhsvl_tvlydy"
    ],

    "meta": {
        "title": "موجودی پایان دوره",

        "columns": [
            {
                "key": "dimension1",
                "title": "نام محصول تولیدی"
            }
        ]
    }
},


"first_period_inventory": {
    "form_key": "first_period_inventory",

    "menu_group": "انبار",

    "menu_title": "موجودی اول دوره",

    "model": FirstPeriodInventory,

    "dimension1_field": "nam_mhsvl_tvlydy",

    "budget_field": "mvjvdy_abtday_dvrh_bvdjh",

    "actual_field": "mvjvdy_abtday_dvrh_vaghy_sal_jary",

    "template_distinct_fields": [
        "nam_mhsvl_tvlydy"
    ],

    "meta": {
        "title": "موجودی اول دوره",

        "columns": [
            {
                "key": "dimension1",
                "title": "نام محصول تولیدی"
            }
        ]
    }
},


"grays_costs": {
    "form_key": "grays_costs",

    "menu_group": "هزینه ها",

    "menu_title": "هزینه ها خاکستری",

    "model": GraysCosts,

    "dimension1_field": "ajza_bhay_tmam_shdh_syman_khakstry",

    "budget_field": "mblgh_bvdjh",

    "actual_field": "mblgh_vaghy_sal_jary",

    "template_distinct_fields": [
        "ajza_bhay_tmam_shdh_syman_khakstry"
    ],

    "meta": {
        "title": "هزینه های سیمان خاکستری",

        "columns": [
            {
                "key": "dimension1",
                "title": "اجزاء بهای تمام شده سیمان خاکستری"
            }
        ]
    }
},

"human_resource_1": {
    "form_key": "human_resource_1",

    "menu_group": "نیروی انسانی",

    "menu_title": "نیروی انسانی 1",

    "model": HumanResource1,

    "dimension1_field": "nv_ghrardad",

    "budget_field": "tdad_prsnl_bh_tfkyk_nv_ghrardad_bvdjh",

    "actual_field": "tdad_prsnl_bh_tfkyk_nv_ghrardad_vaghy_sal_jary",

    "template_distinct_fields": [
        "nv_ghrardad"
    ],

    "meta": {
        "title": "تعداد پرسنل به تفکیک نوع قرارداد",

        "columns": [
            {"key": "dimension1", "title": "نوع قرارداد"}
        ]
    }
},

"human_resource_2": {
    "form_key": "human_resource_2",

    "menu_group": "نیروی انسانی",

    "menu_title": "نیروی انسانی 2",

    "model": HumanResource2,

    "dimension1_field": "mrkz_hzynh",

    "budget_field": "tdad_prsnl_bh_tfkyk_mrkz_hzynh_bvdjh",

    "actual_field": "tdad_prsnl_bh_tfkyk_mrkz_hzynh_vaghy_sal_jary",

    "template_distinct_fields": [
        "mrkz_hzynh"
    ],

    "meta": {
        "title": "تعداد پرسنل به تفکیک مرکز هزینه",

        "columns": [
            {"key": "dimension1", "title": "مرکز هزینه"}
        ]
    }
},
"human_resource_3": {
    "form_key": "human_resource_3",

    "menu_group": "نیروی انسانی",

    "menu_title": "نیروی انسانی 3",

    "model": HumanResource3,

    "dimension1_field": "jnsyt",

    "budget_field": "tdad_prsnl_bh_tfkyk_jnsyt_bvdjh",

    "actual_field": "tdad_prsnl_bh_tfkyk_jnsyt_vaghy_sal_jary",

    "template_distinct_fields": [
        "jnsyt"
    ],

    "meta": {
        "title": "تعداد پرسنل به تفکیک جنسیت",

        "columns": [
            {"key": "dimension1", "title": "جنسیت"}
        ]
    }
},
"human_resource_4": {
    "form_key": "human_resource_4",

    "menu_group": "نیروی انسانی",

    "menu_title": "نیروی انسانی 4",

    "model": HumanResource4,

    "dimension1_field": "vzyt_nyrvy_ansany",

    "budget_field": "tdad_vrvdy_v_khrvjy_prsnl_bvdjh",

    "actual_field": "tdad_vrvdy_v_khrvjy_prsnl_vaghy_sal_jary",

    "template_distinct_fields": [
        "vzyt_nyrvy_ansany"
    ],

    "meta": {
        "title": "ورودی و خروجی پرسنل",

        "columns": [
            {"key": "dimension1", "title": "وضعیت نیروی انسانی"}
        ]
    }
},
"human_resource_5": {
    "form_key": "human_resource_5",

    "menu_group": "نیروی انسانی",

    "menu_title": "نیروی انسانی 5",

    "model": HumanResource5,

    "dimension1_field": "tfkyk_sn",

    "budget_field": "tdad_prsnl_bh_tfkyk_sn_bvdjh",

    "actual_field": "tdad_prsnl_bh_tfkyk_sn_vaghy_sal_jary",

    "template_distinct_fields": [
        "tfkyk_sn"
    ],

    "meta": {
        "title": "تعداد پرسنل به تفکیک سن",

        "columns": [
            {"key": "dimension1", "title": "تفکیک سن"}
        ]
    }
},
"human_resource_6": {
    "form_key": "human_resource_6",

    "menu_group": "نیروی انسانی",

    "menu_title": "نیروی انسانی 6",

    "model": HumanResource6,

    "dimension1_field": "myzan_thsylat",

    "budget_field": "tdad_prsnl_bh_tfkyk_thsylat_bvdjh",

    "actual_field": "tdad_prsnl_bh_tfkyk_thsylat_vaghy_sal_jary",

    "template_distinct_fields": [
        "myzan_thsylat"
    ],

    "meta": {
        "title": "تعداد پرسنل به تفکیک تحصیلات",

        "columns": [
            {"key": "dimension1", "title": "میزان تحصیلات"}
        ]
    }
},
"other_expenses": {
    "form_key": "other_expenses",

    "menu_group": "هزینه ها",

    "menu_title": "سایر هزینه ها",

    "model": OtherExpenses,

    "dimension1_field": "hzynh",

    "budget_field": "mblgh_bvdjh",

    "actual_field": "mblgh_vaghy_sal_jary",

    "template_distinct_fields": [
        "hzynh"
    ],

    "meta": {
        "title": "سایر هزینه ها",

        "columns": [
            {"key": "dimension1", "title": "هزینه"}
        ]
    }
},
"overload": {
    "form_key": "overload",

    "menu_group": "هزینه ها",

    "menu_title": "سربار",

    "model": Overload,

    "dimension1_field": "nvan_hzynh_srbar",

    "budget_field": "hzynh_srbar_bvdjh",

    "actual_field": "hzynh_srbar_vaghy_sal_jary",

    "template_distinct_fields": [
        "nvan_hzynh_srbar"
    ],

    "meta": {
        "title": "هزینه های سربار",

        "columns": [
            {"key": "dimension1", "title": "عنوان هزینه سربار"}
        ]
    }
},
"production": {
    "form_key": "production",

    "menu_group": "تولید",

    "menu_title": "تولید",

    "model": Production,

    "dimension1_field": "nam_mhsvl_tvlydy",

    "budget_field": "myzan_tvlyd_bvdjh",

    "actual_field": "myzan_tvlyd_vaghy_sal_jary",

    "template_distinct_fields": [
        "nam_mhsvl_tvlydy"
    ],

    "meta": {
        "title": "میزان تولید",

        "columns": [
            {"key": "dimension1", "title": "نام محصول تولیدی"}
        ]
    }
},
"raw_material_consumption_price": {
    "form_key": "raw_material_consumption_price",

    "menu_group": "مواد اولیه",

    "menu_title": "نرخ مصرف مواد اولیه",

    "model": RawMaterialConsumptionPrice,

    "dimension1_field": "mvad_avlyh",

    "dimension2_field": "nv_klynkrsyman",

    "budget_field": "nrkh_msrf_mvad_avlyh_bvdjh",

    "actual_field": "nrkh_msrf_mvad_avlyh_vaghy_sal_jary",

    "template_distinct_fields": [
        "mvad_avlyh",
        "nv_klynkrsyman"
    ],

    "meta": {
        "title": "نرخ مصرف مواد اولیه",

        "columns": [
            {"key": "dimension1", "title": "مواد اولیه"},
            {"key": "dimension2", "title": "نوع کلینکر/سیمان"}
        ]
    }
},
"revenues": {
    "form_key": "revenues",

    "menu_group": "فروش",

    "menu_title": "درآمدها",

    "model": Revenues,

    "dimension1_field": "dramd",

    "dimension2_field": "nv_dramd",

    "budget_field": "dramd_khals_bvdjh",

    "actual_field": "dramd_khals_vaghy_sal_jary",

    "template_distinct_fields": [
        "dramd",
        "nv_dramd"
    ],

    "meta": {
        "title": "درآمدها",

        "columns": [
            {"key": "dimension1", "title": "درآمد"},
            {"key": "dimension2", "title": "نوع درآمد"}
        ]
    }
}

,
"sale_amount": {
    "form_key": "sale_amount",

    "menu_group": "فروش",

    "menu_title": "فروش مقداری",

    "model": SaleAmount,

    "dimension1_field": "nam_mhsvl_frvsh",

    "dimension2_field": "nv_frvsh",

    "budget_field": "frvsh_mghdary_bvdjh",

    "actual_field": "frvsh_mghdary_vaghy_sal_jary",

    "template_distinct_fields": [
        "nam_mhsvl_frvsh",
        "nv_frvsh"
    ],

    "meta": {
        "title": "فروش مقداری",

        "columns": [
            {"key": "dimension1", "title": "نام محصول فروش"},
            {"key": "dimension2", "title": "نوع فروش"}
        ]
    }
}
,
"sales_income": {
    "form_key": "sales_income",

    "menu_group": "فروش",

    "menu_title": "فروش خالص ریالی",

    "model": SalesIncome,

    "dimension1_field": "nam_mhsvl_frvsh",

    "dimension2_field": "nv_frvsh",

    "budget_field": "frvsh_khals_ryaly_bvdjh",

    "actual_field": "frvsh_khals_ryaly_vaghy_sal_jary",

    "template_distinct_fields": [
        "nam_mhsvl_frvsh",
        "nv_frvsh"
    ],

    "meta": {
        "title": "فروش خالص ریالی",

        "columns": [
            {"key": "dimension1", "title": "نام محصول فروش"},
            {"key": "dimension2", "title": "نوع فروش"}
        ]
    }
},
"sales_price": {
    "form_key": "sales_price",

    "menu_group": "فروش",

    "menu_title": "نرخ فروش",

    "model": SalesPrice,

    "dimension1_field": "nam_mhsvl_frvsh",

    "dimension2_field": "nv_frvsh",

    "budget_field": "nrkh_frvsh_bvdjh",

    "actual_field": "nrkh_frvsh_vaghy_sal_jary",

    "template_distinct_fields": [
        "nam_mhsvl_frvsh",
        "nv_frvsh"
    ],

    "meta": {
        "title": "نرخ فروش",

        "columns": [
            {"key": "dimension1", "title": "نام محصول فروش"},
            {"key": "dimension2", "title": "نوع فروش"}
        ]
    }
},
"white_costs": {
    "form_key": "white_costs",

    "menu_group": "هزینه ها",

    "menu_title": "هزینه ها سفید",

    "model": WhiteCosts,

    "dimension1_field": "ajza_bhay_tmam_shdh_syman_sfyd",

    "budget_field": "mblgh_bvdjh",

    "actual_field": "mblgh_vaghy_sal_jary",

    "template_distinct_fields": [
        "ajza_bhay_tmam_shdh_syman_sfyd"
    ],

    "meta": {
        "title": "هزینه های سیمان سفید",

        "columns": [
            {
                "key": "dimension1",
                "title": "اجزاء بهای تمام شده سیمان سفید"
            }
        ]
    }
},
"special_use_rates": {
    "form_key": "special_use_rates",

    "menu_group": "مصارف ویژه",

    "menu_title": "نرخ مصارف ویژه",

    "model": SpecialUseRates,

    "dimension1_field": "msarf_vy_h",

    "dimension2_field": "nv_klynkrsyman",

    "budget_field": "nrkh_msarf_vy_h_bvdjh",

    "actual_field": "nrkh_msarf_vy_h_vaghy_sal_jary",

    "template_distinct_fields": [
        "msarf_vy_h",
        "nv_klynkrsyman"
    ],

    "meta": {
        "title": "نرخ مصارف ویژه",

        "columns": [
            {"key": "dimension1", "title": "مصارف ویژه"},
            {"key": "dimension2", "title": "نوع کلینکر/سیمان"}
        ]
    }
},
"special_uses_in_rials": {
    "form_key": "special_uses_in_rials",

    "menu_group": "مصارف ویژه",

    "menu_title": "مصارف ویژه ریالی",

    "model": SpecialUsesInRials,

    "dimension1_field": "msarf_vy_h",

    "dimension2_field": "nv_klynkrsyman",

    "budget_field": "mblgh_msarf_vy_h_bvdjh",

    "actual_field": "mblgh_msarf_vy_h_vaghy_sal_jary",

    "template_distinct_fields": [
        "msarf_vy_h",
        "nv_klynkrsyman"
    ],

    "meta": {
        "title": "مصارف ویژه (ریالی)",

        "columns": [
            {"key": "dimension1", "title": "مصارف ویژه"},
            {"key": "dimension2", "title": "نوع کلینکر/سیمان"}
        ]
    }
},
"standard_cogs": {
    "form_key": "standard_cogs",

    "menu_group": "بهای تمام شده",

    "menu_title": "بهای تمام شده استاندارد",

    "model": StandardCogs,

    "dimension1_field": "ajza_bhay_tmam_shdh_astandard",

    "budget_field": "mblgh_bvdjh",

    "actual_field": "mblgh_vaghy_sal_jary",

    "template_distinct_fields": [
        "ajza_bhay_tmam_shdh_astandard"
    ],

    "meta": {
        "title": "بهای تمام شده استاندارد",

        "columns": [
            {
                "key": "dimension1",
                "title": "اجزاء بهای تمام شده استاندارد"
            }
        ]
    }
},
"standard_profit_and_loss": {
    "form_key": "standard_profit_and_loss",

    "menu_group": "سود و زیان",

    "menu_title": "سود و زیان استاندارد",

    "model": StandardProfitAndLoss,

    "dimension1_field": "ajza_svd_v_zyan",

    "budget_field": "mblgh_bvdjh",

    "actual_field": "mblgh_vaghy_sal_jary",

    "template_distinct_fields": [
        "ajza_svd_v_zyan"
    ],

    "meta": {
        "title": "سود و زیان استاندارد",

        "columns": [
            {
                "key": "dimension1",
                "title": "اجزاء سود و زیان"
            }
        ]
    }
}

}