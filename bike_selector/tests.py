from django.test import TestCase
from views import bike_search
from forms import BikeSearchForm
from django.core.urlresolvers import resolve
from django.shortcuts import render_to_response


class BikeSelectorPageTest(TestCase):

    def test_bike_selector_page_resolves(self):
        bike_selector_page = resolve('/bike_selector/')
        self.assertEqual(bike_selector_page.func, bike_search)

    def test_bike_selector_page_status_code_is_okay(self):
        bike_selector_page = self.client.get('/bike_selector/')
        self.assertEqual(bike_selector_page.status_code, 200)

    def test_check_bike_selector_content_is_correct(self):
        self.maxDiff = None
        bike_selector_page = self.client.get('/bike_selector/')
        self.assertTemplateUsed(bike_selector_page, "bike_selector/bike_selector.html")
        bike_selector_page_template_output = render_to_response("bike_selector/bike_selector.html",
                                                                {'form': BikeSearchForm()}).content
        self.assertEqual(bike_selector_page.content, bike_selector_page_template_output)
