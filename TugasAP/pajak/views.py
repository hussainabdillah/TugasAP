from django.shortcuts import render
from django.http import HttpResponse
from time import ctime
from .myutils import number_of_vowels
from .myutils import number_of_consonants
from .myutils import ubahwaktu
from .myutils import thousandsMarker
from .myutils import calculateTax

def coba(request):
    s = ubahwaktu()
    context = {
        'judul' : 'Progressive Tax Calculator',
        'nama'  : 'Hussain Abdillah Tugas Kelarno',
        'NIM'   : 'L200214201',
        'waktu' : s,
        'pesan' : 'Hello my friends, apa kabar ? I hope everything is good.',
        'nama2' : 'Ilham Aufal Hadad',
        'NIM2'  : 'L200214071',
        'nama3' : 'Pandu Putra Wijaya',
        'NIM3'  : 'L200214174',
        'Dosen' : 'Fajar Suryawan, Ph.D'
    }

    if request.POST:
        rt = request.POST.get('tax')
        try:
            if int(rt) > 0:
                resultTaxt = calculateTax(int(rt))
                total = 0
                for x in resultTaxt:
                    total += int(x[2].replace("Rp ", "").replace(".", ""))
                total = thousandsMarker(total)
                rtCur = thousandsMarker(int(rt))
                context.update({"rt" : rt, "rtCur" : rtCur , "resultTax" : resultTaxt, "totalTax" : total, })
            else:
                context.update({"exc":"Please enter a positive integer ! "})
                
        except:
            context.update({"exc":"Please enter a positive integer ! "})

    return render(request, 'pajak/index.html', context)

def about(request):
    return render(request, 'pajak/about.html')
