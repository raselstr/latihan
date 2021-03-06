from django.shortcuts import render, redirect
from pegawai.models import Pegawai
from pegawai.forms import FormPegawai
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
@login_required(login_url=settings.LOGIN_URL)
def signup(request):
    if request.POST:
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "User Berhasil dibuat!")
            return redirect('signup')
        else:
            messages.error(request, "Terjadi Kesalahan!")
            return redirect('signup')
    else:
        form = UserCreationForm()
        konteks = {
            'form':form,
        }
    return render(request, 'signup.html', konteks)


@login_required(login_url=settings.LOGIN_URL)
def hapus_pegawai(request, id_pegawai):
    pegawai = Pegawai.objects.filter(id=id_pegawai)
    pegawai.delete()

    return redirect('pegawai')
@login_required(login_url=settings.LOGIN_URL)
def ubah_pegawai(request, id_pegawai):
    pegawai = Pegawai.objects.get(id=id_pegawai)
    template = 'ubah-pegawai.html'
    if request.POST:
        form = FormPegawai(request.POST, instance=pegawai)
        if form.is_valid():
            form.save()
            messages.success(request,"Data Berhasil diperbaharui")
            return redirect('ubah_pegawai', id_pegawai=id_pegawai)
    else:
        form = FormPegawai(instance=pegawai)
        konteks = {
            'form':form,
            'pegawai':pegawai,

        }
    return render(request, template, konteks)

@login_required(login_url=settings.LOGIN_URL)
def pegawai(request):
    pgws = Pegawai.objects.all()  # menampilan seluruh data tabel
    # pgws = Pegawai.objects.filter(pangkat__pangkat = "Pengatur Tk. 1") #Menggunakan Filter pangkat dengan menampilkan nama pangkat dari Model Pangkat
    # pgws = Pegawai.objects.filter(pangkat__pangkat = "Pengatur Tk. 1") [:3] # [:3] Limit

    konteks = {
        'pgws':pgws,
        
    }
    return render(request, 'pegawai.html', konteks)

@login_required(login_url=settings.LOGIN_URL)
def tambah_pegawai(request):
    if request.POST:
        form = FormPegawai(request.POST)
        if form.is_valid():
            form.save()
            form = FormPegawai()
            pesan = "Data berhasil ditambah"

            konteks = {
                'form': form,
                'pesan' : pesan,
            }

            return render(request, 'tambah-pegawai.html', konteks)
     
    else:

        form = FormPegawai()

        konteks = {
            'form' : form,
        }

        return render(request, 'tambah-pegawai.html', konteks)