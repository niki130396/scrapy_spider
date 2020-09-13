from rest_framework import generics
from rest_framework import filters
from rest_framework.permissions import IsAuthenticated


from parliment_api.models import Parliment
from parliment_api.serializers import MPSerializer
from parliment_api.pagination import Paginator
# Create your views here.

#TODO UNCOMMENT PERMISSION_CLASSES
class ParliamentDataById(generics.RetrieveAPIView):
    #permission_classes = [IsAuthenticated]
    serializer_class = MPSerializer
    queryset = Parliment.objects.all()


class FilterParliamentData(generics.ListAPIView):
    #permission_classes = [IsAuthenticated]
    serializer_class = MPSerializer
    pagination_class = Paginator
    filter_backends = [filters.SearchFilter]
    search_fields = ['first_name']
    queryset = Parliment.objects.all()

    # def get_queryset(self):
    #     # filter_ = request.GET['party']
    #     # connection = sqlite3.connect('C:/Users/Lenovo/PycharmProjects/scrapy_spider/parliment_spider/scrapy.db')
    #     # cursor = connection.cursor()
    #     # query = cursor.execute(f'SELECT * FROM parliment WHERE political_party = "{filter_}"').fetchall()
    #     # response = []
    #     # for item in query:
    #     #     response.append({'birth_date': item[0],
    #     #                      'birth_place': item[1],
    #     #                      'profession': item[2],
    #     #                      'languages': item[3],
    #     #                      'political_party': item[4],
    #     #                      'mail': item[5]})
    #     # return Response(response)
    #     if 'party' in self.request.GET:
    #         filter_ = self.request.GET['party']
    #         queryset = Parliment.objects.filter(political_party=filter_)
    #         return queryset
    #     queryset = Parliment.objects.all()
    #     return queryset


class ParliamentData(generics.ListAPIView):
    #permission_classes = [IsAuthenticated]
    serializer_class = MPSerializer
    pagination_class = Paginator
    filter_backends = [filters.SearchFilter]
    search_fields = ['political_party', 'birth_date']
    queryset = Parliment.objects.all()

    # def get_queryset(self):
    #     # connection = sqlite3.connect('C:/Users/Lenovo/PycharmProjects/scrapy_spider/rest_api/db.sqlite3')
    #     # cursor = connection.cursor()
    #     # query = cursor.execute('SELECT birth_date, birth_place, profession, languages, political_party, email_address FROM parliment').fetchall()
    #     # response = []
    #     # for item in query:
    #     #     response.append({'birth_date': item[0],
    #     #                      'birth_place': item[1],
    #     #                      'profession': item[2],
    #     #                      'languages': item[3],
    #     #                      'political_party': item[4],
    #     #                      'mail': item[5]})
    #     # return Response(response)
    #     if 'pp' in self.request.GET:
    #         filter_ = self.request.GET['pp']
    #         queryset = Parliment.objects.filter(political_party=filter_)
    #         return queryset
    #     elif 'bp' in self.request.GET:
    #         filter_ = self.request.GET['bp']
    #         queryset = Parliment.objects.filter(birth_place=filter_)
    #         return queryset
    #     elif 'bd' in self.request.GET:
    #         filter_ = self.request.GET['bd']
    #         queryset = Parliment.objects.filter(birth_date=filter_)
    #         return queryset
    #     queryset = Parliment.objects.all()
    #     return queryset
