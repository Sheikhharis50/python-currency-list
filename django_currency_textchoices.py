from enum import auto

from django.db import models
from django.utils.translation import gettext as _


class Currency(models.TextField):
    ALL = auto(), _("Albania Lek")
    AFN = auto(), _("Afghanistan Afghani")
    ARS = auto(), _("Argentina Peso")
    AWG = auto(), _("Aruba Guilder")
    AUD = auto(), _("Australia Dollar")
    AZN = auto(), _("Azerbaijan New Manat")
    BSD = auto(), _("Bahamas Dollar")
    BBD = auto(), _("Barbados Dollar")
    BDT = auto(), _("Bangladeshi taka")
    BYR = auto(), _("Belarus Ruble")
    BZD = auto(), _("Belize Dollar")
    BMD = auto(), _("Bermuda Dollar")
    BOB = auto(), _("Bolivia Boliviano")
    BAM = auto(), _("Bosnia and Herzegovina Convertible Marka")
    BWP = auto(), _("Botswana Pula")
    BGN = auto(), _("Bulgaria Lev")
    BRL = auto(), _("Brazil Real")
    BND = auto(), _("Brunei Darussalam Dollar")
    KHR = auto(), _("Cambodia Riel")
    CAD = auto(), _("Canada Dollar")
    KYD = auto(), _("Cayman Islands Dollar")
    CLP = auto(), _("Chile Peso")
    CNY = auto(), _("China Yuan Renminbi")
    COP = auto(), _("Colombia Peso")
    CRC = auto(), _("Costa Rica Colon")
    HRK = auto(), _("Croatia Kuna")
    CUP = auto(), _("Cuba Peso")
    CZK = auto(), _("Czech Republic Koruna")
    DKK = auto(), _("Denmark Krone")
    DOP = auto(), _("Dominican Republic Peso")
    XCD = auto(), _("East Caribbean Dollar")
    EGP = auto(), _("Egypt Pound")
    SVC = auto(), _("El Salvador Colon")
    EEK = auto(), _("Estonia Kroon")
    EUR = auto(), _("Euro Member Countries")
    FKP = auto(), _("Falkland Islands (Malvinas) Pound")
    FJD = auto(), _("Fiji Dollar")
    GHC = auto(), _("Ghana Cedis")
    GIP = auto(), _("Gibraltar Pound")
    GTQ = auto(), _("Guatemala Quetzal")
    GGP = auto(), _("Guernsey Pound")
    GYD = auto(), _("Guyana Dollar")
    HNL = auto(), _("Honduras Lempira")
    HKD = auto(), _("Hong Kong Dollar")
    HUF = auto(), _("Hungary Forint")
    ISK = auto(), _("Iceland Krona")
    INR = auto(), _("India Rupee")
    IDR = auto(), _("Indonesia Rupiah")
    IRR = auto(), _("Iran Rial")
    IMP = auto(), _("Isle of Man Pound")
    ILS = auto(), _("Israel Shekel")
    JMD = auto(), _("Jamaica Dollar")
    JPY = auto(), _("Japan Yen")
    JEP = auto(), _("Jersey Pound")
    KZT = auto(), _("Kazakhstan Tenge")
    KPW = auto(), _("Korea (North) Won")
    KRW = auto(), _("Korea (South) Won")
    KGS = auto(), _("Kyrgyzstan Som")
    LAK = auto(), _("Laos Kip")
    LVL = auto(), _("Latvia Lat")
    LBP = auto(), _("Lebanon Pound")
    LRD = auto(), _("Liberia Dollar")
    LTL = auto(), _("Lithuania Litas")
    MKD = auto(), _("Macedonia Denar")
    MYR = auto(), _("Malaysia Ringgit")
    MUR = auto(), _("Mauritius Rupee")
    MXN = auto(), _("Mexico Peso")
    MNT = auto(), _("Mongolia Tughrik")
    MZN = auto(), _("Mozambique Metical")
    NAD = auto(), _("Namibia Dollar")
    NPR = auto(), _("Nepal Rupee")
    ANG = auto(), _("Netherlands Antilles Guilder")
    NZD = auto(), _("New Zealand Dollar")
    NIO = auto(), _("Nicaragua Cordoba")
    NGN = auto(), _("Nigeria Naira")
    NOK = auto(), _("Norway Krone")
    OMR = auto(), _("Oman Rial")
    PKR = auto(), _("Pakistan Rupee")
    PAB = auto(), _("Panama Balboa")
    PYG = auto(), _("Paraguay Guarani")
    PEN = auto(), _("Peru Nuevo Sol")
    PHP = auto(), _("Philippines Peso")
    PLN = auto(), _("Poland Zloty")
    QAR = auto(), _("Qatar Riyal")
    RON = auto(), _("Romania New Leu")
    RUB = auto(), _("Russia Ruble")
    SHP = auto(), _("Saint Helena Pound")
    SAR = auto(), _("Saudi Arabia Riyal")
    RSD = auto(), _("Serbia Dinar")
    SCR = auto(), _("Seychelles Rupee")
    SGD = auto(), _("Singapore Dollar")
    SBD = auto(), _("Solomon Islands Dollar")
    SOS = auto(), _("Somalia Shilling")
    ZAR = auto(), _("South Africa Rand")
    LKR = auto(), _("Sri Lanka Rupee")
    SEK = auto(), _("Sweden Krona")
    CHF = auto(), _("Switzerland Franc")
    SRD = auto(), _("Suriname Dollar")
    SYP = auto(), _("Syria Pound")
    TWD = auto(), _("Taiwan New Dollar")
    THB = auto(), _("Thailand Baht")
    TTD = auto(), _("Trinidad and Tobago Dollar")
    TRY = auto(), _("Turkey Lira")
    TRL = auto(), _("Turkey Lira")
    TVD = auto(), _("Tuvalu Dollar")
    UAH = auto(), _("Ukraine Hryvna")
    GBP = auto(), _("United Kingdom Pound")
    USD = auto(), _("United States Dollar")
    UYU = auto(), _("Uruguay Peso")
    UZS = auto(), _("Uzbekistan Som")
    VEF = auto(), _("Venezuela Bolivar")
    VND = auto(), _("Viet Nam Dong")
    YER = auto(), _("Yemen Rial")
    ZWD = auto(), _("Zimbabwe Dollar")
