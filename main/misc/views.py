from django.views.generic import TemplateView

from main.misc.tables import FifaStandingTable
from main.utility.functions import FifaEPLStandingScrapper


class FifaView(TemplateView):
    template_name = "fifa.html"
    table_class = FifaStandingTable

    def get_table_data(self):

        data = FifaEPLStandingScrapper().get_data()
        return data

    def get_context_data(self, **kwargs):

        result = super().get_context_data(**kwargs)
        result["table"] = FifaStandingTable(self.get_table_data())

        return result
