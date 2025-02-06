import json
from rest_framework import views, response, status
from webhooks import models


class WebhookOrderView(views.APIView):
    
    def post(self, request):
        data = request.data

        models.Webhook.objects.create(
            event_type=data.get('event_type'),
            event=json.dumps(data, ensure_ascii=False),
        )

        return response.Response(
            data=data,
            status=status.HTTP_200_OK,
        )
