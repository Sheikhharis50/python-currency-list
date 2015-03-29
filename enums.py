# -*- coding: utf-8 -*-
from django.utils.translation import gettext as _
from enumerify.enum import Enum


class Currencies(Enum):
    ALL = 0
    AFN = 1
    ARS = 2
    AWG = 3
    AUD = 4
    AZN = 5
    BSD = 6
    BBD = 7
    BDT = 8
    BYR = 9
    BZD = 10
    BMD = 11
    BOB = 12
    BAM = 13
    BWP = 14
    BGN = 15
    BRL = 16
    BND = 17
    KHR = 18
    CAD = 19
    KYD = 20
    CLP = 21
    CNY = 22
    COP = 23
    CRC = 24
    HRK = 25
    CUP = 26
    CZK = 27
    DKK = 28
    DOP = 29
    XCD = 30
    EGP = 31
    SVC = 32
    EEK = 33
    EUR = 34
    FKP = 35
    FJD = 36
    GHC = 37
    GIP = 38
    GTQ = 39
    GGP = 40
    GYD = 41
    HNL = 42
    HKD = 43
    HUF = 44
    ISK = 45
    INR = 46
    IDR = 47
    IRR = 48
    IMP = 49
    ILS = 50
    JMD = 51
    JPY = 52
    JEP = 53
    KZT = 54
    KPW = 55
    KRW = 56
    KGS = 57
    LAK = 58
    LVL = 59
    LBP = 60
    LRD = 61
    LTL = 62
    MKD = 63
    MYR = 64
    MUR = 65
    MXN = 66
    MNT = 67
    MZN = 68
    NAD = 69
    NPR = 70
    ANG = 71
    NZD = 72
    NIO = 73
    NGN = 74
    NOK = 75
    OMR = 76
    PKR = 77
    PAB = 78
    PYG = 79
    PEN = 80
    PHP = 81
    PLN = 82
    QAR = 83
    RON = 84
    RUB = 85
    SHP = 86
    SAR = 87
    RSD = 88
    SCR = 89
    SGD = 90
    SBD = 91
    SOS = 92
    ZAR = 93
    LKR = 94
    SEK = 95
    CHF = 96
    SRD = 97
    SYP = 98
    TWD = 99
    THB = 100
    TTD = 101
    TRY = 102
    TRL = 103
    TVD = 104
    UAH = 105
    GBP = 106
    USD = 107
    UYU = 108
    UZS = 109
    VEF = 110
    VND = 111
    YER = 112
    ZWD = 113

    i18n = (
        _('Albania Lek'),
        _('Afghanistan Afghani'),
        _('Argentina Peso'),
        _('Aruba Guilder'),
        _('Australia Dollar'),
        _('Azerbaijan New Manat'),
        _('Bahamas Dollar'),
        _('Barbados Dollar'),
        _('Bangladeshi taka'),
        _('Belarus Ruble'),
        _('Belize Dollar'),
        _('Bermuda Dollar'),
        _('Bolivia Boliviano'),
        _('Bosnia and Herzegovina Convertible Marka'),
        _('Botswana Pula'),
        _('Bulgaria Lev'),
        _('Brazil Real'),
        _('Brunei Darussalam Dollar'),
        _('Cambodia Riel'),
        _('Canada Dollar'),
        _('Cayman Islands Dollar'),
        _('Chile Peso'),
        _('China Yuan Renminbi'),
        _('Colombia Peso'),
        _('Costa Rica Colon'),
        _('Croatia Kuna'),
        _('Cuba Peso'),
        _('Czech Republic Koruna'),
        _('Denmark Krone'),
        _('Dominican Republic Peso'),
        _('East Caribbean Dollar'),
        _('Egypt Pound'),
        _('El Salvador Colon'),
        _('Estonia Kroon'),
        _('Euro Member Countries'),
        _('Falkland Islands (Malvinas) Pound'),
        _('Fiji Dollar'),
        _('Ghana Cedis'),
        _('Gibraltar Pound'),
        _('Guatemala Quetzal'),
        _('Guernsey Pound'),
        _('Guyana Dollar'),
        _('Honduras Lempira'),
        _('Hong Kong Dollar'),
        _('Hungary Forint'),
        _('Iceland Krona'),
        _('India Rupee'),
        _('Indonesia Rupiah'),
        _('Iran Rial'),
        _('Isle of Man Pound'),
        _('Israel Shekel'),
        _('Jamaica Dollar'),
        _('Japan Yen'),
        _('Jersey Pound'),
        _('Kazakhstan Tenge'),
        _('Korea (North) Won'),
        _('Korea (South) Won'),
        _('Kyrgyzstan Som'),
        _('Laos Kip'),
        _('Latvia Lat'),
        _('Lebanon Pound'),
        _('Liberia Dollar'),
        _('Lithuania Litas'),
        _('Macedonia Denar'),
        _('Malaysia Ringgit'),
        _('Mauritius Rupee'),
        _('Mexico Peso'),
        _('Mongolia Tughrik'),
        _('Mozambique Metical'),
        _('Namibia Dollar'),
        _('Nepal Rupee'),
        _('Netherlands Antilles Guilder'),
        _('New Zealand Dollar'),
        _('Nicaragua Cordoba'),
        _('Nigeria Naira'),
        _('Norway Krone'),
        _('Oman Rial'),
        _('Pakistan Rupee'),
        _('Panama Balboa'),
        _('Paraguay Guarani'),
        _('Peru Nuevo Sol'),
        _('Philippines Peso'),
        _('Poland Zloty'),
        _('Qatar Riyal'),
        _('Romania New Leu'),
        _('Russia Ruble'),
        _('Saint Helena Pound'),
        _('Saudi Arabia Riyal'),
        _('Serbia Dinar'),
        _('Seychelles Rupee'),
        _('Singapore Dollar'),
        _('Solomon Islands Dollar'),
        _('Somalia Shilling'),
        _('South Africa Rand'),
        _('Sri Lanka Rupee'),
        _('Sweden Krona'),
        _('Switzerland Franc'),
        _('Suriname Dollar'),
        _('Syria Pound'),
        _('Taiwan New Dollar'),
        _('Thailand Baht'),
        _('Trinidad and Tobago Dollar'),
        _('Turkey Lira'),
        _('Turkey Lira'),
        _('Tuvalu Dollar'),
        _('Ukraine Hryvna'),
        _('United Kingdom Pound'),
        _('United States Dollar'),
        _('Uruguay Peso'),
        _('Uzbekistan Som'),
        _('Venezuela Bolivar'),
        _('Viet Nam Dong'),
        _('Yemen Rial'),
        _('Zimbabwe Dollar')
    )
