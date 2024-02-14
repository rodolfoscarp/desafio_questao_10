from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import HttpRequest
from django.conf import settings

import folium

from .models import Locais
from .forms import CreateLocalForm


def index(request: HttpRequest):

    form = CreateLocalForm()

    m = folium.Map(location=settings.INTIAL_LOCATION,
                   zoom_start=settings.ZOOM_START,
                   width="100%",
                   height="75%",
                   )

    locais = Locais.objects.all()

    details_button = '<a class="link-primary" href="javascript:void(0);" onclick="javascript:showUpdateDeleteModal();">Detalhes</a>'

    for local in locais:
        folium.Marker(
            location=[local.latitude, local.longitude],
            tooltip=local.nome,
            popup=folium.Popup(details_button),
            icon=folium.Icon(color="green"),
        ).add_to(m)

        folium.Popup()

    context = {'map': m._repr_html_(), 'form': form}

    return render(request, 'maps/index.html', context)


def create(request: HttpRequest):

    if request.method == "POST":
        form = CreateLocalForm(request.POST)

        if form.is_valid():
            Locais.objects.create(
                nome=form.cleaned_data['nome'],
                latitude=form.cleaned_data['latitude'],
                longitude=form.cleaned_data['longitude'],
                data_expiracao=form.cleaned_data['data_expiracao']
            )

    return redirect(reverse('index'))


def update(request: HttpRequest, id: int):
    return redirect(reverse('index'))


def delete(request: HttpRequest, id: int):
    return redirect(reverse('index'))
