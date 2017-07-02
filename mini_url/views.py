# http://djangofeeds.soup.io/since/604909962?newer=1
import json, requests, random, re
import datetime

from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator

from pprint import pprint
from django.views import generic
from django.http.response import HttpResponse
from .models import List, Card

verify_token = "tes_un_pd_si_tu_mets_pas_de_texte"


def get_joke(fbid, recevied_message):
    joke_text = requests.get("http://api.icndb.com/jokes/random/").json()['value']['joke']
    post_message_url = 'https://graph.facebook.com/v2.6/me/messages?access_token=%s'%'EAABcBLigDYcBAIzoAv6dgCR1RHJ0jfEMKepWToFEhmdYwbIifW9JjsAcEMRPGiQsO3gRPLZBBDDFtlFUExtX9BZAaJZBCZAxW7wZBqPZCZCSjMScab9k3zQjNZAKagEecOvQ061qz2mQgdOliZBXhe3WSUc6PEulBpyGWIvSymoa8VQZDZD'
    response_msg = json.dumps({"recipient": {"id": fbid }, "message": {"text": joke_text}})
    status = requests.post(post_message_url, headers={"Content-Type": "application/json"}, data=response_msg)
    pprint(status.json())

class jokebot(generic.View):
    def get(self, request, *args, **kwargs):
        if self.request.GET['hub.verify_token'] == verify_token:
            return HttpResponse(self.request.GET['hub.challenge'])
        else:
            return HttpResponse('Error')

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return generic.View.dispatch(self, request, *args, **kwargs)


    def post(self, request, *args, **kwargs):
        incoming_message = json.loads(self.request.body.decode('utf-8'))
        for entry in incoming_message['entry']:
            for message in entry['messaging']:
                if 'message' in message:
                    get_joke(message['sender']['id'], message['message']['text'])
                else:
                    HttpResponse('a jerk has posted a sticker')
        return HttpResponse()
