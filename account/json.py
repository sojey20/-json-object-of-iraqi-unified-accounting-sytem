import json

iraqi_law = '''

{
    "code": "000002",
    "name": "المطلوبات",
    "children": [
        {
            "code": "000021",
            "name": "رأس المال",
            "children": [
                {
                    "code": "000211",
                    "name": "رأس المال المدفوع"
                },
                {
                    "code": "000212",
                    "name": "رأس المال(صافي الموجودات)"
                },
                {
                    "code": "000213",
                    "name": "رأس المال(متبرع به)"
                }
            ]
        },
        {
            "code": "000022",
            "name": "الاحتياطات",
            "children": [
                {
                    "code": "000221",
                    "name": "الاحتياطات رأسمالية",
                    "children": [
                        {
                            "code": "002211",
                            "name": "احتياطي التوسعات",
                            "children": [
                                {
                                    "code": "022111",
                                    "name": "احتياطي توسعات مستخدم"
                                },
                                {
                                    "code": "022112",
                                    "name": "احتياطي توسعات غير مستخدم"
                                }
                            ]
                        },
                        {
                            "code": "002212",
                            "name": "احتياطي استبدال موجودات ثابتة"
                        },
                        {
                            "code": "002213",
                            "name": "احتياطي المكاسب الثابتة"
                        }
                    ]
                },
                {
                    "code": "000222",
                    "name": "احتياطي عام"
                },
                {
                    "code": "000223",
                    "name": "احتياطي متنوعة"
                },
                {
                    "code": "000224",
                    "name": "الفائض المتراكم"
                },
                {
                    "code": "000225",
                    "name": "العجز المتراكم"
                }
            ]
        },
        {
            "code": "000023",
            "name": "التخصيصات",
            "children": [
                {
                    "code": "000231",
                    "name": "مخصص الاندثار المتراكم",
                    "children": [
                        {
                            "code": "002311",
                            "name": "مخصص اندثار المباني و انشاءات الطرق"
                        },
                        {
                            "code": "002312",
                            "name": "مخصص اندثار الات و المعدات"
                        },
                        {
                            "code": "002313",
                            "name": " مخصص اندثار وساىط النقل وانتقال "
                        },
                        {
                            "code": "002314",
                            "name": "مخصص اندثار عدد و قوالب"
                        },
                        {
                            "code": "002315",
                            "name": "مخصص اندثار أثاث و اجهزة مكاتب"
                        }
                    ]
                },
                {
                    "code": "000232",
                    "name": "مخصص الديون المشكوك في تحصيلها"
                },
                {
                    "code": "000233",
                    "name": "مخصص مصروفات الشراء"
                },
                {
                    "code": "000234",
                    "name": "مخصص خسائر متوقعة لمشاريع قيد الإنجاز"
                },
                {
                    "code": "000235",
                    "name": "مخصص مصاريف الصيانة محتملة"
                },
                {
                    "code": "000236",
                    "name": "مخصص هبوط أسعار المخزون السلعي"
                },
                {
                    "code": "000237",
                    "name": "مخصص هبوط الاستثمارات المالية"
                },
                {
                    "code": "000238",
                    "name": "تخصيصات متنوعة"
                }
            ]
        },
        {
            "code": "000024",
            "name": "القروض المستلمة",
            "children:": [
                {
                    "code": "000241",
                    "name": "القروض المستلمة طويلة الأجل",
                    "children": [
                        {
                            "code": "002411",
                            "name": "قروض طويلة الاجل من القطاع العام"
                        },
                        {
                            "code": "002412",
                            "name": "قروض طويلة الاجل من القطاع التعاوني"
                        },
                        {
                            "code": "002413",
                            "name": "قروض طويلة الاجل من القطاع المختلط"
                        },
                        {
                            "code": "002414",
                            "name": "قروض طويلة الاجل من القطاع الخاص"
                        },
                        {
                            "code": "002415",
                            "name": "قروض طويلة الاجل من العالم الخارجي"
                        }
                    ]
                },
                {
                    "code": "000242",
                    "name": "القروض المستلمة قصيرة الأجل",
                    "children": [
                        {
                            "code": "002421",
                            "name": "قروض قصيرة الاجل من القطاع العام"
                        },
                        {
                            "code": "002422",
                            "name": "قروض قصيرة الاجل من القطاع التعاوني"
                        },
                        {
                            "code": "002423",
                            "name": "قروض قصيرة الاجل من القطاع المختلط"
                        },
                        {
                            "code": "002424",
                            "name": "قروض قصيرة الاجل من القطاع الخاص"
                        },
                        {
                            "code": "002425",
                            "name": "قروض قصيرة الاجل من العالم الخارجي"
                        }
                    ]
                }
            ]
        },
        {
            "code": "000025",
            "name": "المصارف الداىنة",
            "children":[{
                "code": "000251",
                "name": "جاري مكشوف"
            }]
        },
        {
            "code": "000026",
            "name": "الدائنون",
            "children":[
                {
                    "code": "000261",
                    "name": "مجهزون تجاريون",
                    "children": [
                        {
                            "code": "002611",
                            "name": "مجهزون قطاع عام"
                        },
                        {
                            "code": "002612",
                            "name": "مجهزون قطاع تعاوني"
                        },
                        {
                            "code": "002613",
                            "name": "مجهزون قطاع مختلط"
                        },
                        {
                            "code": "002614",
                            "name": "مجهزون قطاع خاص"
                        },
                        {
                            "code": "002615",
                            "name": "مجهزون عالم خارجي"
                        },
                        {
                            "code": "002616",
                            "name": "مجهزون بالدفع الاجل"
                        }
                    ]
                },
                {
                    "code": "000262",
                    "name": "أوراق الدفع",
                    "children":[{
                        "code": "002621",
                        "name": "أوراق الدفع قطاع عام"
                    },
                    {
                        "code": "002622",
                        "name": "أوراق الدفع القطاع التعاوني"
                    },
                    {
                        "code": "002623",
                        "name": "أوراق الدفع القطاع المختلط"
                    },
                    {
                        "code": "002624",
                        "name": "أوراق الدفع القطاع الخاص"
                    },
                    {
                        "code": "002625",
                        "name": "أوراق الدفع العالم الخارجي"
                    }]
                },
                {
                    "code": "000263",
                    "name": "حسابات جارية دائنة",
                    "children":[
                        {
                            "code": "002631",
                            "name": "حسابات جارية دائنة داخل الوحدة الاقتصادية الرئيسة"
                        },
                        {
                            "code": "002632",
                            "name": "حسابات جارية دائنة خارج الوحدة الاقتصادية الفرعية"
                        }
                    ]
                },
                {
                    "code": "000264",
                    "name": "حسابات التعهدات",
                    "children":[
                        {
                            "code": "002641",
                            "name": "سلف مستلمة مقدما" 
                        },
                        {
                            "code": "002642",
                            "name": "الذرعات المنجزة"
                        }
                    ]
                },
                {
                    "code":"000265",
                    "name": "دائنو نشاط غير جاري"
                },
                {
                    "code": "000266",
                    "name":"حسابات دائنة متنوعة",
                    "children":[
                        {
                            "code": "002661",
                            "name": "تأمينات مستلمة وحسابات التوفير",
                            "children":[
                                {
                                    "code":"026611",
                                    "name":"تأمينات مستلمة قصيرة الأجل"
                                },
                                {
                                    "code":"026612",
                                    "name":"تأمينات مستلمة طويلة الأجل"
                                },
                                {
                                    "code":"026613",
                                    "name":"حسابات التوفير"
                                    ,"children":[
                                        {
                                            "code":"266131",
                                            "name":" توفير عادي"
                                        },
                                        {
                                            "code":"266132",
                                            "name":"توفير مدرسي"
                                        },
                                        {
                                            "code":"266133",
                                            "name":"حوالات داخلية"
                                        },
                                        {
                                            "code":"266134",
                                            "name":"حوالات خارجية"
                                        },
                                        {
                                            "code":"266135",
                                            "name":"تحاويل بريدية"
                                        }
                                    ] 
                                }
                            ]
                        },
                        {
                            "code": "002662",
                            "name":"إيرادات مستلمة مقدما"
                        },
                        {
                            "code": "002663",
                            "name":"مصاريف مستحقة"
                        },
                        {
                            "code": "002664",
                            "name":"رواتب و اجور مستحقة"
                        },
                        {
                            "code": "002665",
                            "name":"رواتب و اجور معادة"
                        },
                        {
                            "code": "002666",
                            "name":"هيئة التقاعد الوطنية"
                        },
                        {
                            "code": "002667",
                            "name":"دائرة التقاعد و الضمان الاجتماعي"
                        },
                        {
                            "code": "002668",
                            "name":"فروقات نقدية و مخزنية دائنة",
                            "children":[
                                {
                                    "code":"026681",
                                    "name":"فروقات نقدية دائنة"
                                },
                                {
                                    "code":"026682",
                                    "name":"فروقات مخزنية دائنة"
                                }
                            ]
                        },
                        {
                            "code":"002669",
                            "name":"تعويضات و غرامات مؤدلة"
                        }
                    ]
                },
                {
                    "code": "000267",
                    "name":"استقطاعات لحساب الغير",
                    "children":[
                        {
                            "code":"002671",
                            "name":"استقطاعات من المنتسبين لحساب الغير"
                        },
                        {
                            "code":"002672",
                            "name":"استقطاعات من غير المنتسبين لحساب الغير"
                        }
                    ]
                },
                {
                    "code": "000268",
                    "name":"دائنو توزيع الارباح",
                    "children":[
                        {
                            "code":"002681",
                            "name":"حصة الخزينة العامة"
                        },
                        {
                            "code":"002682",
                            "name":"حصة العاملين"
                        }
                    ]
                }
            ]
        },
        {
            "code": "000028",
            "name": "حساب العمليات الجارية",
            "children":[
                {
                    "code": "000281",
                    "name": "حسابات النشاط الجاري"
                }
            ]
        },
        {
            "code": "000029",
            "name": "الحسابات المتقابلة الدائنة",
            "children":[
                {
                    "code": "000291",
                    "name": "مقابل حركه الإنتاج التام بسعر البيع"
                },
                {
                    "code": "000292",
                    "name": "حسابات الالتزامات الدائنة",
                    "children":[
                        {
                            "code":"002921",
                            "name":"مقابل الاعتمادات المستندية المستلمة"
                        },
                        {
                            "code":"002922",
                            "name":"الاعتمادات المستندية الصادرة"
                        },
                        {
                            "code":"002923",
                            "name":"مقابل خطابات الضمان المستلمة"
                        },
                        {
                            "code":"002924",
                            "name":"خطابات الضمان الصادرة"
                        },
                        {
                            "code":"002925",
                            "name":" مقابل العقود"
                        }
                    ]
                },
                {
                    "code": "000293",
                    "name": "مقابل حسابات بالقيمة الرمزية"
                },
                {
                    "code": "000294",
                    "name": "حسابات النتيجة الدائنة",
                    "children":[
                        {
                            "code":"002941",
                            "name":"مقابل فرق الايجار المحتسب"
                        },
                        {
                            "code":"002942",
                            "name":"مقابل فرق الفوائد المحتسبة"
                        },
                        {
                            "code":"002943",
                            "name":"مقابل فرق تقويم تغير مخزون الانتاج التام"
                        },
                        {
                            "code":"002944",
                            "name":"مقابل فرق تقويم تغير مخزون بضائع و اراضي بغرض البيع"
                        }
                    ]
                },
                {
                    "code": "000295",
                    "name": "مقابل موجودات اثرية و فنية"
                }
            ]
        }
    ]
}
'''

data =json.dumps(iraqi_law)

print(data)