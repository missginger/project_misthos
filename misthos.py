from datetime import *


episimes_argies=["1.1.2018""6.1.2018""19.2.2018""25.3.2018""6.4.2018""9.4.2018""1.5.2018""15.8.2018""28.10.2018""25.12.2018""26.12.2018"]



dayearn= input ("insert your day earnigs (6.6 hours)")
hour= dayearn/6.6


for i in range(0,7):
    hmerom= raw_input("insert the date day, month, year")
    spl=hmerom[2]
    lala=hmerom.split(spl)
    day=int(lala[0])
    month=int(lala[1])
    year=int(lala[2])
    weekday=date(year,month,day).isoweekday()


    hourstart = raw_input("the time you star")
    hourfinish = raw_input("the time you finisk")
    spl2=hourstart[2]
    lalala=hourstart.split(spl2)
    hourss=int(lalala[0])
    minouts=int(lalala[1])
    hourstart=timedelta(hours=hourss,minutes=minouts)

    spl2 = hourfinish[2]
    lalala = hourfinish.split(spl2)
    hourss = int(lalala[0])
    minouts = int(lalala[1])
    hourfinish = timedelta(hours=hourss, minutes=minouts)

    tw=timedelta(hours=12)
    if hourstart>hourfinish:
        hourfinish1=hourfinish+tw
        hourstart1=hourstart-tw
        workinghours = hourfinish1 - hourstart1
    else: workinghours = hourfinish - hourstart
    half= timedelta(hours=0,minutes=30)
    five=timedelta(hours=5,minutes=0)
    if workinghours>five: workinghours=workinghours-half
    workinghours = str(workinghours)
    work=workinghours.split(":")
    workinghours=work[0]


    if day>=1 and day <=6:
        if hourstart>=06.00 and hourfinish<22.00:

    elif (day==7) or (date in episimes_argies):

