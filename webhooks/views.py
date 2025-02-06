import json
from rest_framework import views, response, status
from webhooks import models
from webhooks.messages import outflow_message
from services.callmebot import CallMeBot


class WebhookOrderView(views.APIView):
    
    def post(self, request):
        data = request.data

        models.Webhook.objects.create(
            event_type=data.get('event_type'),
            event=json.dumps(data, ensure_ascii=False),
        )

        product_title = data.get('product')
        quantity = data.get('quantity')
        product_cost_price = data.get('product_cost_price')
        product_selling_price = data.get('product_selling_price')
        total_value = product_selling_price * quantity
        profit_value = total_value - (product_cost_price * quantity)

        message = outflow_message.format(
            product_title, 
            quantity,
            total_value,
            profit_value,
        )

        callmebot = CallMeBot()
        callmebot.send_message(message)

        return response.Response(
            data=data,
            status=status.HTTP_200_OK,
        )
