from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect


def validar_renda(request):
    if request.method == 'POST':
        renda = float(request.POST['renda'])
        #validação da renda
        if renda >= 1000:  
            return redirect('calcular_emprestimo')  
        else:
            return redirect('renda_invalida')
    return render(request, 'validar_renda.html')  
    
def calcular_emprestimo(request):
    if request.method == 'POST':
        valor_emprestimo = float(request.POST['valor_emprestimo'])
        prazo = int(request.POST['prazo'])
        #cálculo do empréstimo 
        juros = 0.05  #taxa de juros
        prestacao = (valor_emprestimo * juros) / (1 - (1 + juros) ** -prazo)
        custo_total = prestacao * prazo  # Custo total do empréstimo

        # Arredonda os valores para duas casas decimais
        prestacao = round(prestacao, 2)
        custo_total = round(custo_total, 2)
        
        return render(request, 'resultado_emprestimo.html', {'prestacao': prestacao, 'custo_total': custo_total})
    return render(request, 'calcular_emprestimo.html')  

def index(request):
    return render(request, 'index.html')

def renda_invalida(request):
    return render(request, 'renda_invalida.html')

def resultado_emprestimo(request):
    return render(request, 'resultado_emprestimo.html', {'prestacao': prestacao, 'custo_total': custo_total})