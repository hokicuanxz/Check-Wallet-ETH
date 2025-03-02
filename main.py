from web3 import Web3
from colorama import Fore, Style, init

# Inisialisasi colorama untuk warna di terminal
init(autoreset=True)

# Ganti dengan URL Alchemy kamu
ALCHEMY_RPC_URL = "https://eth-mainnet.g.alchemy.com/v2/hZv6hdChwBUXRuC8ZUIBQqkgCFFhRo2Z"

# Inisialisasi Web3
web3 = Web3(Web3.HTTPProvider(ALCHEMY_RPC_URL))

def check_balance(wallet_address):
    """Cek saldo ETH / BNB / MATIC dari alamat dompet."""
    if web3.is_address(wallet_address):
        balance_wei = web3.eth.get_balance(wallet_address)  # Saldo dalam Wei
        balance_eth = web3.from_wei(balance_wei, "ether")  # Konversi ke ETH/BNB/MATIC
        return balance_eth
    else:
        return "Alamat tidak valid"

def check_multiple_balances(wallets):
    """Cek saldo banyak wallet sekaligus"""
    results = {}
    for wallet in wallets:
        balance = check_balance(wallet)
        results[wallet] = balance
    return results

# Menu pilihan
while True:
    print(Fore.CYAN + "\n╔═══════════════════════════╗")
    print(Fore.CYAN + "║   🚀 PENGECEK SALDO EVM   ║")
    print(Fore.CYAN + "╠═══════════════════════════╣")
    print(Fore.YELLOW + "║ 1️⃣  Cek saldo satu wallet  ║")
    print(Fore.YELLOW + "║ 2️⃣  Cek saldo banyak wallet║")
    print(Fore.RED + "║ 3️⃣  Keluar                 ║")
    print(Fore.CYAN + "╚═══════════════════════════╝")
    
    choice = input(Fore.GREEN + "👉 Pilih opsi (1/2/3): ").strip()
    
    if choice == "1":
        wallet = input(Fore.BLUE + "🔹 Masukkan alamat dompet EVM: ").strip()
        balance = check_balance(wallet)
        print(Fore.MAGENTA + f"💰 Saldo {wallet}: {balance} ETH")

    elif choice == "2":
        wallets = input(Fore.BLUE + "🔹 Masukkan alamat dompet (pisahkan dengan koma): ").strip().split(",")
        wallets = [w.strip() for w in wallets]  # Hapus spasi ekstra
        balances = check_multiple_balances(wallets)
        
        print(Fore.CYAN + "\n🎯 === Hasil Cek Saldo === 🎯")
        for wallet, balance in balances.items():
            print(Fore.MAGENTA + f"💰 {wallet}: {balance} ETH")
    
    elif choice == "3":
        print(Fore.RED + "🚀 Keluar dari program...")
        break

    else:
        print(Fore.RED + "⚠️ Pilihan tidak valid. Coba lagi!")
