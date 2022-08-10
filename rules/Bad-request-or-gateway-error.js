const charges = {
    transaction: {
        reference: {type: "string", minLength: 1, maxLength: 64, required: []},
        amount: {type: "integer", exclusiveMinimum: 0, gt:{toss:100,toss_banktransfer: 200},required: []},
        currency: {type: "string", required: []},
        country: {type: "string"},
        auto_capture: {type: "boolean",toss_banktransfer:1,toss_toss:1},
        note: {type: "string"}
    },
    payment: {
        method: {type: "string", minLength: 1, toss:['card', 'banktransfer', 'toss', 'lpay', 'lgpay', 'samsungpay'], required:[]},
        indicator: {type: "string"},
        request_token: {type: "boolean"},
        timeout: {type: "integer", minimum: 0, required:['toss']},
        token: {type: "string"},
        nonce: {type: "string"},
        client: {
            type: "array",
            items: {
                type: "string",
                enum: [
                    "desktop",
                    "mobile_browser",
                    "mobile_native",
                    "mini_program",
                ],
            },
            minItems: 1,
            uniqueItems: true,
        },
        data: {
            pan: {type: "string"},
            first_name: {type: "string"},
            last_name: {type: "string"},
            expiry: {type: "string", pattern: "^(([0][1-9])|([1][0-2]))\\/[2-9][0-9]$"},
            cvv: {type: "string"}
        },
        billing_address: {
            street: {type: 'string'},
            street2: {type: 'string'},
            city: {type: 'string'},
            state: {type: 'string'},
            zip: {type: 'string'},
            country: {type: 'string'}
        },
        '3ds': {
            indicator: {type: "string"},
            id: {type: "string"},
            authentication: {type: "string"},
            server: {type: "string"},
            version: {type: "string"},
        },
        cof: {
            request: {type: "boolean"},
            id: {type: "string"},
            indicator: {type: "string"},
        },
        check: {
            cvv: {type: "boolean"},
            avs: {type: "boolean"}
        }
    },
    consumer: {
        reference: {type: "string"},
        first_name: {type: "string"},
        last_name: {type: "string"},
        phone: {type: "string"},
        email: {type: "string", pattern: "^[+a-zA-Z0-9_.!#$%&\"*\\/=?^`{|}~-]+@([a-zA-Z0-9-]+\\.)+[a-zA-Z0-9]{2,63}$"},
        ext_data: {
            document_id: {type: "string"},
            eft_code: {type: "string"},
        }
    },
    goods: {
        data: {
            item: [
                {
                    name: {type: 'string'},
                    sku: {type: 'string'},
                    url: {type: 'string'},
                    quantity: {type: 'number', exclusiveMinimum: 0},
                    total_amount: {type: 'number', exclusiveMinimum: 0},
                    unit_amount: {type: 'number', exclusiveMinimum: 0},
                    total_tax_rate: {type: 'number'},
                    total_tax_amount: {type: 'number'},
                    total_discount_amount: {type: 'number'},
                    taxable_amount: {type: 'number'},
                    tax_exempt_amount: {type: 'number',lt:{toss:'amount'}},
                }
            ],
            minItems: 1, type: 'array', required: []
        },
        shipping: {
            first_name: {type: 'string'},
            last_name: {type: 'string'},
            phone: {type: 'string'},
            email: {
                type: 'string',
                pattern: '^[+a-zA-Z0-9_.!#$%&\'*\\/=?^`{|}~-]+@([a-zA-Z0-9-]+\\.)+[a-zA-Z0-9]{2,63}$'
            },
            street: {type: 'string'},
            street2: {type: 'string'},
            city: {type: 'string'},
            state: {type: 'string'},
            zip: {type: 'string'},
            country: {type: 'string'},
        }
    },
    installments: {
        id: {type: "string",toss:[0,12]},
        payment_number: {type: "number"},
        quantity: {type: "integer", toss_card:[0,12]},
        promo: {
            type: "array",
            items: {type: "string"},
        }
    },
    urls: {
        ipn: {type: "string",required:['toss']},
        success: {type: "string", required:['toss']},
        fail: {type: "string", required:['toss']},
        mobile: {type: "string"},
        cancel: {type: "string"},
    },
    ext: {
        device: {
            id: {type: "string"},
            ip: {type: "string"},
            fingerprint: {type: "string"},
        },
        client: {
            app: {type: 'string'},
            version: {type: 'string'},
        },
        transaction: {
            cash_receipt:{
                type: { type: 'string' },
                registration_number: { type: 'string' },

            }
        }
    }
};