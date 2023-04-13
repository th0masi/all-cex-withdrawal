import time
import ccxt
import random

#----main-options----#
switch_cex = "binance"       # binance, mexc, kucoin, gate, okx, huobi, bybit
symbolWithdraw = "USDT"      # символ токена
network = "Arbitrum One"     # ID сети
proxy_server = "http://login:password@IP:port"

#----second-options----#
amount = [1.5, 2.5]          # минимальная и максимальная сумма
decimal_places = 2           # количество знаков, после запятой для генерации случайных чисел
delay = [35, 85]             # минимальная и максимальная задержка
shuffle_wallets = "no"       # нужно ли мешать кошельки yes/no
#----end-all-options----#

class API:
    # binance API
    binance_apikey = "your_api"
    binance_apisecret = "your_api_secret"
    # okx API
    okx_apikey = "your_api"
    okx_apisecret = "your_api_secret"
    okx_passphrase = "your_api_password"
    # bybit API
    bybit_apikey = "your_api"
    bybit_apisecret = "your_api_secret"
    # gate API
    gate_apikey = "your_api"
    gate_apisecret = "your_api_secret"
    # kucoin API
    kucoin_apikey = "your_api"
    kucoin_apisecret = "your_api_secret"
    kucoin_passphrase = "your_api_password"
    # mexc API
    mexc_apikey = "your_api"
    mexc_apisecret = "your_api_secret"
    # huobi API
    huobi_apikey = "your_api"
    huobi_apisecret = "your_api_secret"

proxies = {
  "http": proxy_server,
  "https": proxy_server,
}

def binance_withdraw(address, amount_to_withdrawal, wallet_number):
    exchange = ccxt.binance({
        'apiKey': API.binance_apikey,
        'secret': API.binance_apisecret,
        'enableRateLimit': True,
        'options': {
            'defaultType': 'spot'
        }
    })

    try:
        exchange.withdraw(
            code=symbolWithdraw,
            amount=amount_to_withdrawal,
            address=address,
            tag=None,
            params={
                "network": network
            }
        )
        print(f'\n>>>[Binance] Вывел {amount_to_withdrawal} {symbolWithdraw} ', flush=True)
        print(f'    [{wallet_number}]{address}', flush=True)
    except Exception as error:
        print(f'\n>>>[Binance] Не удалось вывести {amount_to_withdrawal} {symbolWithdraw}: {error} ', flush=True)
        print(f'    [{wallet_number}]{address}', flush=True)


def okx_withdraw(address, amount_to_withdrawal, wallet_number):
    exchange = ccxt.okx({
        'apiKey': API.okx_apikey,
        'secret': API.okx_apisecret,
        'password': API.okx_passphrase,
        'enableRateLimit': True,
        'proxies': proxies,
    })

    try:
        chainName = symbolWithdraw + "-" + network
        fee = get_withdrawal_fee(symbolWithdraw, chainName)
        exchange.withdraw(symbolWithdraw, amount_to_withdrawal, address,
            params={
                "toAddress": address,
                "chainName": chainName,
                "dest": 4,
                "fee": fee,
                "pwd": '-',
                "amt": amount_to_withdrawal,
                "network": network
            }
        )

        print(f'\n>>>[OKx] Вывел {amount_to_withdrawal} {symbolWithdraw} ', flush=True)
        print(f'    [{wallet_number}]{address}', flush=True)
    except Exception as error:
        print(f'\n>>>[OKx] Не удалось вывести {amount_to_withdrawal} {symbolWithdraw}: {error} ', flush=True)
        print(f'    [{wallet_number}]{address}', flush=True)


def bybit_withdraw(address, amount_to_withdrawal, wallet_number):
    exchange = ccxt.bybit({
        'apiKey': API.bybit_apikey,
        'secret': API.bybit_apisecret,
    })

    try:
        exchange.withdraw(
            code=symbolWithdraw,
            amount=amount_to_withdrawal,
            address=address,
            tag=None,
            params={
                "forceChain": 1,
                "network": network
            }
        )
        print(f'\n>>>[ByBit] Вывел {amount_to_withdrawal} {symbolWithdraw} ', flush=True)
        print(f'    [{wallet_number}]{address}', flush=True)
    except Exception as error:
        print(f'\n>>>[ByBit] Не удалось вывести {amount_to_withdrawal} {symbolWithdraw}: {error} ', flush=True)
        print(f'    [{wallet_number}]{address}', flush=True)


def gate_withdraw(address, amount_to_withdrawal, wallet_number):
    exchange = ccxt.gate({
        'apiKey': API.gate_apikey,
        'secret': API.gate_apisecret,
    })

    try:
        exchange.withdraw(
            code=symbolWithdraw,
            amount=amount_to_withdrawal,
            address=address,
            params={
                "network": network
            }
        )
        print(f'\n>>>[Gate.io] Вывел {amount_to_withdrawal} {symbolWithdraw} ', flush=True)
        print(f'    [{wallet_number}]{address}', flush=True)
    except Exception as error:
        print(f'\n>>>[Gate.io] Не удалось вывести {amount_to_withdrawal} {symbolWithdraw}: {error} ', flush=True)
        print(f'    [{wallet_number}]{address}', flush=True)


