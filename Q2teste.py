from Q2 import ContaCorrente

novaConta = ContaCorrente("Paulo", 1000)
print(f"Saldo inicial: R$ {novaConta.saldo:.2f}")

saque1 = novaConta.sacar(500)
if saque1:
    print("Saque de R$ 500.00 realizado com sucesso.")
else:
    print("Saldo insuficiente para o saque de R$ 500.00.")
print(f"Cliente: {novaConta.cliente}, Saldo: R$ {novaConta.saldo:.2f}")

saque2 = novaConta.sacar(500)
if saque2:
    print("Saque de R$ 500.00 realizado com sucesso.")
else:
    print("Saldo insuficiente para o saque de R$ 500.00.")
print(f"Novo saldo: R$ {novaConta.saldo:.2f}")

novaConta.depositar(50)
print(f"Novo saldo após depósito: R$ {novaConta.saldo:.2f}")
saque3 = novaConta.sacar(500)
if saque3:
    print("Saque de R$ 500.00 realizado com sucesso.")
else:
    print("Saldo insuficiente para o saque de R$ 500.00.")
print(f"Cliente: {novaConta.cliente}, Saldo final: R$ {novaConta.saldo:.2f}")