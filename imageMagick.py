from wand.image import Image

widthCard = 486
heightCard = 759
color = ["red", "yellow", "green", "blue"]
cardEsp = ["block", "reverse", "+2"]
blackCard = ["swithColor", "+4"]

image = Image(filename="cards.png")
for column in range(4):
    for line in range(10):
        with image.clone() as imgCrop:
            imgCrop.crop(widthCard * line, heightCard * column, widthCard * (line + 1), heightCard * (column + 1))
            if column == 0: imgCrop.save(filename="./cards/card_"+str(line+1)+"_"+color[column]+".png")
            if column == 1: imgCrop.save(filename="./cards/card_"+str(line+1)+"_"+color[column]+".png")
            if column == 2: imgCrop.save(filename="./cards/card_"+str(line+1)+"_"+color[column]+".png")
            if column == 3: imgCrop.save(filename="./cards/card_"+str(line+1)+"_"+color[column]+".png")

i = 0
for lineCE in range(10):
    with image.clone() as imgCrop:
        imgCrop.crop(widthCard * lineCE, heightCard * 4, widthCard * (lineCE + 1), heightCard * 5)
        if lineCE <= 2: imgCrop.save(filename="./cards/card_"+cardEsp[i]+"_"+color[0]+".png")
        if lineCE > 2 and lineCE <= 5: 
            imgCrop.save(filename="./cards/card_"+cardEsp[i]+"_"+color[1]+".png")
        if lineCE > 5 and lineCE <= 8:
            imgCrop.save(filename="./cards/card_"+cardEsp[i]+"_"+color[2]+".png")
        if lineCE > 8:
            imgCrop.save(filename="./cards/card_"+cardEsp[i]+"_"+color[3]+".png")
    if i != 2:
        i += 1
    else:
        i = 0

for lineBC in range(6):
    with image.clone() as imgCrop:
        imgCrop.crop(widthCard * lineBC, heightCard * 5, widthCard * (lineBC + 1), heightCard * 6)
        if lineBC < 2: 
            imgCrop.save(filename="./cards/card_"+cardEsp[lineBC+1]+"_"+color[3]+".png")
        if lineBC == 2:
            imgCrop.save(filename="./cards/card_"+blackCard[0]+"_black.png")
            
        if lineBC == 5:
            imgCrop.save(filename="./cards/card_"+blackCard[1]+"_black.png")

            
