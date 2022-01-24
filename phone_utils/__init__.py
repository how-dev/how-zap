class PhoneValidators:
    ddd_range: list = range(11, 100)

    @staticmethod
    def country_digit_list() -> list:
        digit_list = [
            "+93",
            "+27",
            "+355",
            "+49",
            "+376",
            "+244",
            "+1",
            "+599",
            "+966",
            "+213",
            "+54",
            "+374",
            "+297",
            "+247",
            "+61",
            "+43",
            "+994",
            "+880",
            "+973",
            "+32",
            "+501",
            "+229",
            "+375",
            "+591",
            "+387",
            "+267",
            "+55",
            "+673",
            "+359",
            "+226",
            "+257",
            "+975",
            "+238",
            "+237",
            "+855",
            "+974",
            "+7",
            "+235",
            "+56",
            "+86",
            "+357",
            "+57",
            "+269",
            "+242",
            "+243",
            "+850",
            "+82",
            "+225",
            "+506",
            "+385",
            "+53",
            "+45",
            "+253",
            "+20",
            "+503",
            "+971",
            "+593",
            "+291",
            "+421",
            "+386",
            "+34",
            "+268",
            "+372",
            "+251",
            "+679",
            "+63",
            "+358",
            "+33",
            "+241",
            "+220",
            "+233",
            "+995",
            "+350",
            "+30",
            "+299",
            "+590",
            "+502",
            "+592",
            "+594",
            "+224",
            "+245",
            "+240",
            "+509",
            "+504",
            "+852",
            "+36",
            "+967",
            "+672",
            "+682",
            "+298",
            "+960",
            "+500",
            "+692",
            "+677",
            "+91",
            "+62",
            "+98",
            "+964",
            "+353",
            "+354",
            "+972",
            "+39",
            "+81",
            "+962",
            "+383",
            "+965",
            "+856",
            "+266",
            "+371",
            "+961",
            "+231",
            "+218",
            "+423",
            "+370",
            "+352",
            "+853",
            "+389",
            "+261",
            "+60",
            "+265",
            "+223",
            "+356",
            "+212",
            "+596",
            "+230",
            "+222",
            "+52",
            "+691",
            "+258",
            "+373",
            "+377",
            "+976",
            "+382",
            "+95",
            "+264",
            "+674",
            "+977",
            "+505",
            "+227",
            "+234",
            "+683",
            "+47",
            "+687",
            "+64",
            "+968",
            "+31",
            "+680",
            "+970",
            "+507",
            "+675",
            "+92",
            "+595",
            "+51",
            "+689",
            "+48",
            "+351",
            "+254",
            "+996",
            "+686",
            "+44",
            "+236",
            "+262",
            "+40",
            "+250",
            "+685",
            "+290",
            "+378",
            "+508",
            "+239",
            "+248",
            "+221",
            "+94",
            "+232",
            "+381",
            "+65",
            "+963",
            "+252",
            "+249",
            "+211",
            "+46",
            "+41",
            "+597",
            "+992",
            "+66",
            "+886",
            "+255",
            "+246",
            "+420",
            "+670",
            "+228",
            "+690",
            "+676",
            "+216",
            "+993",
            "+90",
            "+688",
            "+380",
            "+256",
            "+598",
            "+998",
            "+678",
            "+379",
            "+58",
            "+84",
            "+681",
            "+260",
            "+263",
        ]
        return digit_list

    def is_valid_country(self, digit, raise_exception: bool = False) -> bool:
        is_digit = f"+{digit}" in self.country_digit_list()

        if raise_exception is True and not is_digit:
            return False
        else:
            return True

    def is_valid_ddd(self, ddd, raise_exception: bool = False) -> bool:
        try:
            ddd = int(ddd)
        except ValueError:
            return False
        is_ddd = ddd in self.ddd_range

        if raise_exception is True and not is_ddd:
            return False
        else:
            return True

    @staticmethod
    def is_valid_phone(phone, raise_exception: bool = False) -> bool:
        try:
            int(phone)
        except ValueError:
            return False

        is_actual = phone[0] == "9"
        is_right_size = len(phone) == 9
        is_alright = phone.isnumeric()

        if raise_exception is True and (not is_actual or not is_right_size or not is_alright):
            return False
        else:
            return True

    @staticmethod
    def is_valid_amount(amount, raise_exception: bool = False) -> bool:
        try:
            amount = int(amount)
        except ValueError:
            return False

        is_positive = amount > 0

        if raise_exception is True and not is_positive:
            return False
        else:
            return True