def kucoin_withdraw(address, amount_to_withdrawal, wallet_number):
    exchange = ccxt.kucoin({
        'apiKey': API.kucoin_apikey,
        'secret': API.kucoin_apisecret,
        'password': API.kucoin_passphrase,
        'enableRateLimit': True,
    })

    try:
        exchange.withdraw(
            code=symbolWithdraw,
            amount=amount_to_withdrawal,
            address=address,
            params={
                "network": network
            }
        )
        print(f'\n>>>[Kucoin] Вывел {amount_to_withdrawal} {symbolWithdraw} ', flush=True)
        print(f'    [{wallet_number}]{address}', flush=True)
    except Exception as error:
        print(f'\n>>>[Kucoin] Не удалось вывести {amount_to_withdrawal} {symbolWithdraw}: {error} ', flush=True)
        print(f'    [{wallet_number}]{address}', flush=True)


def mexc_withdraw(address, amount_to_withdrawal, wallet_number):
    exchange = ccxt.mexc({
        'apiKey': API.mexc_apikey,
        'secret': API.mexc_apisecret,
        'enableRateLimit': True,
    })

    try:
        exchange.withdraw(
            code=symbolWithdraw,
            amount=amount_to_withdrawal,
            address=address,
            params={
                "network": network
            }
        )
        print(f'\n>>>[MEXC] Вывел {amount_to_withdrawal} {symbolWithdraw} ', flush=True)
        print(f'    [{wallet_number}]{address}', flush=True)
    except Exception as error:
        print(f'\n>>>[MEXC] Не удалось вывести {amount_to_withdrawal} {symbolWithdraw}: {error} ', flush=True)
        print(f'    [{wallet_number}]{address}', flush=True)


def huobi_withdraw(address, amount_to_withdrawal, wallet_number):
    exchange = ccxt.huobi({
        'apiKey': API.huobi_apikey,
        'secret': API.huobi_apisecret,
        'enableRateLimit': True,
    })

    try:
        exchange.withdraw(
            code=symbolWithdraw,
            amount=amount_to_withdrawal,
            address=address,
            params={
                "network": network
            }
        )
        print(f'\n>>>[Huobi] Вывел {amount_to_withdrawal} {symbolWithdraw} ', flush=True)
        print(f'    [{wallet_number}]{address}', flush=True)
    except Exception as error:
        print(f'\n>>>[Huobi] Не удалось вывести {amount_to_withdrawal} {symbolWithdraw}: {error} ', flush=True)
        print(f'    [{wallet_number}]{address}', flush=True)


def choose_cex(address, amount_to_withdrawal, wallet_number):
    if switch_cex == "binance":
        binance_withdraw(address, amount_to_withdrawal, wallet_number)
    elif switch_cex == "okx":
        okx_withdraw(address, amount_to_withdrawal, wallet_number)
    elif switch_cex == "bybit":
        print(f"\n>>> Bybit в больнице, у них API заболело, sorry") #bybit_withdraw(address, amount_to_withdrawal, wallet_number)
    elif switch_cex == "gate":
        gate_withdraw(address, amount_to_withdrawal, wallet_number)
    elif switch_cex == "huobi":
        huobi_withdraw(address, amount_to_withdrawal, wallet_number)
    elif switch_cex == "kucoin":
        kucoin_withdraw(address, amount_to_withdrawal, wallet_number)
    elif switch_cex == "mexc":
        mexc_withdraw(address, amount_to_withdrawal, wallet_number)
    else:
        raise ValueError("Неверное значение CEX. Поддерживаемые значения: binance, okx, bybit, gate, huobi, kucoin, mexc.")

def get_withdrawal_fee(symbolWithdraw, chainName):
    exchange = ccxt.okx({
        'apiKey': API.okx_apikey,
        'secret': API.okx_apisecret,
        'password': API.okx_passphrase,
        'enableRateLimit': True,
        'proxies': proxies,
    })
    currencies = exchange.fetch_currencies()
    for currency in currencies:
        if currency == symbolWithdraw:
            currency_info = currencies[currency]
            network_info = currency_info.get('networks', None)
            if network_info:
                for network in network_info:
                    network_data = network_info[network]
                    network_id = network_data['id']
                    if network_id == chainName:
                        withdrawal_fee = currency_info['networks'][network]['fee']
                        if withdrawal_fee == 0:
                            return 0
                        else:
                            return withdrawal_fee
    raise ValueError(f"     не могу получить сумму комиссии, проверьте значения symbolWithdraw и network")

def shuffle(wallets_list, shuffle_wallets):
    numbered_wallets = list(enumerate(wallets_list, start=1))
    if shuffle_wallets.lower() == "yes":
        random.shuffle(numbered_wallets)
    elif shuffle_wallets.lower() == "no":
        pass
    else:
        raise ValueError("\n>>> Неверное значение переменной 'shuffle_wallets'. Ожидается 'yes' или 'no'.")
    return numbered_wallets

if __name__ == "__main__":
    with open("wallets.txt", "r") as f:
        wallets_list = [row.strip() for row in f if row.strip()]
        numbered_wallets = shuffle(wallets_list, shuffle_wallets)
        print(f'developed by th0masi [https://t.me/thor_lab]')
        print(f'Number of wallets: {len(wallets_list)}')
        print(f"CEX: {switch_cex}")
        print(f"Amount: {amount[0]} - {amount[1]} {symbolWithdraw}")
        print(f"Network: {network}")
        time.sleep(random.randint(2, 4))

        for wallet_number, address in numbered_wallets:
            amount_to_withdrawal = round(random.uniform(amount[0], amount[1]), decimal_places)
            choose_cex(address, amount_to_withdrawal, wallet_number)
            time.sleep(random.randint(delay[0], delay[1]))



