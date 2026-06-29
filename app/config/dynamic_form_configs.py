# 8 فرم
from app.models.accounts_and_documents_receivable import AccountsAndDocumentsReceivable
from app.models.balance_sheet import BalanceSheet
from app.models.bank_facilities import BankFacilities
from app.models.cash_flow import CashFlow
from app.models.raccounts import Raccounts
from app.models.salary import Salary
from app.models.summary_of_other_receivables import SummaryOfOtherReceivables
from app.models.summary_of_receivables import SummaryOfReceivables

SERVICE_MAP = {
    "balance_sheet": {
    "type": "dynamic",

    "form_key": "balance_sheet",

    "menu_group": "سایر گزارشات مالی",
    "menu_title": "ترازنامه جامع",

    "model": BalanceSheet,

    "columns": [
        {
            "field": "shrh",
            "title": "شرح",
            "editable": False,
            "type": "text"
        },
        {
            "field": "tbghh_bndy",
            "title": "طبقه بندی",
            "editable": False,
            "type": "text"
        },
        {
            "field": "dr_tarykh_payan_mah_sal_jary",
            "title": "در تاریخ پایان ماه سال جاری",
            "editable": True,
            "type": "number"
        },
        {
            "field": "dr_tarykh_payan_mah_sal_ghbl",
            "title": "در تاریخ پایان ماه سال قبل",
            "editable": True,
            "type": "number"
        }
    ],

    "template_distinct_fields": [
        "shrh",
        "tbghh_bndy"
    ],

    "meta": {
        "title": "ترازنامه جامع"
    },
    "approval": {"type": "single"}
},
"summary_of_receivables": {
    "type": "dynamic",

    "form_key": "summary_of_receivables",

    "menu_group": "حساب های دریافتنی",
    "menu_title": "خلاصه دریافتنی ها",

    "model": SummaryOfReceivables,

    "columns": [
        {
            "field": "shrh",
            "title": "شرح",
            "editable": False,
            "type": "text"
        },
        {
            "field": "abtday_sal_maly_jary",
            "title": "ابتدای سال مالی جاری",
            "editable": True,
            "type": "number"
        },
        {
            "field": "payan_mah_jary",
            "title": "پایان ماه جاری",
            "editable": True,
            "type": "number"
        },
        {
            "field": "payan_mah_jary_sal_ghbl",
            "title": "پایان ماه جاری سال قبل",
            "editable": True,
            "type": "number"
        }
    ],

    "template_distinct_fields": [
        "shrh"
    ],

    "meta": {
        "title": "خلاصه دریافتنی ها"
    },
    "approval": {"type": "single"}
},
"summary_of_other_receivables": {
    "type": "dynamic",

    "form_key": "summary_of_other_receivables",

    "menu_group": "حساب های دریافتنی",
    "menu_title": "سایر دریافتنی ها",

    "model": SummaryOfOtherReceivables,

    "columns": [
        {
            "field": "shrh",
            "title": "شرح",
            "editable": False,
            "type": "text"
        },
        {
            "field": "nv_hsab",
            "title": "نوع حساب",
            "editable": False,
            "type": "text"
        },
        {
            "field": "abtday_sal_maly_jary",
            "title": "ابتدای سال مالی جاری",
            "editable": True,
            "type": "number"
        },
        {
            "field": "payan_mah_jary",
            "title": "پایان ماه جاری",
            "editable": True,
            "type": "number"
        },
        {
            "field": "payan_mah_jary_sal_ghbl",
            "title": "پایان ماه جاری سال قبل",
            "editable": True,
            "type": "number"
        }
    ],

    "template_distinct_fields": [
        "shrh",
        "nv_hsab"
    ],

    "meta": {
        "title": "خلاصه سایر دریافتنی ها"
    },
    "approval": {"type": "single"}
},
"accounts_and_documents_receivable": {
    "type": "dynamic",
    "form_key": "accounts_and_documents_receivable",
    "menu_group": "حساب های دریافتنی",
    "menu_title": "حسابها و اسناد دریافتنی",
    "allow_add_rows": True,
    "load_template_if_empty": False,
    "model": AccountsAndDocumentsReceivable,
    "columns": [
        {
            "field": "bdhkar",
            "title": "بدهکار",
            "editable": True,
            "type": "text"
        },
        {
            "field": "mblgh_asnad_dryaftny_srrsyd_shdh",
            "title": "مبلغ اسناد دریافتنی سررسید شده",
            "editable": True,
            "type": "number"
        },
        {
            "field": "mblgh_asnad_dryaftny_srrsyd_nshdh",
            "title": "مبلغ اسناد دریافتنی سررسید نشده",
            "editable": True,
            "type": "number"
        },
        {
            "field": "mjmv_asnad_dryaftny",
            "title": "مجموع اسناد دریافتنی",
            "editable": True,
            "type": "number"
        },
        {
            "field": "mblgh_hsab_dryaftny",
            "title": "مبلغ حساب دریافتنی",
            "editable": True,
            "type": "number"
        },
        {
            "field": "mjmv_hsabha_v_asnad_dryaftny",
            "title": "مجموع حسابها و اسناد دریافتنی",
            "editable": True,
            "type": "number"
        }
    ],
    "template_distinct_fields": [
        "bdhkar"
    ],
    "meta": {
        "title": "حسابها و اسناد دریافتنی"
    },
    "approval": {"type": "single"}
},
"r_accounts": {
    "type": "dynamic",
    "form_key": "r_accounts",
    "menu_group": "حساب های دریافتنی",
    "menu_title": "مطالبات",
    "model": Raccounts,
    "columns": [
        {
            "field": "mjmv_hsabha_v_asnad_dryaftny_tjary_v_ghyr_tjary_vaghy_sal_jary",
            "title": "مجموع حسابها و اسناد دریافتنی تجاری و غیر تجاری - واقعی سال جاری",
            "editable": True,
            "type": "number",
            "width": "250px" # اضافه کردن عرض برای جلوگیری از تداخل
        },
        {
            "field": "mandh_hsabha_v_asnad_dryaftny_tjary_vaghy_sal_jary",
            "title": "مانده حسابها و اسناد دریافتنی تجاری - واقعی سال جاری",
            "editable": True,
            "type": "number",
            "width": "200px"
        },
        {
            "field": "mandh_hsabha_v_asnad_dryaftny_ghyr_tjary_vaghy_sal_jary",
            "title": "مانده حسابها و اسناد دریافتنی غیر تجاری - واقعی سال جاری",
            "editable": True,
            "type": "number",
            "width": "200px"
        },
        {
            "field": "mblgh_tlb_az_rvh_vaghy_sal_jary",
            "title": "مبلغ طلب از گروه - واقعی سال جاری",
            "editable": True,
            "type": "number",
            "width": "150px"
        },
        {
            "field": "mblgh_tlb_kharj_az_rvh_vaghy_sal_jary",
            "title": "مبلغ طلب خارج از گروه - واقعی سال جاری",
            "editable": True,
            "type": "number",
            "width": "150px"
        }
    ],
    "meta": {
        "title": "مطالبات"
    },
    "approval": {"type": "single"}
},
"salary": {
    "type": "dynamic",
    "form_key": "salary",
    "menu_group": "نیروی انسانی",
    "menu_title": "دستمزد",
    "model": Salary,
    "columns": [
        # ستون کلیدی (شرح)
        {"field": "ajza_hzynh_prsnly", "title": "اجزاء هزینه پرسنلی", "editable": False, "type": "text"},
        
        # بخش مقادیر واقعی
        {"field": "dstmzd_mstghym_vaghy_sal_jary", "title": "دستمزد مستقیم (واقعی)", "editable": True, "type": "number"},
        {"field": "dstmzd_srbar_vaghy_sal_jary", "title": "دستمزد سربار (واقعی)", "editable": True, "type": "number"},
        {"field": "dstmzd_adary_mvmy_vaghy_sal_jary", "title": "دستمزد اداری عمومی (واقعی)", "editable": True, "type": "number"},
        {"field": "dstmzd_frvsh_vaghy_sal_jary", "title": "دستمزد فروش (واقعی)", "editable": True, "type": "number"},
        {"field": "mjmv_dstmzd_vaghy_sal_jary", "title": "مجموع دستمزد (واقعی)", "editable": True, "type": "number"},
        
        # بخش مقادیر بودجه
        {"field": "dstmzd_mstghym_bvdjh", "title": "دستمزد مستقیم (بودجه)", "editable": True, "type": "number"},
        {"field": "dstmzd_srbar_bvdjh", "title": "دستمزد سربار (بودجه)", "editable": True, "type": "number"},
        {"field": "dstmzd_adary_mvmy_bvdjh", "title": "دستمزد اداری عمومی (بودجه)", "editable": True, "type": "number"},
        {"field": "dstmzd_frvsh_bvdjh", "title": "دستمزد فروش (بودجه)", "editable": True, "type": "number"},
        {"field": "mjmv_dstmzd_bvdjh", "title": "مجموع دستمزد (بودجه)", "editable": True, "type": "number"},
    ],
    "template_distinct_fields": ["ajza_hzynh_prsnly"],
    "meta": {
        "title": "دستمزد"
    },
    "approval": {
    "type": "double",

    "budget_fields": [
        "dstmzd_mstghym_bvdjh",
        "dstmzd_srbar_bvdjh",
        "dstmzd_adary_mvmy_bvdjh",
        "dstmzd_frvsh_bvdjh","mjmv_dstmzd_bvdjh"
    ],

    "actual_fields": [
        "dstmzd_mstghym_vaghy_sal_jary",
        "dstmzd_srbar_vaghy_sal_jary",
        "dstmzd_adary_mvmy_vaghy_sal_jary",
        "dstmzd_frvsh_vaghy_sal_jary","mjmv_dstmzd_vaghy_sal_jary"
    ]
}
},
"bank_facilities": {
    "type": "dynamic",
    "form_key": "bank_facilities",
    "menu_group": "مصارف ویژه",
    "menu_title": "تسهیلات بانکی",
    "allow_add_rows": True,
    "load_template_if_empty": False,
    "model": BankFacilities,
    "columns": [
        {"field": "nam_tamyn_knndh_tshylat", "title": "نام تأمین‌کننده", "editable": True, "type": "text", "width": "180px"},
        {"field": "nv_arz", "title": "نوع ارز", "editable": True, "type": "text"},
        {"field": "nv_ghrardad", "title": "نوع قرارداد", "editable": True, "type": "text"},
        {"field": "nrkh_tshylat", "title": "نرخ (%)", "editable": True, "type": "number"},
        
        # مانده اول دوره + مجموع
        {"field": "mandh_avl_dvrh_asl_tshylat", "title": "مانده اول (اصل)", "editable": True, "type": "number"},
        {"field": "mandh_avl_dvrh_bhrh_aty", "title": "مانده اول (بهره)", "editable": True, "type": "number"},
        {"field": "mandh_avl_dvrh_jraim_mvgh", "title": "مانده اول (جرائم)", "editable": True, "type": "number"},
        {"field": "mjmv_mandh_tshylat_abtday_dvrh", "title": "جمع مانده اول", "editable": True, "type": "number", "className": "bg-light-sum"},
        
        # پرداختی‌ها + مجموع
        {"field": "prdakhty_asl_tshylat_ty_mah", "title": "پرداخت اصل", "editable": True, "type": "number"},
        {"field": "prdakhty_svd_v_karmzd_ty_mah", "title": "پرداخت سود", "editable": True, "type": "number"},
        {"field": "prdakhty_jraim_ty_dvrh", "title": "پرداخت جرائم", "editable": True, "type": "number"},
        {"field": "mjmv_prdakhty_ty_dvrh", "title": "جمع پرداختی", "editable": True, "type": "number", "className": "bg-light-sum"},
        
        # مانده پایان دوره + مجموع
        {"field": "mandh_payan_dvrh_asl_tshylat", "title": "مانده پایان (اصل)", "editable": True, "type": "number"},
        {"field": "mandh_payan_dvrh_svd_v_karmzd", "title": "مانده پایان (سود)", "editable": True, "type": "number"},
        {"field": "mandh_payan_dvrh_jraim_mvgh", "title": "مانده پایان (جرائم)", "editable": True, "type": "number"},
        {"field": "mjmv_mandh_tshylat_payan_dvrh", "title": "جمع مانده پایان", "editable": True, "type": "number", "className": "bg-light-sum"},
        
        {"field": "tdad_aghsat_mvgh_payan_dvrh", "title": "تعداد اقساط معوق", "editable": True, "type": "number"},
        {"field": "myzan_sprdh_msdvdy", "title": "سپرده مسدودی", "editable": True, "type": "number"},
    ],
    "template_distinct_fields": ["nam_tamyn_knndh_tshylat"],
    "meta": {"title": "گزارش تسهیلات بانکی"},
    "approval": {"type": "single"}
},
"cash_flow": {
    "menu_group": "سایر گزارشات مالی",
    "menu_title": "منابع و مصارف",
    "meta": {
        "title": "منابع و مصارف",
        "type": "cash_flow",
    },
},



}