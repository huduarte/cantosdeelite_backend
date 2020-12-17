# from django.db.models.signals import post_save
# from django.dispatch import receiver
# from person.models import Person
# from pessoa.models import pessoa
# from diagnostic.models import Diagnostic
# from django.contrib.auth import get_user_model
# User = get_user_model()

# @receiver(post_save, sender=pessoa)
# def post_pessoa_save(sender, instance, *args, **kwargs):
#     pass
#     # user = User.objects.filter(email=instance.email).first()
#     # if user:
#     #     person = Person.objects.filter(user=user).first()
#     #     if person:
#     #         diagnostic = Diagnostic.objects.filter(pessoa_uuid = instance.uuid).first()
#     #         if not diagnostic and instance.status != 'OFF':
#     #             Diagnostic.objects.create(
#     #                 person = person,   
#     #                 pessoa_uuid = instance.uuid, 
#     #                 pessoa = instance.pessoa,
#     #                 pessoa_answerable = instance.answerable,
#     #                 pessoa_sensor = instance.sensor,
#     #                 pessoa_installation_location = instance.installation_location      
#     #             )
#         # else:
#     #     diagnostic.user = instance.user
#     #     diagnostic.uuid = instance.uuid
#     #     diagnostic.pessoa = instance.pessoa
#     #     diagnostic.answerable = instance.answerable
#     #     diagnostic.sensor = instance.sensor
#     #     diagnostic.installation_location = instance.installation_location
#     #     diagnostic.save()