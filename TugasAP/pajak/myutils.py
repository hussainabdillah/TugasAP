from time import ctime

def number_of_vowels(s):
    vowels = 'aiueo'
    c = 0
    for i in s.lower():
        if i in vowels:
            c = c + 1
    return c

def number_of_consonants(x):
    consonants = 'qwrtypsdfghjklzxcvbnm'
    p = 0
    for i in x.lower():
        if i in consonants:
            p = p + 1
    return p

day = { 'Sun' : 'Ahad',
        'Mon' : 'Senin',
        'Tue' : 'Selasa',
        'Wed' : 'Rabu',
        'Thu' : 'Kamis',
        'Fri' : 'Jumat',
        'Sat' : 'Sabtu'}

month = {'Jan' : 'Januari',
         'Feb' : 'Februari',
         'Mar' : 'Maret',
         'Apr' : 'April',
         'May' : 'Mei',
         'Jun' : 'Juni',
         'Jul' : 'Juli',
         'Aug' : 'Agustus',
         'Sep' : 'September',
         'Oct' : 'Oktober',
         'Nov' : 'November',
         'Dec' : 'Desember'}

def ubahwaktu():
    now = ctime()
    _day    = now[0:3]
    _month  = now[4:7]
    _date   = now[8:10]
    _clock  = now[11:19]
    _year   = now[20:24]
    sekarang = day[_day]+' '+ _date +' '+ month[_month]+' '+ _year+' '+ "Pukul "+' '+ _clock
    return sekarang

def thousandsMarker(x):
    a = (f"{x:,}" .replace(',', '.'))
    str(a)
    return "Rp " + a

brackets = {       0:0,
             1000000:5,
             3000000:10,
             6000000:15,
            10000000:20,
            20000000:25,
            35000000:30,
            55000000:35,
            80000000:40,}

def calculateTax(param):
    lPoint,lPercent,totalTax, has, totalBracket, resultData = 0, 0, 0, param, len(brackets), []
    for enum,(key,item) in enumerate(brackets.items(),1):
        lOc = key - lPoint
        if lOc > 0 :
            if has > lOc:
                added = lOc * lPercent / 100
                totalTax += added
                resultData.append((str(thousandsMarker(lPoint))+" ⎯⎯ "+str(thousandsMarker(key)),(str(lPercent)+"%"), thousandsMarker(int(added))))
                has -= lOc
            else:
                added = has * lPercent / 100
                totalTax += added
                resultData.append((str(thousandsMarker(lPoint))+" ⎯⎯ "+str(thousandsMarker(key)),(str(lPercent)+"%"), thousandsMarker(int(added))))
                has = 0
            if enum == totalBracket:
                added = has * item / 100
                totalTax += added
                resultData.append((str(thousandsMarker(key))+" ⎯⎯ ...", (str(item)+"%"), thousandsMarker(int(added))))
        lPercent = item
        lPoint = key
    return resultData