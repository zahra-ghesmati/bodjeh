
from ..database import Base
from sqlalchemy import (
    Column,
    NVARCHAR,
    Integer,
    Float
)
class BankFacilities(Base):
    __tablename__ = "Bank Facilities"
    __table_args__ = {"schema": "Report_Main"}

    id = Column(Integer, primary_key=True, autoincrement=True)


    nam_shrkt = Column("نام شرکت", NVARCHAR(255))
    sal_maly = Column("سال مالی", NVARCHAR(255))
    mah_zarsh = Column("ماه گزارش", NVARCHAR(255))
    nam_tamyn_knndh_tshylat = Column("نام تامین کننده تسهیلات", NVARCHAR(255))
    nv_arz = Column("نوع ارز", NVARCHAR(255))
    nv_ghrardad = Column("نوع قرارداد", NVARCHAR(255))
    nrkh_tshylat = Column("نرخ تسهیلات", Float)
    mandh_avl_dvrh_asl_tshylat = Column("مانده اول دوره اصل تسهیلات", Float)
    mandh_avl_dvrh_bhrh_aty = Column("مانده اول دوره بهره آتی", Float)
    mandh_avl_dvrh_jraim_mvgh = Column("مانده اول دوره جرائم معوق", Float)
    mjmv_mandh_tshylat_abtday_dvrh = Column("مجموع مانده تسهیلات ابتدای دوره", Float)
    prdakhty_asl_tshylat_ty_mah = Column("پرداختی اصل تسهیلات طی ماه", Float)
    prdakhty_svd_v_karmzd_ty_mah = Column("پرداختی سود و کارمزد طی ماه", Float)
    prdakhty_jraim_ty_dvrh = Column("پرداختی جرائم طی دوره", Float)
    mjmv_prdakhty_ty_dvrh = Column("مجموع پرداختی طی دوره", Float)
    mandh_payan_dvrh_asl_tshylat = Column("مانده پایان دوره اصل تسهیلات", Float)
    mandh_payan_dvrh_svd_v_karmzd = Column("مانده پایان دوره سود و کارمزد", Float)
    mandh_payan_dvrh_jraim_mvgh = Column("مانده پایان دوره جرائم معوق", Float)
    mjmv_mandh_tshylat_payan_dvrh = Column("مجموع مانده تسهیلات پایان دوره", Float)
    tdad_aghsat_mvgh_payan_dvrh = Column("تعداد اقساط معوق پایان دوره", Float)
    myzan_sprdh_msdvdy = Column("میزان سپرده مسدودی", Float)
