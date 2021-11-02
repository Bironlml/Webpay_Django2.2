from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
import datetime as dt

from transbank.webpay.webpay_plus.transaction import Transaction

import random

###     PAGINA PRINCIPAL    ###
def index(request):
    return render(request, 'index.html')

###     PRODUCTO 1          ###

def producto1(request):
    
    #TOTAL SE REFIERE AL PRECIO DEL PRODUCTO EL CUAL 
    #TIENE UN TEMPLATE ESPECIFICO EL CUAL ES EL "PAY.HTML"

    total = 10000

    return render(request, 'pay.html', {'total': total})

###     CREACION DEL PAGO POR WEBPAY    ###

def webpay_plus_create(request):

    

    buy_order = str(random.randrange(1000000, 99999999))
    session_id = str(random.randrange(1000000, 99999999))
    amount = request.POST.get('total')

    return_url = request.build_absolute_uri(location='commit-pay/')

    response = Transaction.create(buy_order, session_id, amount, return_url) 

    return render(request, 'send-pago.html', {'response': response, 'amount': amount})    



@csrf_exempt 
def commitpay(request):  
    token = request.POST.get('token_ws')

    TBK_TOKEN = request.POST.get('TBK_TOKEN')
    TBK_ID_SESION = request.POST.get('TBK_ID_SESION')
    TBK_ORDEN_COMPRA = request.POST.get('TBK_ORDEN_COMPRA')

    #TRANSACCIÓN REALIZADA

    if TBK_TOKEN is None and TBK_ID_SESION is None and TBK_ORDEN_COMPRA is None and token is not None:

        #APROBAR TRANSACCIÓN

        response = Transaction.commit(token=token)

        status = response.status

        response_code = response.response_code
        

        #TRANSACCIÓN APROBADA

        if status == 'AUTHORIZED' and response_code == 0:

            state = ''
            if response.status == 'AUTHORIZED':
                state = 'Aceptado'
            pay_type = ''
            if response.payment_type_code == 'VD':
                pay_type = 'Tarjeta de Débito'
            amount = int(response.amount)
            amount = f'{amount:,.0f}'.replace(',', '.')
            transaction_date = dt.datetime.strptime(response.transaction_date, '%Y-%m-%dT%H:%M:%S.%fZ')
            transaction_date = '{:%d-%m-%Y %H:%M:%S}'.format(transaction_date)
            transaction_detail = {  'card_number': response.card_detail.card_number,
                                    'transaction_date': transaction_date,
                                    'state': state,
                                    'pay_type': pay_type,
                                    'amount': amount,
                                    'authorization_code': response.authorization_code,
                                    'buy_order': response.buy_order, }
            return render(request, 'commit-pay.html', {'transaction_detail': transaction_detail})
        else:

        #TRANSACCIÓN RECHAZADA  

            return HttpResponse('ERROR EN LA TRANSACCIÓN, SE RECHAZA LA TRANSACCIÓN.')
    else:

    #TRANSACCIÓN CANCELADA   

        return HttpResponse('ERROR EN LA TRANSACCIÓN, SE CANCELO EL PAGO.')
