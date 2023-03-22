from django.db import models
from django.utils.translation import gettext as _

"""
Usage:
class ModelName:
    ...
    currency = models.CharField(
        max_length=255,
        choices=Currency.choices,
        default=Currency.USD,
    )
    ...
    
Notes

- `auto()` method will give you str value such as: AFN = "AFN", _("Afghanistan Afghani")
- To use integer values replace:
    `class Currency(models.TextChoices):` => `class Currency(models.IntegerChoices):`
"""

class Currency(models.TextChoices):
    ALL = "ALL", _("Albania Lek")
    AFN = "AFN", _("Afghanistan Afghani")
    ARS = "ARS", _("Argentina Peso")
    AWG = "AWG", _("Aruba Guilder")
    AUD = "AUD", _("Australia Dollar")
    AZN = "AZN", _("Azerbaijan New Manat")
    BSD = "BSD", _("Bahamas Dollar")
    BBD = "BBD", _("Barbados Dollar")
    BDT = "BDT", _("Bangladeshi taka")
    BYR = "BYR", _("Belarus Ruble")
    BZD = "BZD", _("Belize Dollar")
    BMD = "BMD", _("Bermuda Dollar")
    BOB = "BOB", _("Bolivia Boliviano")
    BAM = "BAM", _("Bosnia and Herzegovina Convertible Marka")
    BWP = "BWP", _("Botswana Pula")
    BGN = "BGN", _("Bulgaria Lev")
    BRL = "BRL", _("Brazil Real")
    BND = "BND", _("Brunei Darussalam Dollar")
    KHR = "KHR", _("Cambodia Riel")
    CAD = "CAD", _("Canada Dollar")
    KYD = "KYD", _("Cayman Islands Dollar")
    CLP = "CLP", _("Chile Peso")
    CNY = "CNY", _("China Yuan Renminbi")
    COP = "COP", _("Colombia Peso")
    CRC = "CRC", _("Costa Rica Colon")
    HRK = "HRK", _("Croatia Kuna")
    CUP = "CUP", _("Cuba Peso")
    CZK = "CZK", _("Czech Republic Koruna")
    DKK = "DKK", _("Denmark Krone")
    DOP = "DOP", _("Dominican Republic Peso")
    XCD = "XCD", _("East Caribbean Dollar")
    EGP = "EGP", _("Egypt Pound")
    SVC = "SVC", _("El Salvador Colon")
    EEK = "EEK", _("Estonia Kroon")
    EUR = "EUR", _("Euro Member Countries")
    FKP = "FKP", _("Falkland Islands (Malvinas) Pound")
    FJD = "FJD", _("Fiji Dollar")
    GHC = "GHC", _("Ghana Cedis")
    GIP = "GIP", _("Gibraltar Pound")
    GTQ = "GTQ", _("Guatemala Quetzal")
    GGP = "GGP", _("Guernsey Pound")
    GYD = "GYD", _("Guyana Dollar")
    HNL = "HNL", _("Honduras Lempira")
    HKD = "HKD", _("Hong Kong Dollar")
    HUF = "HUF", _("Hungary Forint")
    ISK = "ISK", _("Iceland Krona")
    INR = "INR", _("India Rupee")
    IDR = "IDR", _("Indonesia Rupiah")
    IRR = "IRR", _("Iran Rial")
    IMP = "IMP", _("Isle of Man Pound")
    ILS = "ILS", _("Israel Shekel")
    JMD = "JMD", _("Jamaica Dollar")
    JPY = "JPY", _("Japan Yen")
    JEP = "JEP", _("Jersey Pound")
    KZT = "KZT", _("Kazakhstan Tenge")
    KPW = "KPW", _("Korea (North) Won")
    KRW = "KRW", _("Korea (South) Won")
    KGS = "KGS", _("Kyrgyzstan Som")
    LAK = "LAK", _("Laos Kip")
    LVL = "LVL", _("Latvia Lat")
    LBP = "LBP", _("Lebanon Pound")
    LRD = "LRD", _("Liberia Dollar")
    LTL = "LTL", _("Lithuania Litas")
    MKD = "MKD", _("Macedonia Denar")
    MYR = "MYR", _("Malaysia Ringgit")
    MUR = "MUR", _("Mauritius Rupee")
    MXN = "MXN", _("Mexico Peso")
    MNT = "MNT", _("Mongolia Tughrik")
    MZN = "MZN", _("Mozambique Metical")
    NAD = "NAD", _("Namibia Dollar")
    NPR = "NPR", _("Nepal Rupee")
    ANG = "ANG", _("Netherlands Antilles Guilder")
    NZD = "NZD", _("New Zealand Dollar")
    NIO = "NIO", _("Nicaragua Cordoba")
    NGN = "NGN", _("Nigeria Naira")
    NOK = "NOK", _("Norway Krone")
    OMR = "OMR", _("Oman Rial")
    PKR = "PKR", _("Pakistan Rupee")
    PAB = "PAB", _("Panama Balboa")
    PYG = "PYG", _("Paraguay Guarani")
    PEN = "PEN", _("Peru Nuevo Sol")
    PHP = "PHP", _("Philippines Peso")
    PLN = "PLN", _("Poland Zloty")
    QAR = "QAR", _("Qatar Riyal")
    RON = "RON", _("Romania New Leu")
    RUB = "RUB", _("Russia Ruble")
    SHP = "SHP", _("Saint Helena Pound")
    SAR = "SAR", _("Saudi Arabia Riyal")
    RSD = "RSD", _("Serbia Dinar")
    SCR = "SCR", _("Seychelles Rupee")
    SGD = "SGD", _("Singapore Dollar")
    SBD = "SBD", _("Solomon Islands Dollar")
    SOS = "SOS", _("Somalia Shilling")
    ZAR = "ZAR", _("South Africa Rand")
    LKR = "LKR", _("Sri Lanka Rupee")
    SEK = "SEK", _("Sweden Krona")
    CHF = "CHF", _("Switzerland Franc")
    SRD = "SRD", _("Suriname Dollar")
    SYP = "SYP", _("Syria Pound")
    TWD = "TWD", _("Taiwan New Dollar")
    THB = "THB", _("Thailand Baht")
    TTD = "TTD", _("Trinidad and Tobago Dollar")
    TRY = "TRY", _("Turkey Lira")
    TRL = "TRL", _("Turkey Lira")
    TVD = "TVD", _("Tuvalu Dollar")
    UAH = "UAH", _("Ukraine Hryvna")
    GBP = "GBP", _("United Kingdom Pound")
    USD = "USD", _("United States Dollar")
    UYU = "UYU", _("Uruguay Peso")
    UZS = "UZS", _("Uzbekistan Som")
    VEF = "VEF", _("Venezuela Bolivar")
    VND = "VND", _("Viet Nam Dong")
    YER = "YER", _("Yemen Rial")
    ZWD = "ZWD", _("Zimbabwe Dollar")
